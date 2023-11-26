import pymysql
from typing import Union


class Mysql:
    """
    mysql增、删、查、改、块执行、块的填充参数执行
    """
    __attrs__ = ["ip", "port", "user", "password", "database"]

    def __init__(self, ip: str, port: int, user: str, password: str, database: str):
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def select(self, sql: str):
        connection = pymysql.connect(host=self.ip, port=self.port, user=self.user, password=self.password,
                                     database=self.database, cursorclass=pymysql.cursors.DictCursor, connect_timeout=60)
        cursor = connection.cursor()
        ret = False
        try:
            cursor.execute(sql)
            ret = []
            datas = cursor.fetchall()
            for row in datas:
                ret.append(row)
            if len(ret) == 0:
                ret = True
        except:
            ret = False
        finally:
            if connection:
                connection.close()
        return ret

    def insert(self, sql: str):
        connection = pymysql.connect(host=self.ip, port=self.port, user=self.user, password=self.password,
                                     database=self.database, connect_timeout=60)
        cursor = connection.cursor()
        ret = False
        try:
            cursor.execute(sql)
            if cursor.rowcount:
                connection.commit()
                ret = True
        except:
            ret = False
        finally:
            if connection:
                connection.close()
        return ret

    def update(self, sql: str):
        connection = pymysql.connect(host=self.ip, port=self.port, user=self.user, password=self.password,
                                     database=self.database, connect_timeout=60)
        cursor = connection.cursor()
        ret = False
        try:
            cursor.execute(sql)
            if cursor.rowcount:
                connection.commit()
                ret = True
        except:
            ret = False
        finally:
            if connection:
                connection.close()
        return ret

    def delete(self, sql: str):
        connection = pymysql.connect(host=self.ip, port=self.port, user=self.user, password=self.password,
                                     database=self.database, connect_timeout=60)
        cursor = connection.cursor()
        ret = False
        try:
            cursor.execute(sql)
            if cursor.rowcount:
                connection.commit()
                ret = True
        except:
            ret = False
        finally:
            if connection:
                connection.close()
        return ret

    def prepareExecute(self, sql: str, args: Union[tuple, list, dict] = ()):
        connection = pymysql.connect(host=self.ip, port=self.port, user=self.user, password=self.password,
                                     database=self.database, connect_timeout=60)
        cursor = connection.cursor()
        ret = False
        try:
            cursor.execute(sql, args=args)
            ret = True
        except:
            ret = False
        finally:
            if connection:
                connection.close()
        return ret
