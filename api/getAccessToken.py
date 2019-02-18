import json
from api import sendSMSCode
from api import dbManager
import readConfig as readConfig
from common import configHttp as ConfigHttp
from common.configDB import MyDB


myDB = MyDB()

localReadConfig = readConfig.ReadConfig()
configHttp = ConfigHttp.ConfigHttp()
url = 'app/User/login'
configHttp.set_url(url)
header={"Content-Type": localReadConfig.get_headers("Content-Type")}
configHttp.set_header(header)
def getAccessToken():
    loginType = '1'
    phoneNumber = '15726940779'
    sendSMSCode.send_Login_Code(phoneNumber)
    verifyCode = dbManager.getVerifyCode(phoneNumber)
    data = {"loginType":loginType,"phoneNumber":phoneNumber,'verifyCode':verifyCode}
    data = json.JSONEncoder().encode(data)
    configHttp.set_data(data)

    return_json = configHttp.post()
    info = return_json.json()
    accessToken = info['data']['accessToken']
    memberId = info['data']['userInfo']['memberId']
    localReadConfig.set_headers('accessToken',accessToken)
    # if return_json.status_code!=200 or info['success'] is None or info['success'] != True:
    #     print("短信发送失败,原因:"+info['resultMessage'])
    #     return
    # print(info['resultMessage'])
    return {'accessToken':accessToken,'memberId':memberId}

# 登录并获取token和memberId
def loginToGetAccessToken(phoneNumber):
    loginType = '1'
    # phoneNumber = '15726940779'
    sendSMSCode.send_Login_Code(phoneNumber)
    verifyCode = dbManager.getVerifyCode(phoneNumber)
    data = {"loginType":loginType,"phoneNumber":phoneNumber,'verifyCode':verifyCode}
    data = json.JSONEncoder().encode(data)
    configHttp.set_data(data)

    return_json = configHttp.post()
    info = return_json.json()
    if info is not None:
        if info['data'] is not None:
            accessToken = info['data']['accessToken']
            memberId = info['data']['userInfo']['memberId']
            localReadConfig.set_headers('accessToken',accessToken)
    # if return_json.status_code!=200 or info['success'] is None or info['success'] != True:
    #     print("短信发送失败,原因:"+info['resultMessage'])
    #     return
    # print(info['resultMessage'])
            return {'accessToken':accessToken,'memberId':memberId}

# 获取token和memberId
def getToken(phoneNumber):
    q = myDB.executeSQL("dccj_20161022","t_sys_user_login","getToken",phoneNumber)
    result=q.fetchone()
    if result is not None:
        accessToken=result[0]
        memberId=result[1]
        return {'accessToken':accessToken,'memberId':memberId}
    else:
        return {'msg':'该手机号未登录'}
    myDB.closeDB()


if __name__ == '__main__':
    print(loginToGetAccessToken('15726940779'))
