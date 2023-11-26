from resource.TeprunnerBaseClient import TeprunnerBaseClient

class Lib_api_teprunner_cases(TeprunnerBaseClient):
    """
    resource里边只需要配置url路径和报文格式
    """
    url = "/api/teprunner/cases/1"
    body = {} # get请求中报文为空

