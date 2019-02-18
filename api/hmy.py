import datetime
import json
import random
import time

from jpype import *
import jpype

import readConfig
from api import getSecureKey

import smtplib
import smtplib
from email.mime.text import MIMEText
from email.header import Header


# mail_title = '有陌生人来访！'
# mail_body = '请查看附件图片'
#
# # 创建一个实例
# message = MIMEText(mail_body, 'plain', 'utf-8')  # 邮件正文
# # (plain表示mail_body的内容直接显示，也可以用text，则mail_body的内容在正文中以文本的形式显示，需要下载）
# message['From'] = 'panjingjing'  # 邮件上显示的发件人
# message['To'] = 'yaozheng@ydfinance.com.cn'  # 邮件上显示的收件人
# message['Subject'] = Header(mail_title, 'utf-8')  # 邮件主题
#
# smtp = smtplib.SMTP()
# smtp.connect('mail.ydfinance.com.cn','25')
# print("打印日志")
#
#
# print('登录')
# smtp.login('panjingjing@ydfinance.com.cn', 'jing@8544606')
# print('登陆成功')
# smtp.sendmail( 'panjingjing@ydfinance.com.cn','yaozheng@ydfinance.com.cn',  message.as_string())
# smtp.quit()
# jvmPath = jpype.get_default_jvm_path()
# jpype.startJVM(jvmPath,"-Djava.class.path=D:\\utils\\out\\artifacts\\utils_jar\\utils.jar")
# # jpype.java.lang.System.out.println("hello World")
# javaClass = jpype.JClass('yongda.util.ParamSecurityUtil')
# # javaClass = javaClass()
# print(javaClass)
# javaClass = jPachge('yongda.util').ParamSecurityUtil
#
params={"attachInfo": '{\"attachAuditInfoVO\":{\"address\":\"杭州\",\"bankCardNo\":\"'+"6228480329403702666"+'\",\"homeBuildArea\":\"122.00\",\"homeCaseArea\":\"120.00\",\"homeCaseInstance\":\"民用\",\"houseProperty\":\"自住\"},\"consumeList\":[{\"imageUrl\":\"http://img03.tooopen.com/uploadfile/downs/images/20110714/sy_20110714135215645030.jpg\"},{\"imageUrl\":\"http://pic30.photophoto.cn/20140302/0035035834818295_b.jpg\"}],\"creditList\":[{\"$ref\":\"$.consumeList[0]\"},{\"$ref\": \"$.consumeList[1]\"}],\"houseList\":[{\"$ref\":\"$.consumeList[0]\"},{\"$ref\":\"$.consumeList[1]\"}],\"idList\":[{\"$ref\":\"$.consumeList[0]\"},{\"$ref\":\"$.consumeList[1]\"}]}',}
params.update(bankAccountName= "曹远超")
params.update(bankAccountNo="6228480329403702666")
params.update(bankBranch= "湖墅南路支行")
params.update(bankCityName= "杭州市")
params.update(bankId= "ABC")
params.update(bankProvinceName= "浙江省")
params.update(childMerchantId= "37")
params.update(contractName= "12345678")
params.update(contractNo= "399786478163996672")
params.update(contractParams= {})
params.update(contractPath= "http://172.16.10.40:8080/tosignserver/action/record/original/1023854133544747008")
params.update(deviceId= "3164itygrtuwytuygeugruyew")
params.update(externalOrderId= "399786478163996672")
params.update(externalOutPaymentNo= "123")
params.update(externalUserId="100001434444")
params.update(ip= "192.168.100.100")
params.update(memo= "备注")
params.update(merchantId= 36)
params.update(money= 12000)
params.update(notifyUrl= "http://ydtest002:35000/live/daStage/notifyAction")
params.update(outsideOverdueRate= 5.0)
params.update(platformName="好美意")
params.update(productId=19)
params.update(reason= "借钱")
params.update(repaymentMode= 1)
params.update(source= "app")
# params['bankAccountName'] = '曹远超'
# params['bankAccountNo'] = '6228480329403702666'
# params['bankBranch'] = '湖墅南路支行'
# params['bankCityName'] = '杭州市'
# params['bankId'] = 'ABC'
# params['bankProvinceName'] = '浙江省'
# params['childMerchantId'] = '37'
# params['bankAccountNo'] = '37'
# params['contractName'] = '12345678'
# params['contractNo'] = '399786478163996672'
# params['contractParams'] = {}
# params['contractPath'] = 'http://ydtest002:35000/live/daStage/notifyAction'
# params['outsideOverdueRate'] = 5.0
# params['platformName'] = '好美意'
# params['productId'] = 19
# params['reason'] = '借钱'
# params['repaymentMode'] = 1
# params['source'] = 'app'
#
#
#
stageList =  [{
		"amount": 2000,
		"discountAmount": 0,
		"interestFee": 200,
		"repayDate": "2018-12-25",
		"stage": 1
	}, {
		"amount": 2000,
		"discountAmount": 0,
		"interestFee": 200,
		"repayDate": "2018-12-25",
		"stage": 2
	}, {
		"amount": 2000,
		"discountAmount": 0,
		"interestFee": 200,
		"repayDate": "2018-12-25",
		"stage": 3
	}, {
		"amount": 2000,
		"discountAmount": 0,
		"interestFee": 200,
		"repayDate": "2018-12-25",
		"stage": 4
	}, {
		"amount": 2000,
		"discountAmount": 0,
		"interestFee": 200,
		"repayDate": "2018-12-25",
		"stage": 5
	}, {
		"amount": 2000,
		"discountAmount": 0,
		"interestFee": 200,
		"repayDate": "2018-12-25",
		"stage": 6
	}]
params.update(stageList= stageList)
params.update(stageType= "month")
params.update(stages= 6)
params.update(telphone="13675870972")

stageList1 =  [{
	  "stage": 1,
      "interestFeeAmount": 1100,
      "discountAmount": 0
	},
	{
	  "stage": 2,
	  "interestFeeAmount": 500,
	  "discountAmount": 0
	},
    {
	  "stage": 3,
      "interestFeeAmount": 500,
      "discountAmount": 0
	},
    {
	  "stage": 4,
      "interestFeeAmount": 500,
      "discountAmount": 0
	},
    {
	  "stage": 5,
      "interestFeeAmount": 500,
      "discountAmount": 0
	},
    {
	  "stage": 6,
      "interestFeeAmount": 500,
      "discountAmount": 0
	}
]

#data1 = {"merchantId":"36","accountDate":"1546531200000","tradeType":"1"}
# data = {"merchantId": "30","paymentCode":"1233333","loanId": "412353045544953856"}
# data.update(stageList1= stageList1)
# params['stageList'] = stageList
# params['stageType'] = 'month'
# params['stages'] = 6
# params['telphone'] = '13675870972'
#
#
#
#
# jsonString = {"attachInfo":"{\"attachAuditInfoVO\":{\"address\":\"杭州\",\"bankCardNo\":\"6228480329403702676\",\"homeBuildArea\":\"122.00\",\"homeCaseArea\":\"120.00\",\"homeCaseInstance\":\"民用\",\"houseProperty\":\"自住\"},\"consumeList\":[{\"imageUrl\":\"http://img03.tooopen.com/uploadfile/downs/images/20110714/sy_20110714135215645030.jpg\"},{\"imageUrl\":\"http://pic30.photophoto.cn/20140302/0035035834818295_b.jpg\"}],\"houseList\":[{\"$ref\":\"$.consumeList[0]\"},{\"$ref\":\"$.consumeList[1]\"}],\"idList\":[{\"$ref\":\"$.consumeList[0]\"},{\"$ref\":\"$.consumeList[1]\"}]}","bankAccountName":"曹远超","bankAccountNo":"6228480329403702666","bankBranch":"湖墅南路支行","bankCityName":"杭州市","bankId":"ABC","bankProvinceName":"浙江省","childMerchantId":"37","contractName":"12345678","contractNo":"399786478163996672","contractParams":{},"contractPath":"http://172.16.10.40:8080/tosignserver/action/record/original/1023854133544747008","deviceId":"3164itygrtuwytuygeugruyew","externalOrderId":"399786478163996672","externalOutPaymentNo":"123","externalUserId":"100001434444","ip":"192.168.100.100","memo":"备注","merchantId":36,"money":12000,"notifyUrl":"http://ydtest002:35000/live/daStage/notifyAction","outsideOverdueRate":5.0,"platformName":"好美意","productId":19,"reason":"借钱","repaymentMode":1,"source":"app","stageList":[{"amount":2000,"discountAmount":0,"interestFee":200,"repayDate":"2018-12-25","stage":1},{"amount":2000,"discountAmount":0,"interestFee":200,"repayDate":"2018-12-25","stage":2},{"amount":2000,"discountAmount":0,"interestFee":200,"repayDate":"2018-12-25","stage":3},{"amount":2000,"discountAmount":0,"interestFee":200,"repayDate":"2018-12-25","stage":4},{"amount":2000,"discountAmount":0,"interestFee":200,"repayDate":"2018-12-25","stage":5},{"amount":2000,"discountAmount":0,"interestFee":200,"repayDate":"2018-12-25","stage":6}],"stageType":"month","stages":6,"telphone":"13675870972"}
#data1 = json.JSONEncoder().encode(data)
#data = json.loads(params, object_hook=getSecureKey.JSONObject)
#print(data)
# string = '12345'
# localReadConfig = readConfig.ReadConfig()
# publicKey = localReadConfig.get_Secure("public_key")
# secureKey = localReadConfig.get_Secure("secret_key")
# secure = getSecureKey.getParamSecure(data, publicKey, secureKey)
# print(secure)

#getSecureKey.getSpzxMain("411270791095773184")
# print(HanLP().getMD5(string))
# print(javaClass.add(1,2))
# jpype.shutdownJVM()
# id = ''.join(str(i) for i in random.sample(range(0,9),8))
# money=12000
# stages=6
# stageList = [{"amount": money/stages,
#             "discountAmount": 0,
#             "interestFee": money/stages/10,
#             "repayDate": time.strftime('%Y-%m-%d',time.localtime(time.time())),
#             "stage": i} for i in range(1,stages)]
# print(stageList)
# stageList = [1].append( i for i in range(1,stages))
# contractNo =  ''.join(str(i) for i in random.sample(range(0,9),9))+''.join(str(i) for i in random.sample(range(0,9),9))

# print(contractNo)
# D52D34A7137F1587DEBD0414977303E8


