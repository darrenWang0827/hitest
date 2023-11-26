import random
import string
from datetime import timedelta,date,datetime

def generate_id_card():
    """
    生成身份证号
    :return:
    """
    #生成前6位地区码
    region_code = str(random.randint(110000,659804))
    #生成中间8位出生日期
    year=str(random.randint(1900,2022)).zfill(4)
    month=str(random.randint(1,12)).zfill(2)
    day=str(random.randint(1,28)).zfill(2)
    birth_date = f"{year}-{month}-{day}"
    #生成顺序码（后4位）
    sequence_code =str(random.randint(1,99)).zfill(2)+"7"
    #计算校验码
    id_number = region_code + birth_date + sequence_code
    check_code = calc_check_code(id_number)
    return id_number + check_code

def calc_check_code(id_number:str):
    """
    计算身份证最后一位校验码
    :param id_number:
    :return:
    """
    factors = [int(i) for i in id_number]
    weights = [int(i) for i in '7 9 10 5 8 4 2 1 6 3 7 9 10 5 8 4 2'.split()]
    total = sum(f * w for f,w in zip(factors,weights))
    check_code_dict = {0:'1',1:'0',2:'X',3:'9',4:'8',5:'7',6:'6',7:'5',8:'4',9:'3',10:'2'}
    return check_code_dict[total % 11]

def generate_taiwan_tomainland_card(length: int=8):
    """
    生成台湾大陆通行证号码
    :param length:
    :return:
    """
    digits = "0123456789"
    return ''.join(random.choice(digits) for _ in range(length))

def generate_gangao_tomainland_card(type: int=1):
    """
    生成港澳通行证号码
    :param type:
    :return:
    """
    digits = "0123456789"
    if type == 1:
        return random.choice(["H","M"]) + ''.join(random.choice(digits) for _ in range(10))
    elif type==2:
        return random.choice(["c","M"]) + ''.join(random.choice(digits) for _ in range(8))
    else:
        return "CZ"+''.join(random.choice(digits) for _ in range(7))

def generate_leaglePerson_code(length: int=18):
    """
    生成法人代码证号码
    :param length:
    :return:
    """
    digits = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(digits) for _ in range(length))

def generate_passport_number(length: int=9):
    """
    生成护照号码
    :param length:
    :return:
    """
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_military_id(length: int=18):
    """
    生成军人身份证号码
    :param length:
    :return:
    """
    digits = '0123456789'
    return ''.join(random.choice(digits) for _ in range(length))

def generate_permanentresidencepermitid(length: int=12):
    """
    生成外国人永久居留证号码
    :param Length:
    :return:
    """
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(characters) for _ in range(length))

def generate_police_id(length: int=18):
    """
    生成武装警察身份证号码
    :param length:
    :return:
    """
    digits = '0123456789'
    return ''.join(random.choice(digits) for _ in range(length))

def generate_tax_registration_certificate(length: int=15):
    """
    生成税务登记证号码
    :param length:
    :return:
    """
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(characters) for _ in range(length))

def generate_random_business_registration_certificate(length: int=15):
    """
    生成工商登记证号码
    :param length: 
    :return: 
    """
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(characters) for _ in range(length))

def generate_random_businessLicense(length: int=15):
    """
    生成企业经营热照号码
    :param length:
    :return:
    """
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(characters) for _ in range(length))

def generate_organization_code():
    """
    生成企业组织机构代码
    :return: 
    """
    #组织机构代码证的格式：8位数字或大写英文字母 + "-" + 1位数字或大写英文字母
    code = ''.join(random.choices(string.digits + string.ascii_uppercase,k=8))+ '-' +random.choice(string.digits + string.ascii_uppercase)
    return code

def generate_credit_code():
    """
    生成企业统一社会信用代码
    :return:
    """
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    code = random.choice(letters)#第一个字符为数字或大写字母
    for _ in range(17):
        code += random.choice(letters) #后面17个字符为数字或大写字母
    return code

def get_todaystr(deltadays: int = 0, needHour: bool = False):
    """
    获取当天的时间字符串
    :param deltadays:
    :param needHour:
    :return:
    """
    if needHour:
        return (datetime.now+timedelta(days=deltadays)).strftime("%Y-%m-%d %H:")
    return (datetime.now+timedelta(days=deltadays)).strftime("%Y-%m-%d")

def qet_date_of_last_week():
    """
    获取上周的开始与结束日期
    return:str,date tuple
    """
    today = date.today()
    beqin_of_last_week = (today - timedelta(days=today.isoweekday() + 6 ).strftime("%y-%m-%d"))
    end_of_Last_week = (today - timedelta(days=today.isoweekday())).strftime("%y-%m-%d")
    return beqin_of_last_week,end_of_Last_week

def get_date_of_last_two_week():
    """
    获取上两周的开始与结束日期
    return:str,date tuple
    """
    today = date.today()
    begin_of_last_week = (today - timedelta(days = today.isoweekday()+13)).strftime("%Y-%m-%d")
    end_of_last_week = (today - timedelta(days=today.isoweekday())).strftime("%Y-%m-%d")
    return begin_of_last_week,end_of_last_week

SURNAME_LIST = """赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康伍余元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明藏计伏成戴谈宋茅庞熊纪舒屈项祝董梁杜阮蓝闵席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯昝管卢莫经房裘缪干解应宗丁宣贲邓郁单杭洪包诸左石崔吉钮龚程嵇邢滑裴陆荣翁荀羊於惠甄麴家封芮羿储靳汲邴糜松井段富巫乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘斜厉戎祖武符刘景詹束龙叶幸司韶郜黎蓟薄印宿白怀蒲邰从鄂索咸籍赖卓蔺屠蒙池乔阴鬱胥能苍双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍舄璩桑桂濮牛寿通边扈燕冀郏浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庾终暨居衡步都耿满弘匡国文寇广禄阙东殴殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空曾毋沙乜养鞠须丰巢关蒯相查后荆红游竺权逯盖益桓公俟赏微生羊舌海归藏琴岳帅缑亢况有琴壤归海共岳琴晋楚闫法汝鄢涂钦归海海归藏琴岳帅缑亢况有琴壤归海共岳琴晋楚闫法汝鄢涂钦段干百里东郭南门呼延归海海归藏琴岳帅缑亢况有琴壤归海共岳琴晋楚闫法汝鄢涂钦段干百里东郭南门呼延归海海归藏琴岳帅缑亢况有琴壤归海共岳琴晋楚闫法汝鄢涂钦段干百里东郭南门呼延王"""
GIVENNAME_LIST = """明丽伟娟华国静玲刚秀文磊宇阳雨志俊莉强霞龙红鹏丹浩美萍梅亮琳博彬军玉丹洁辉飞辰晨宁恒迪晓晶欣立佳卓婷凯勇敏凡春夏秋冬丰杰雪兰颖明子伊岚可倩妍仪萱妙琪美琦萌雯蕾柳惠雅晴宜芬芳苗如媛婉薇露明丽伟娟华国静玲刚秀文磊宇阳雨志俊莉强霞龙红鹏丹浩美萍梅亮琳博彬军玉丹洁辉飞辰晨宁恒迪晓晶欣立佳卓婷凯勇敏凡春夏秋冬丰杰雪兰颖明子伊岚可倩妍仪萱妙琪美琦萌雯蕾柳惠雅晴宜芬芳苗如媛婉薇露"""

def generate_username():
    """
    随机生成姓名
    :param count:
    :return:
    """
    # 随机选择姓氏和名字
    surname = random.choice(SURNAME_LIST)
    given_name = random.choice(GIVENNAME_LIST)
    return "测"+surname+given_name

def generate_mobile():
    """
    随机生成手机号
    :return:
    """
    prefix = random.choice(["134","135","136","137","138","139","150","151","152","157","158","159","182","183","184","187","188","178","130","131","132","155","156","185","186","176","133","153","180","181","189","177"])
    digits = random.sample("123456789",8)#随机生成后10位数字
    return prefix + ''.join(digits)