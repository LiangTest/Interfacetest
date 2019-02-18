import json
import readConfig as readConfig
from common import configHttp as ConfigHttp
from api import dbManager


localReadConfig = readConfig.ReadConfig()
configHttp = ConfigHttp.ConfigHttp()
url = 'app/User/verifyCode'
configHttp.set_url(url)
header={"Content-Type": localReadConfig.get_headers("Content-Type")}
configHttp.set_header(header)
def send_Register_Code(phone):

    data = {"type":1,"phoneNumber":phone}
    data = json.JSONEncoder().encode(data)
    configHttp.set_data(data)

    return_json = configHttp.post()
    info = return_json.json()
    print(info)
    return dbManager.getVerifyCode(phone)
    # if return_json.status_code!=200 or info['success'] is None or info['success'] != True:
    #     print("短信发送失败,原因:"+info['resultMessage'])
    #     return
    # print(info['resultMessage'])

def send_Login_Code(phone):

    data = {"type":0,"phoneNumber":phone}
    data = json.JSONEncoder().encode(data)
    configHttp.set_data(data)

    return_json = configHttp.post()
    info = return_json.json()
    print(info)
    return dbManager.getVerifyCode(phone)
    # if return_json.status_code!=200 or info['success'] is None or info['success'] != True:
    #     print("短信发送失败,原因:"+info['resultMessage'])
    #     return
    # print(info['message'])


def send_Set_LoginPSW_Code(phone):

    data = {"type":3,"phoneNumber":phone}
    data = json.JSONEncoder().encode(data)
    configHttp.set_data(data)

    return_json = configHttp.post()
    info = return_json.json()
    print(info)
    return dbManager.getVerifyCode(phone)
    # if return_json.status_code!=200 or info['success'] is None or info['success'] != True:
    #     print("短信发送失败,原因:"+info['resultMessage'])
    #     return
    # print(info['message'])


def send_Set_PayPSW_Code(phone):

    data = {"type":4,"phoneNumber":phone}
    data = json.JSONEncoder().encode(data)
    configHttp.set_data(data)

    return_json = configHttp.post()
    info = return_json.json()
    return dbManager.getVerifyCode(phone)
    # if return_json.status_code!=200 or info['success'] is None or info['success'] != True:
    #     print("短信发送失败,原因:"+info['resultMessage'])
    #     return
    # print(info['message'])


if __name__ == '__main__':
    send_Register_Code('18458104743')