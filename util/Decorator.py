import functools
import time
from loguru import logger
import os

RUN_TAG = os.environ.get("RUN_TAG","debug")
RUN_TAG_LIST = os.environ.get("RUN_TAG_LIST","debug")
DEBUG_MODULE = os.environ.get("RUN_MODULE","debug")

class RetryFlag(Exception):
    """
    插获该异常并重试
    """

def retry(reruns:int,reruns_delay:int,exception=(RetryFlag,)):
    """
    重试装饰器
    :param reruns：函数重试次数，n表示函数在第一次失败后会再执行n次
    :param reruns_delay：函数重试间赠延时，单位：秒
    :param exception：支持插获的失败异常，默认为AssertionError，即：仅在触发AssertionError 时重试
    sreturn:
    """
    if reruns< 0 or reruns_delay < 0:
        raise ValueError(f"重试次数和重试间隔必须大于0")

    def wrapper_outer(func):
        @functools.wraps(func)
        def wrapper_inner(*args,**kwargs):
            error = None
            for current_retry in range(1,reruns+1):
                try:
                    return func(*args,**kwargs)
                except exception as err:
                    if current_retry == reruns:
                        logger.error(err)
                    else:
                        logger.warning(err)
                    logger.info(f"函数重试第 {current_retry}次，函数名：{func.__name__}，参数：args={args} kwargs={kwargs}")
                    logger.info(f"waiting... {reruns_delay}s")
                    time.sleep(reruns_delay)
                    error = err
            logger.error("已达到最大重试次数！")
            raise error
        return wrapper_inner
    return wrapper_outer

def custom_skipUnless(tag_list):
    """
      功能：unittest用例过滤装饰器
        使用：to1st是要给用例打标的标签列表，运行总运行文件时，可以填多个标签，执行命中这些标签的用例
          sit用例：如23.10.17sit
        标金设规范：
          冒烟用例：如23.10.17smoke
          同扫用例：如regress
    """
    def decorator(test_item):
      if not[value for value in tag_list if value in RUN_TAG_LIST.split(",")]:
          test_item.__unittest_skip__ = True
          test_item.__unittest_skip_why__ = "不在标签列表内"
      return test_item
    return decorator
