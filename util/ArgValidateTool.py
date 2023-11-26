import json
import copy


def requriedArgValidate_bodyRender(bodyjson: str, requiredKeys: dict):
    """
    将请求报文的json字符串内容，根据必填字段进行渲染
    :param bodyjson:
    :param requiredKeys:
    :return: 一个渲染后的json请求报文
    """
    from jinja2 import Environment, Template
    env = Environment()
    template: Template = env.from_string(bodyjson)
    view = template.render(requiredKeys)
    return json.loads(view)


def requriedArgValidate_bodyListGenerator(bodyjson: dict, requiredKeys: list):
    """
    遍历必填参数字段，分别构造字段值不传、为None、为""时的报文
    :param bodyjson:
    :param requiredKeys:
    :return: 一个json报文列表
    """
    retBodyList = []
    for key in requiredKeys:
        # 不传
        tmp = copy.deepcopy(bodyjson)
        tmp.pop(key)
        retBodyList.append(tmp)
        # 为None
        tmp = copy.deepcopy(bodyjson)
        tmp[key] = None
        retBodyList.append(tmp)
        # 为空字符串"
        tmp = copy.deepcopy(bodyjson)
        tmp[key] = ""
        retBodyList.append(tmp)
    return retBodyList
