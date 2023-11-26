import requests
from util.MysqlTool import Mysql
from data.Teprunner_DataManager import API_BASE_URL,DB_CONFIG
from typing import Dict
import json

class TeprunnerBaseClient(object):
    """
    根据某个平台的url、用户登录密码，构造基础的请求客户端
    """
    appClient = requests.Session() # 请求客户端
    apiBaseUrl:str = API_BASE_URL # api的基础路径
    token:str = None # token
    dbClient = Mysql(ip=DB_CONFIG["ip"],port=DB_CONFIG["port"],user=DB_CONFIG["user"],password=DB_CONFIG["password"],database=DB_CONFIG["database"]) # 数据库客户端

    url: str = "/"  # api路径，每个resource可变化
    params: Dict = {} # url参数，每个resource可变化
    body: Dict = {} # json报文，每个resource可变化
    headers: Dict = {
        "content-type": "application/json",
    } # 请求头，每个resource可变化

    def __init__(self):
        res = self.post(url="/api/users/login",body={"username":"admin","password":"qa123456"})
        self.token = res["data"]["token"]
        self.headers["Authorization"] = f"Bearer {self.token}"

    def get(self,url:str="",params:Dict= {},body:Dict={},headers:Dict={}):
        url = self.apiBaseUrl+url if url else self.apiBaseUrl+self.url
        headers = headers if headers else self.headers
        params = params if params else self.params
        body = body if body else self.body
        response = self.appClient.get(url = url,params=params,data=json.dumps(body),headers=headers)
        ret = {
            "status_code": response.status_code,
            "data": ""
        }
        try:
            ret["data"] = json.loads(response.text)
        except:
            ret = response.text
        finally:
            return ret

    def put(self, url: str = "", params: Dict = {}, body: Dict = {}, headers: Dict = {}):
        url = self.apiBaseUrl + url if url else self.apiBaseUrl + self.url
        headers = headers if headers else self.headers
        params = params if params else self.params
        body = body if body else self.body
        response = self.appClient.put(url=url, params=params, data=json.dumps(body), headers=headers)
        ret = {
            "status_code": response.status_code,
            "data": ""
        }
        try:
            ret["data"] = json.loads(response.text)
        except:
            ret = response.text
        finally:
            return ret

    def post(self, url: str = "", params: Dict = {}, body: Dict = {}, headers: Dict = {}):
        url = self.apiBaseUrl + url if url else self.apiBaseUrl + self.url
        headers = headers if headers else self.headers
        params = params if params else self.params
        body = body if body else self.body
        response = self.appClient.post(url=url, params=params, data=json.dumps(body), headers=headers)
        ret = {
            "status_code": response.status_code,
            "data": ""
        }
        try:
            ret["data"] = json.loads(response.text)
        except:
            ret = response.text
        finally:
            return ret

    def delete(self, url: str = "", params: Dict = {}, body: Dict = {}, headers: Dict = {}):
        url = self.apiBaseUrl + url if url else self.apiBaseUrl + self.url
        headers = headers if headers else self.headers
        params = params if params else self.params
        body = body if body else self.body
        response = self.appClient.delete(url=url, params=params, data=json.dumps(body), headers=headers)
        ret = {
            "status_code": response.status_code,
            "data": ""
        }
        try:
            ret["data"] = json.loads(response.text)
        except:
            ret = response.text
        finally:
            return ret

if __name__ == "__main__":
    clt = TeprunnerBaseClient()
    res = clt.get(url="/api/teprunner/cases/1")
    print("test")