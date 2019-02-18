import unittest
import json
import datetime
import paramunittest
import readConfig as readConfig
from common.log import MyLog as Log
from common import common
from common import configHttp as ConfigHttp


localReadConfig = readConfig.ReadConfig()
configHttp = ConfigHttp.ConfigHttp()
url = 'app/User/checkCode'
configHttp.set_url(url)
header={"Content-Type": localReadConfig.get_headers("Content-Type")}
configHttp.set_header(header)
def Check_Register_Code(phone,code):

    data = {"phoneNumber":phone,"code":code,"type":1}
    data = json.JSONEncoder().encode(data)
    configHttp.set_data(data)
    print(configHttp.url)
    print(configHttp.data)

    return_json = configHttp.post()
    info = return_json.json()
    print(info)
    # if return_json.status_code!=200 or info['success'] is None:
    #     print("验证码校验失败,原因:"+info['resultMessage'])
    #     return
    # print(info['resultMessage'])
    return info['data']['token']

def Check_Login_Code(phone,code):

    data = {"phoneNumber":phone,"code":code,"type":0}
    data = json.JSONEncoder().encode(data)
    configHttp.set_data(data)
    print(configHttp.url)
    print(configHttp.data)

    return_json = configHttp.post()
    info = return_json.json()
    # if return_json.status_code!=200 or info['success'] is None:
    #     print("验证码校验失败,原因:"+info['resultMessage'])
    #     return
    # print(info['resultMessage'])
    return info['data']['token']

def Check_SetLoginPSW_Code(phone,code):

    data = {"phoneNumber":phone,"code":code,"type":3}
    data = json.JSONEncoder().encode(data)
    configHttp.set_data(data)
    print(configHttp.url)
    print(configHttp.data)

    return_json = configHttp.post()
    info = return_json.json()
    # if return_json.status_code!=200 or info['success'] is None:
    #     print("验证码校验失败,原因:"+info['resultMessage'])
    #     return
    # print(info['resultMessage'])
    return info['data']['token']

def Check_SetPayPSW_Code(phone,code):

    data = {"phoneNumber":phone,"code":code,"type":4}
    data = json.JSONEncoder().encode(data)
    configHttp.set_data(data)
    print(configHttp.url)
    print(configHttp.data)

    return_json = configHttp.post()
    info = return_json.json()
    # if return_json.status_code!=200 or info['success'] is None:
    #     print("验证码校验失败,原因:"+info['resultMessage'])
    #     return
    # print(info['resultMessage'])
    return info['data']['token']


if __name__ == '__main__':
    Check_Login_Code('15726940779','989946')