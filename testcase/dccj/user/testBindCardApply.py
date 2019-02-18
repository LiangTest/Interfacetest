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

add_xls = common.get_xls("loan.xlsx", "bindCardApply")  #读取测试用例
localReadConfig = readConfig.ReadConfig()
configHttp = ConfigHttp.ConfigHttp()
info = {}


@paramunittest.parametrized(*add_xls)  #@parameterized.expand装饰接受列表或可迭代的元组或param(...)
class TestBindCardApply(unittest.TestCase):
    def setParameters(self, case_name, method, bankAccountName,bankAccountNo,bankBranch,bankId,bankName,externalUserId,idNo,merchantId,mobile,productCode, resultCode, success):
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
        self.bankName = str(bankName)
        self.bankId = str(bankId)
        #self.idNo = str(idNo)
        if merchantId != None and merchantId !='':
            self.merchantId = str(int(merchantId))
        else:
            self.merchantId = None
        if idNo != None and idNo !='':
            self.idNo = str(idNo)
        else:
            self.idNo = None
        if externalUserId != None and externalUserId !='':
            self.externalUserId = str(externalUserId)
        else:
            self.externalUserId = None
        if mobile != None and mobile !='':
            self.mobile = int(mobile)
        else:
            self.mobile = None
        if productCode != None and productCode !='':
            self.productCode = int(productCode)
        else:
            self.productCode = None

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

    def testBindCardApply(self):
        """
        test body
        :return:
        """
        # set url
        #self.url = common.get_url_from_xml('getModuleList')  #从interfaceURL.xml文件中读取url
        self.url = 'user/bindCardApply'
        configHttp.set_url(self.url)
        print("第一步：设置url  "+self.url)
        header = {}
        configHttp.set_header(header)
        print("第二步：设置header(token等)")
        params = {"bankAccountName":self.bankAccountName,
		"bankAccountNo": self.bankAccountNo,
		"bankBranch": self.bankBranch,
		"bankId": self.bankId,
		"bankName": self.bankName,
		"idNo": self.idNo,
        "externalUserId": self.externalUserId,
		"ip": "192.168.100.100",
		"merchantId": self.merchantId,
		"mobile": self.mobile,
		"productCode": self.productCode}
        publicKey = localReadConfig.get_Secure("public_key")
        secret_key = localReadConfig.get_Secure("secret_key")
        secure = getSecureKey.getParamSecure(params, publicKey, secret_key)
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

        #第六步：写入bindserialno
        bindSerialNo = self.info["result"].get('bindSerialNo')
        localReadConfig.set_bindSerialNo("bindserial", str(bindSerialNo))
        print(str(datetime.datetime.now()) + "写入时间")
        print("第六步：写入bindserialno")

    def tearDown(self):
        """

        :return:
        """
        try:
            # self.log.build_case_line(self.case_name, str(self.return_json.status_code), str(self.info['result']),self.time)
            WeChatClient.sendmsg("DCCJ-绑卡验证用例","\nDCCJ-绑卡验证用例"+"\n用例名："+self.case_name+"\n响应时间(ms):"+str(self.time))
        except KeyError:
            # self.log.build_case_line(self.case_name, str(self.return_json.status_code), str(self.info['message']),self.time)
            WeChatClient.sendmsg("DCCJ-绑卡验证用例","\nDCCJ-绑卡验证用例"+"\n用例名："+self.case_name+"\n响应时间(ms):"+str(self.time))
        print("测试结束，输出log完结\n\n")

    def checkResult(self):
        """
        check test result
        :return:
        """
        self.info = self.return_json.json()

        common.show_return_msg(self.return_json)  # 显示返回信息
        self.assertEqual(self.return_json.status_code, 200)
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
