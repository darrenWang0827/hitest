from pathlib import Path
from hitest_tool.HirunnerReporter import HirunnerReporter


class Runner(HirunnerReporter):
    """
    通过hitest_rool子模块提供的运行器运行，用于对接hirunner平台
    """
    # 必填参数
    prd_name: str = 'EFAS'
    # 产品名称请用能区分各自负责的产品的大写英文，如签章使
    run_user: str = 'darrenwang(王成)'
    # 测试用例执行人
    case_dir: Path = Path('testcase/EFAS/vRegressTest/联机接口')  # 用例目录
    case_file_pattern: str = 'Test_*.py'
    RUN_TAG_LIST: str = 'pegress,'  # 用例标签跳过不在列表中标签的用例

    # 其他可选参数，开关控制
    reruns: int = 0
    # 失败重试次数
    is_upload: bool = True
    # 是否上传到SFTP服务器
    is_open_report: bool = True
    # 是否自动打开测试报告
    is_report_channel: bool = True
    case_source: str = '2130'

    # 自动化产能数据相关
    # 其他自定义全局参数，由is_set_env和父类的set_environ()方法设置到环境变量中，请自
    is_set_env: bool = True
    RUN_MODULE: str = "test"

if __name__ == "__main__":
    runner = Runner()
    runner.run()