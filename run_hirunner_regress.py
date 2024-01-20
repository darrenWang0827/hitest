from pathlib import Path
from util.TestRunnerTool import TestRunner


class Runner(TestRunner):
    """
    原先git工程自带的运行器运行
    """
    idc = "I"
    prd_name: str = "Teprunner"  # 产品名称 | 用例所在文件夹名称
    version: str = "23.11.23"  # 版本号
    test_stage: str = "回归"  # 测试阶段如冒烟，SIT，回归
    case_dir = Path('testcase/Teprunner/RegressTest/联机接口/用例')
    case_file_pattern = "Test_*.py"  # 用例文件匹配表达式
    run_user: str = "darrenwang"
    RUN_MODULE: str = "test"  # 执行模式，默认debug
    RUN_TAG_LIST: str = "regress,"  # 用例标签，默认debug，支持多个标签选择，请用逗号隔开
    reruns: int = 0  # 失败重试次数
    is_upload: bool = False  # 是否上传到SFTP服务器
    is_open_report: bool = False  # 是否自动打开测试报告


if __name__ == "__main__":
    runner = Runner()
    runner.run()
