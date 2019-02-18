import random
import time
import unittest
import json
import datetime
import paramunittest
import readConfig as readConfig
from common.log import MyLog as Log
from common import common
from common import configHttp as ConfigHttp
from api import WeChatClient, getSecureKey

add_xls = common.get_xls("loan.xlsx", "add")  #读取测试用例
localReadConfig = readConfig.ReadConfig()
configHttp = ConfigHttp.ConfigHttp()

info = {}


@paramunittest.parametrized(*add_xls)  #@parameterized.expand装饰接受列表或可迭代的元组或param(...)
class TestAdd(unittest.TestCase):
    def setParameters(self, case_name, method, bankAccountName,bankAccountNo,bankBranch,bankCityName,bankId,bankProvinceName,childMerchantId,externalUserId,money,stages,telphone, resultCode, success):
        """
        set params
        :param case_name:
        :param method:
        :param type:
        :param result:
        :param resultCode:
        :param success:
        :return:
        """
        self.case_name = str(case_name)
        self.method = str(method)
        self.bankAccountName = str(bankAccountName)

        if bankAccountNo != None and bankAccountNo !='':
            self.bankAccountNo = str(int(bankAccountNo))
        else:
            self.bankAccountNo = None
        self.bankBranch = str(bankBranch)
        self.bankCityName = str(bankCityName)
        self.bankId = str(bankId)
        self.bankProvinceName = str(bankProvinceName)
        if childMerchantId != None and childMerchantId !='':
            self.childMerchantId = str(int(childMerchantId))
        else:
            self.childMerchantId = None
        if externalUserId != None and externalUserId !='':
            self.externalUserId = str(int(externalUserId))
        else:
            self.externalUserId = None
        if money != None and money !='':
            self.money = int(money)
        else:
            self.money = None
        if stages != None and stages !='':
            self.stages = int(stages)
        else:
            self.stages = None

        if telphone != None and telphone !='':
            self.telphone = str(int(telphone))
        else:
            self.telphone = None
        if resultCode != None and resultCode !='':
            self.resultCode = resultCode
        else:
            self.code = None
        if success != None and success != '':
            self.success = bool(success)
        else:
            self.success = None
        self.return_json = None
        self.info = None

    def description(self):
        """
        测试报告描述
        :return:
        """
        self.case_name

    def setUp(self):
        """

        :return:
        """
        self.log = Log.get_log()  #实例化日志
        self.logger = self.log.get_logger()
        print(self.case_name+"测试开始前准备")

    def testAdd(self):
        """
        test body
        :return:
        """
        # set url
        #self.url = common.get_url_from_xml('getModuleList')  #从interfaceURL.xml文件中读取url
        self.url = 'loan/add'
        configHttp.set_url(self.url)
        print("第一步：设置url  "+self.url)
        header = {}
        configHttp.set_header(header)
        print("第二步：设置header(token等)")
        params = {
            "attachInfo": '{\"attachAuditInfoVO\":{\"address\":\"杭州\",\"bankCardNo\":\"'+str(self.bankAccountNo)+'\",\"homeBuildArea\":\"122.00\",\"homeCaseArea\":\"120.00\",\"homeCaseInstance\":\"民用\",\"houseProperty\":\"自住\"},\"consumeList\":[{\"imageUrl\":\"http://picm.photophoto.cn/033/014/391/0143910002.jpg\"},{\"imageUrl\":\"http://pic30.photophoto.cn/20140302/0035035834818295_b.jpg\"}],\"creditList\":[{\"$ref\":\"$.consumeList[0]\"},{\"$ref\": \"$.consumeList[1]\"}],\"houseList\":[{\"$ref\":\"$.consumeList[0]\"},{\"$ref\":\"$.consumeList[1]\"}],\"idList\":[{\"$ref\":\"$.consumeList[0]\"},{\"$ref\":\"$.consumeList[1]\"}]}',}
        params.update(bankAccountName=self.bankAccountName)
        params.update(bankAccountNo=self.bankAccountNo)
        params.update(bankBranch=self.bankBranch)
        params.update(bankCityName=self.bankCityName)
        params.update(bankId=self.bankId)
        params.update(bankProvinceName=self.bankProvinceName)
        params.update(childMerchantId=self.childMerchantId)
        params.update(contractName="12345678")
        contractNo = ''.join(str(i) for i in random.sample(range(0,9),9))+''.join(str(i) for i in random.sample(range(0,9),9))
        params.update(contractNo=contractNo)
        params.update(contractParams={})
        params.update(contractPath="https://testapi.fadada.com:8443/api//getdocs.action?app_id=401572&timestamp=20181227183004&v=2.0&msg_digest=NkE3MDMzMzFBQTMyOEJFNDZEMTZDNzBFREQ4RDEwRDkzMUM2ODg5NA==&send_app_id=null&transaction_id=510245")
        params.update(deviceId="3164itygrtuwytuygeugruyew")
        params.update(externalOrderId=contractNo)
        params.update(externalOutPaymentNo="123")
        params.update(externalUserId=self.externalUserId)
        params.update(ip="192.168.100.100")
        params.update(memo="备注")
        params.update(merchantId=36)
        params.update(money=self.money)
        params.update(notifyUrl="http://ydtest002:35000/live/daStage/notifyAction")
        params.update(outsideOverdueRate=5.0)
        params.update(platformName="好美意")
        params.update(productId=18)
        params.update(reason="借钱")
        params.update(repaymentMode=1)
        params.update(source="app")
        stageList =[{"amount": self.money/self.stages,
            "discountAmount": 10000,
            "interestFee": self.money/self.stages/10,
            "repayDate": time.strftime('%Y-%m-%d',time.localtime(time.time())),
            "stage": i} for i in range(1,self.stages+1)]
        params.update(stageList=stageList)
        params.update(stageType="month")
        params.update(stages=self.stages)
        params.update(telphone=self.telphone)
        publicKey = localReadConfig.get_Secure("public_key")
        secret_key = localReadConfig.get_Secure("secret_key")
        secure = getSecureKey.getParamSecure(params,publicKey,secret_key)
        data = {'params':params}
        data.update(publicKey=publicKey)
        data.update(secureKey=secure)

        # set params
        #data = {"interfaceInfo":{"agent": "android","fingerPrint": "UYGIGVYUGHBNUYFYTGINOK","requestUUID": "6c268717-be27-4e6e-ba90-b27b6f5211fe","version": "1.0.0","latitude": 0,"longitude": 0,"deviceId": "d70a659c-31c3-403f-9160-c4476ea9d5f4","deviceModel": "xiaomi"},"type":1}

        # self.accessToken = getAccessToken.loginTonGetAccessToken(self.phon)
        data = json.JSONEncoder().encode(data)
        configHttp.set_data(data)
        print("第三步：设置发送请求的参数")

        # test interface
        self.time_s = datetime.datetime.now()
        self.return_json = configHttp.post()
        self.time_e  = datetime.datetime.now()
        self.time = (self.time_e - self.time_s).total_seconds()*1000
        #self.time = self.time_e - self.time_s
        method = str(self.return_json.request)[int(str(self.return_json.request).find('['))+1:int(str(self.return_json.request).find(']'))]
        print("第四步：发送请求\n\t\t请求方法："+method+"\n\t\t响应时间(ms)："+str(self.time))
        # check result
        self.checkResult()
        print("第五步：检查结果")

        #if self.assertEqual(self.info['success'],"true"):
        loan_id = self.info["result"]
        getSecureKey.getSpzxMain(loan_id)
        print("第六步：下单审核")

        #获取的loanid，写入配置文件
        localReadConfig.set_loan("loanid",loan_id)
        print(str(datetime.datetime.now()) + "写入时间")
        print("第七步：记录借款单")

    def tearDown(self):
        """

        :return:
        """
        try:
            WeChatClient.sendmsg("DCCJ-好美意下单用例","\nDCCJ-好美意下单用例"+"\n用例名："+self.case_name+"\n响应时间(ms):"+str(self.time))
        except KeyError:
            WeChatClient.sendmsg("DCCJ-好美意下单用例","\nDCCJ-好美意下单用例"+"\n用例名："+self.case_name+"\n响应时间(ms):"+str(self.time))
        print("测试结束，输出log完结\n\n")

    def checkResult(self):
        """
        check test result
        :return:
        """
        self.info = self.return_json.json()

        common.show_return_msg(self.return_json)  # 显示返回信息

        # if self.result == '0':
        #     email = common.get_value_from_return_json(self.info, 'member', 'email')
        #     self.assertEqual(self.info['code'], self.code)
        #     self.assertEqual(self.info['msg'], self.msg)
        #     self.assertEqual(email, self.email)
        #
        # if self.result == '1':
        #     self.assertEqual(self.info['code'], self.code)
        #     self.assertEqual(self.info['msg'], self.msg)
        self.assertEqual(self.return_json.status_code,200)
        try:
            if self.success != None and self.success != '':
                self.assertEqual(self.info['success'], self.success)
        except KeyError:
            pass
        try:
            if self.code != None and self.code != '':
                self.assertEqual(self.info['code'], self.code)
        except KeyError:
            pass
