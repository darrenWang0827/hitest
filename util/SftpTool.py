import paramiko

class SFTP:
    __attrs__ = ["hostname","port","username","password","transport","sftp"]

    def __init__(self, hostname:str, port:int, username:str, password:str):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password

    def __connect(self):
        self.transport = paramiko.Transport((self.hostnameself.port))
        self.transport.connect(username=self.username,password=self.password)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)
        return self.sftp

    def __close(self):
        self.sftp.close()
        self.transport.close()

    def put(self,local_file_path:str, remote_file_path:str):
        """
        上传文件
        :param local_file_path:
        :param remote_file_path:
        :return:
        """
        self.__connect()
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

sftp_hitest = SFTP(hostname="localhost",port=57000,username="sftp_hitest",password="qa123456")
