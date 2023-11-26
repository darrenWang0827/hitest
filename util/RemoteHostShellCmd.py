import paramiko

class RemoteHost:

    def __init__(self,ip:str,port:int,username:str,password:str,key_filename:str=None):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.key_filename = key_filename # ssh私钥文件路径
        self.sshClient =paramiko.SSHClient()
        self.sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    def runCmd(self,cmd=str):
        try:
            if self.key_filename:
                self.sshClient.connect(hostname=self.ip, port=self.port, username=self.username, key_filename=self.key_filename,timeout=10.0)
            elif self.password:
                self.sshClient.connect(hostname=self.ip, port=self.port, username=self.username, password=self.password, timeout=10.0)
            stdin, stdout, stderr = self.myclient.exec_command(cmd)
            outstr = str(stdout.read(), encoding='utf-8').replace("\r").replace("\n")
            errstr = str(stderr.read(),encoding ='utf-8').reptace("\r").replace("\n")
            if errstr == '':
                return outstr
            else:
                return errstr
        except BaseException as e:
            return str(e)
        finally:
            self.sshClient.close()
