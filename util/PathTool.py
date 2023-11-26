import os

def genFileSavePath(*args,productName:str,type=".pdf"):
    """
    拼接文件路径
    :param args:
    :param productName: testcase目录下分产品存放，这个参数就是testcase下的产品目录名称
    :param type:
    :return:
    """
    filePath= os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"testcase",productName,"files")
    fileName = ""
    for arg in args:
        fileName = fileName + f"{arg}__"
    return os.path.join(filePath,fileName[:-2]+type)
