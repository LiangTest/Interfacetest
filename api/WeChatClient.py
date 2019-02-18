# pip3 install requests
import requests
import json
import readConfig
from common import configHttp
from model import wxTextMessage

rc = readConfig.ReadConfig()
ch = configHttp.ConfigHttp()
wtm = wxTextMessage.WXTextMessage()
def getWXToken():
    """获取微信全局接口的凭证(默认有效期俩个小时)"""
    grant_type=rc.get_WeChat("grant_type")
    appid = rc.get_WeChat("appID")
    secret  = rc.get_WeChat("appSecret")
    tokenURL = rc.get_WeChat("tokenURL")

    ret = requests.get(url=tokenURL+"?grant_type="+grant_type+"&appid="+appid+"&secret="+secret)
    return ret

def get_access_token():
    """
    获取微信全局接口的凭证(默认有效期俩个小时)
    如果不每天请求次数过多, 通过设置缓存即可
    """
    result = requests.get(
        url="https://api.weixin.qq.com/cgi-bin/token",
        params={
            "grant_type": "client_credential",
            "appid": "wx872e5e68a2f5a06e",
            "secret": "e4c5054250ef5bde9b1d09cf7c72d976",
        }
    ).json()

    if result.get("access_token"):
        access_token = result.get('access_token')
    else:
        access_token = None
    return access_token

def sendmsg(title,content):
    if rc.get_WeChat('on_off') == 'on':
        ret = getWXToken()
        access_token = ret.json()['access_token']
        SendMessageURL = rc.get_WeChat("SendMessageURL") + "?access_token=" + access_token

        body =   {
                "filter":{
                    "is_to_all":True,
                },
            "title":title,
                "text":{
                    "content":content
                },
                "msgtype":"text"
            }
        data=json.JSONEncoder().encode(body)
        # response = requests.post(
        #     url="https://api.weixin.qq.com/cgi-bin/message/custom/send",
        #     params={
        #         'access_token': access_token
        #     },
        #     data=bytes(json.dumps(body, ensure_ascii=False), encoding='utf-8')
        # )
        # 这里可根据回执code进行判定是否发送成功(也可以根据code根据错误信息)
        response = requests.post(url=rc.get_WeChat("SendMessageURL"), params={
                    'access_token': access_token
                }, data=bytes(json.dumps(body, ensure_ascii=False), encoding='utf-8'))
        result = response.json()
        print(result)



if __name__ == '__main__':
    #sendmsg('oVhWu04b5xLdeCA9TY5I5LciBUsI','发送消息内容')
    res = sendmsg("DCCJ-银行卡列表用例","\n返回结果:"+"\n响应时间4:" )