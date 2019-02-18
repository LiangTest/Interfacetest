from common import configHttp
import json
import datetime,time

#获取当前时间
dtime = datetime.datetime.now()
ans_time = int(time.mktime(dtime.timetuple()))
authorization='OAuth oauth_version="1.0", oauth_consumer_key="vIf3DAstj3ma5zq6", oauth_token="c98624b63fda854bc7f2a2a9ab14c3e", oauth_signature_method="HMAC-SHA1", oauth_timestamp='+str(ans_time)+', oauth_nonce="DD2A2B06-CBEC-4D8F-B67A-E2B3499D0C73", oauth_signature="iommi1I8EmFlF%2FJdkIAnSF9z4pY%3D"',
# print(authorization)
cookie={'gl':'75d520f9-33d9-47ae-b197-2af7ecc28cb4', 'tribenews-sid':'s%3AP0bF2mb6H_J2NwT4x0XvUHxQ7MYrZb6D.MRvnPoOn%2FZQaVTUv5mUmoeWlL2qBwynVgGYenc7LSEk'}
url = 'https://www.yunzhijia.com/openaccess/lightapp/getCsPubByAppid'
header={'content-type':'application/x-www-form-urlencoded',
        'accept':'*/*',
        'accept-language':'zh-CN',
        'accept-encoding':'br, gzip, deflate',
        'x-request-id':'04BE7A99-5649-4D02-A3F5-72815A9EA3B9',
        'user-agent':'10200/10.1.4;iOS 12.1;Apple;iPhone9,2;102;deviceId:37a918b5-6ef1-4150-9c81-b6f3e51d3daa;deviceName:Z%20%E7%9A%84%20iPhone;clientId:10200;os:iOS 12.1;brand:Apple;model:iPhone9,2;lang:zh-CN;fontNum:0',
        'opentoken':'9d7a8099bed96a5ca042aa6bdafcbe'}
header.update({'authorization':str(authorization)})

data = {'bssid':'ac:7e:8a:68:b4:8f',
'configId':'5bfba8afe4b0034e0ff726dc_4',
'lat':'30.32681396484375',
'lng':'120.1810400390625',
'networkId':'573d1c09e4b010f1433ba518',
'photoIds':'',
'ssid':'YongDa',
'userId':'5bfdfd2ae4b0ef521f7ce37b'}
data = json.JSONEncoder().encode(data)
ch = configHttp.ConfigHttp()
ch.set_fullurl(url)
ch.set_header(header)
ch.set_cookies(cookie)
ch.set_data(data)

res = ch.post()
print(res.content)








