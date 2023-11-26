import cx_Oracle
import os
from typing import Union

class Oracleclientl2:
    __attrs__ = [ 'connection','ip','port','user', 'password', 'service_name']

    def __init__(self, ip:str, port:Union[str,int], user:str, password:str, service_name:str):
        # 以下环境变量，如若需要指定客户端版本环境变量，可以取消注释
        # os.environ["ORACLE_HOME"] = r'D:\instantclient_21_3'
        # oS.environ["LD_LIBRARY_PATH"] = r'D\instantclient_21_3'

        # os.environ["ORACLE HOME] = '/usr/local/instantelient_21_6'
        # os.environ["LD_LIBRARY_PATH"]=/usr/local/instantclient_21_6'

        os.environ["NLS_LANG"] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
        self.ip = ip
        self.port = str(port)
        self.user=user
        self.password= password
        self.service_name= service_name
        sql = user+"/" +password+"@"+ip+":"+str(port)+"/"+service_name
        try:
            self.connection = cx_Oracle.connect(sql)
        except cx_Oracle.DatabaseError:
            pass
        finally:
            pass

    def checkConnect(self):
        sql = self.user + "/" + self.password + "@" + self.ip + ":" + self.port + "/" + self.service_name
        ret = False
        try:
            connect = cx_Oracle.connect(sql)
            if connect:
                ret = True
                connect.close()
        except cx_Oracle.DatabaseError:
            ret = False
        finally:
            pass
        return ret

    def select(self, sql:str):
        cursor = self.connection.cursor()
        ret = False
        try:
            cursor.execute(sql)
            rows = cursor.fetchall()
            cols = [d[0] for d in cursor.description]
            ret = []
            for row in rows:
                b = dict(zip(cols, row))
                ret.append(b)
            if len(ret):
                ret = True
        except:
            ret = False
        finally:
            pass
        return ret

    def insert(self,sql:str):
        cursor = self.connection.cursor()
        ret = False
        try:
            cursor.prepare(sql)
            cursor.execute(sql)
            self.connection.commit()
            ret = True
        except:
            self.connection.rollback()
            ret = False
        finally:
            pass
        return ret

    def update(self,sql:str):
        cursor = self.connection.cursor()
        ret = False
        try:
            cursor.prepare(sql)
            cursor.execute(sql)
            self.connection.commit()
            ret = True
        except:
            self.connection.rollback()
            ret = False
        finally:
            pass
        return ret

    def delete(self,sql:str):
        cursor = self.connection.cursor()
        ret = False
        try:
            cursor.prepare(sql)
            cursor.execute(sql)
            self.connection.commit()
            ret = True
        except:
            self.connection.rollback()
            ret = False
        finally:
            pass
        return ret

    def excuteBlock(self,sql:str,params=()):
        cursor = self.connection.cursor()
        ret = False
        try:
            cursor.execute(sql,params)
            self.connection.commit()
            ret = True
        except:
            self.connection.rollback()
            ret = False
        finally:
            pass
        return ret

