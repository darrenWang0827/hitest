import os
import json
import sys
import unittest
import unittestreport
from datetime import datetime
from functools import cached_property
from pathlib import Path
from typing import Literal
from jinja2 import Environment,FileSystemLoader

from util.SftpTool import SFTP
sftp_hitest = SFTP(hostname="localhost",port=57000,username="sftp_hitest",password="qa123456")

class TestRunner:
    idc: str # 测试环境IDC
    prd_name: str # 产品名称
    version: str # 版本号
    test_stage: Literal['冒烟','SIT','回归'] = 'SIT' # 测试阶段
    run_user:str # 执行人
    case_dir: Path # 测试用例目录，支持中文
    case_file_pattern: str = 'Test_*.py' # 测试用例文件匹配表达式
    RUN_TAG_LIST: str = 'debug,' # 测试用例执行时的筛选标签，默认debug,调试的时候用
    thread_count:int=1 # 执行最大线程数，大于1时，可以多个用例并行执行，但是请注意多个用例执行时，它们直接的数据冲突问题
    reruns: int= 0 # 失败重试次数
    is_upload: bool= False # 是否将测试报告上传到sftp服务器
    is_open_report: bool = True # 执行结束后，是否自动打开浏览器查看测试报告结果

    @cached_property
    def suite(self):
        return unittest.TestSuite()

    @property
    def report_title(self) -> str:
        """
        测试报告标题
        :return:
        """
        return f"【{self.prd_name}】{self.version}--{self.test_stage}测试报告"

    @cached_property
    def report_filename(self)-> str:
        """
        测试报告生成的html文件名
        :return:
        """
        return f'{self.prd_name}_{self.version}_{datetime.now().strftime("%Y%m%d%H%M%S")}_report.html'

    @property
    def local_report_path(self) -> Path:
        """
        本地测试报告存放路径
        :return:
        """
        return (Path(__file__).parent / Path('../report') / self.report_filename).resolve()

    @cached_property
    def report_url(self) -> str:
        """
        测试报告url访问连接
         这里是用nginx搭建的文件服务器，将sftp上传上来的测试报告用url连接展示
        :return:
        """
        return f'http://localhost/hitest_report/{self.prd_name}/{self.report_filename}'

    def run(self):
        """
        运行测试用例，生成测试报告
        :return:
        """
        self.load_case()
        self.check_case()
        self.set_environ()
        report_runner = unittestreport.TestRunner(
            suite=self.suite,
            tester = self.run_user,
            filename = str(self.local_report_path),
            title = self.report_title,
            report_dir = '.',
            desc = '测试报告'
        )
        report_runner.run(
            thread_count = self.thread_count,
            count = self.reruns, # 重试次数
            interval = 2  # 重试运行间隔时间
        )
        # 重新生成测试报告
        self.regenerate_test_report(report_runner)

    def load_case(self):
        """
        加载测试用例
        :return:
        """
        test_loader = unittest.TestLoader()
        self.suite.addTests(test_loader.discover(str(self.case_dir.resolve()), pattern=self.case_file_pattern, top_level_dir = None))

    def check_case(self):
        """执行前检查测试用例"""
        tests: list = getattr(self.suite,'_tests')
        for suites in tests.copy():
            suites: list
            suite_cases: list = getattr(suites, '_tests')
            if not suite_cases:  # 空套件
                tests.remove(suites)
            for suite in suite_cases:
                for case in suite:
                    method_doc = getattr(case, '_testMethodDoc','')
                    if not method_doc or '【用例名称】' not in method_doc:
                        raise ValueError(
                            f"[{case.__module__}.{case.__class__.__name__}.{getattr(case, '_testMethodName')}]需修改测试用例说明")
                    setattr(case, 'case_name', method_doc.split("【用例名称】：")[1].split("\n")[0])
                    new_method_doc = method_doc.replace("\n","<br>")
                    setattr(case, '_testMethodDoc',new_method_doc)
        if not tests:
            raise ValueError("未选择测试用例，请检查！")

    def regenerate_test_report(self,report_runner: unittestreport.TestRunner):
        """
        重新生成测试报告
        :param repopt_runner:
        :return:
        """
        test_result = report_runner.test_result
        results = test_result['results']
        for case_result in results.copy():
            # 报告中去掉跳过的用例
            if case_result.state == '跳过':
                results.remove(case_result)
                test_result['skip'] -= 1
                test_result['all'] -= 1
                continue
            # 解决报告XmL格式显示不完整的问题
            case_result.runner = [i.replace( '<','&lt').replace('>','&gt') for i in case_result.run_info]
            # 在result中追加报文数据的属性
            if case_result.method_name in getattr(case_result,'caseToBodyMappings',dict()):
                case_result.body = json.dumps(case_result.caseToBodyMappings[case_result.method_name],
                                              ensure_ascii = False,indent = 4).replace('<','&lt').replace('>','&gt')
        # 重新计算通过率上面去掉了跳过的用例
        test_result["pass_rate"] = f'{100 * test_result["success"] / test_result["all"]:.2f}'

        # 重新生成测试报告
        env = Environment(loader=FileSystemLoader(os.path.dirname(__file__)))
        template = env.get_template('templates.html')  # 测试报告模板
        with open(self.local_report_path,'wb') as f:
            f.write(template.render(test_result).encode('utf8'))

        # 上传测试报告到sftp
        self.upload2sftp()

        # 返回执行结果给调度平台
        report_json = {}
        for k,v in test_result.items():
            if isinstance(v, (int, str)):
                report_json[k] = v

        # 自动打开测试报告
        if self.is_open_report:
            if self.is_upload:
                os.startfile(self.local_report_path)
                report_json["report_url"] = str(self.local_report_path)
        else:
            os.startfile(self.local_report_path)
            report_json['report_url'] = str(self.local_report_path)
        json.dump(report_json,fp = sys.stdout,ensure_ascii = False)  # 这里是打印给测i试调度平台对接用的，请勿删除

    def upload2sftp(self):
        """
        上传文件到SFTP服务器，远程需要有文件夹存在
        :return:
        """
        if self.is_upload:
            sftp_hitest.put(str(self.local_report_path),f'/{self.prd_name}/{self.report_filename}')

    def set_environ(self):
        """
        设置环境变量
        :return:
        """
        for attribute in dir(self):
            # 大写的变量，设置为环境变量
            if attribute.isupper() and hasattr(self, attribute):
                os.environ[attribute] = getattr(self,attribute)
