import requests
import re
from urllib.parse import urlencode

def getLoginMsg():
    '''
    登录时获取参数函数
    '''
    paramsdic = {}          #参数字典
    url = 'http://192.168.2.135'
    r = requests.get(url=url)
    try:
        pattern = "href='(\S+)'"
        href = re.search(pattern=pattern,string=r.text).group(1)
    except TypeError:
        print('你已在线')
    destination = href.split('?')[0]        #跳转目标url
    params = href.split('?')[1]             #params字符串
    for param in params.split('&'):
        paramlist = param.split('=')
        paramsdic[paramlist[0]] = paramlist[1]
    return destination,paramsdic
    
def login(userId,password):
    '''
    登录函数
    params:
    userId :学号
    password :密码
    '''
    url = 'http://192.168.2.135/eportal/InterFace.do?method=login'
    datadic = getLoginMsg()[1]
    params = {
        "method":"login"
    }
    data = {
        "userId":userId,
        "password":password,
        "service":"internet",
        "queryString":urlencode(datadic),
        "operatorPwd":"",
        "operatorUserId":"",
        "validcode":"",
        "passwordEncrypt":"false"
    }
    r = requests.post(url=url,params=params,data=data)
    if r.json()["result"] == "success":
        print("登录成功")
    else:
        print("登录失败")

def getLogoutMsg():
    '''
    获取退出时信息
    '''
    url = 'http://192.168.2.135/eportal/InterFace.do?method=getOnlineUserInfo'
    r = requests.get(url=url)
    try:
        return r.json()["userIndex"]
    except Exception:
        print('已下线')

def logout():
    '''
    下线函数
    '''
    url = 'http://192.168.2.135/eportal/InterFace.do?method=logout'
    try:
        data = {
            "userIndex":getLogoutMsg()
        }
        r = requests.post(url=url,data=data)
        r.encoding = 'utf-8'
        
        if r.json()["message"]=='下线成功！':
            print('成功下线')
        else:
            print('下线失败')
    except Exception:
        print('用户已经下线')