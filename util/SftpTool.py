import paramiko
import os

class SFTP:
    __attrs__ = ["hostname","port","username","password","transport","sftp"]

    def __init__(self, hostname:str, port:int, username:str, password:str):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password

    def __connect(self):
        self.transport = paramiko.Transport((self.hostname,self.port))
        self.transport.connect(username=self.username,password=self.password)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)
        return self.sftp

    def __close(self):
        self.sftp.close()
        self.transport.close()

    def mkdir_p(self, path):
        """
        逸归创建日录
        :param path: 日录名
        """
        if path == "/":
            self.sftp.chdir('/')
            return
        if path == '':
            return
        try:
            self.sftp.chdir(path)
        except IOError:
            dirname,basename = os.path.split(path.rstrip('/'))
            self.mkdir_p(dirname)
            self.sftp.mkdir(basename)
            self.sftp.chdir(basename)
        return True

    def put(self,local_file_path:str, remote_file_path:str,dir_exist:bool = False):
        """
        上传文件
        :param local_file_path:
        :param remote_file_path:
        :return:
        """
        self.__connect()
        if dir_exist:
            dirpath = os.path.dirname(remote_file_path)
            self.mkdir_p(dirpath)
        self.sftp.put(local_file_path,remote_file_path)
        self.__close()

    def get(self, remote_file_path:str,local_file_path:str):
        """
        下载文件
        :param local_file_path:
        :param remote_file_path:
        :return:
        """
        self.__connect()
        self.sftp.get(remote_file_path,local_file_path)
        self.__close()

if __name__ == "__main__":
    sftp_hitest = SFTP(hostname="localhost",port=57000,username="sftp_hitest",password="qa123456")
