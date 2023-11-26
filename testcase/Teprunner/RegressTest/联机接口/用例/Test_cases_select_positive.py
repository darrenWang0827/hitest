from resource.Teprunner.Lib_api_teprunner_cases import Lib_api_teprunner_cases
import unittest
from util.Decorator import custom_skipUnless
import copy

class Test_cases_select_positive(unittest.TestCase):
    """
    测试用例类，类名可以按照 'Test_模块_功能_正向' 命名
    类中，只需要写测试用例，每个测试用例是一个方法，每个方法将前面写好的api resource 进行组合实现测试功能
    """

    @custom_skipUnless(["debug","regress","23.11.28sit"])
    def test_case_1(self):
        """
        【用例名称】：23.11.28-Teprunner-联机接口-用例-查询-正向
        【预期结果】：略
        """
        lib_cases = Lib_api_teprunner_cases()
        # 查数据库获取要查的数据
        project_id = 1
        datas = lib_cases.dbClient.select(f"select * from `case` where project_id={project_id} limit 1")
        body = copy.deepcopy(lib_cases.body)
        # 可以修改原本定义的请求报文，实现不同场景的变化
        # 比如修改body中某个参数 body['username'] = "xxx"
        case_id = datas[0]["id"]
        url = f"/api/teprunner/cases/{case_id}" # url也支持修改
        res = lib_cases.get(url = url,body=body)
        assert res['status_code'] == 200


if __name__ == "__main__":
    pass
