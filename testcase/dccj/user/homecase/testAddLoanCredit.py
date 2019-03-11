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

add_xls = common.get_xls("loan.xlsx", "addloanaudit")  #读取测试用例
localReadConfig = readConfig.ReadConfig()
configHttp = ConfigHttp.ConfigHttp()
info ={}

@paramunittest.parametrized(*add_xls)  #@parameterized.expand装饰接受列表或可迭代的元组或param(...)
class TestQueryCredit(unittest.TestCase):
    def setParameters(self,case_name, method, merchantId, externalUserId, productId,loanId, childMerchantId, resultCode, success):
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
        if merchantId != None and merchantId !='':
            self.merchantId = str(int(merchantId))
        else:
            self.merchantId = None

        if externalUserId != None and externalUserId !='':
            self.externalUserId = str(int(externalUserId))
        else:
            self.externalUserId = None

        if productId != None and productId !='':
            self.productId = str(int(productId))
        else:
            self.productId = None

        if loanId != None and loanId !='':
            self.loanId = str(int(loanId))
        else:
            self.loanId = None

        if childMerchantId != None and childMerchantId != '':
            self.childMerchantId = str(int(childMerchantId))
        else:
            self.childMerchantId = None

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
        self.log = Log.get_log()  # 实例化日志
        self.logger = self.log.get_logger()
        print(self.case_name + "测试开始前准备")

    def testQueryCredit(self):
        """
        test body
        :return:
            """
        # set url
        # self.url = common.get_url_from_xml('getModuleList')  #从interfaceURL.xml文件中读取url
        self.url = 'loan/homeCase/addLoanAuditData'
        configHttp.set_url(self.url)
        print("第一步：设置url  " + self.url)
        header = {}
        configHttp.set_header(header)
        print("第二步：设置header(token等)")
        params = {
            "attachInfo": "{\"consumeList\":[{\"imageUrl\":\"http://qimg.hxnews.com/2019/0130/1548847547452.jpg\"},{\"imageUrl\":\"http://pic30.photophoto.cn/20140302/0035035834818295_b.jpg\"}],\"creditList\":[{\"$ref\":\"$.consumeList[0]\"},{\"$ref\":\"$.consumeList[1]\"}],\"houseList\":[{\"$ref\":\"$.consumeList[0]\"},{\"$ref\":\"$.consumeList[1]\"}],\"idList\":[{\"$ref\":\"$.consumeList[0]\"},{\"$ref\":\"$.consumeList[1]\"}]}",
        }
        params.update(merchantId=self.merchantId)
        params.update(externalUserId=self.externalUserId)
        params.update(productId=self.productId)
        params.update(loanId=self.loanId)
        params.update(childMerchantId=self.childMerchantId)

        publicKey = localReadConfig.get_Secure("public_key")
        secret_key = localReadConfig.get_Secure("secret_key")
        secure = getSecureKey.getParamSecure(params, publicKey, secret_key)
        data = {'params': params}
        data.update(publicKey=publicKey)
        data.update(secureKey=secure)

        data = json.JSONEncoder().encode(data)
        configHttp.set_data(data)
        print("第三步：设置发送请求的参数")

        # test interface
        self.time_s = datetime.datetime.now()
        self.return_json = configHttp.post()
        self.time_e = datetime.datetime.now()
        self.time = (self.time_e - self.time_s).total_seconds() * 1000
        # self.time = self.time_e - self.time_s
        method = str(self.return_json.request)[
                 int(str(self.return_json.request).find('[')) + 1:int(str(self.return_json.request).find(']'))]
        print("第四步：发送请求\n\t\t请求方法：" + method + "\n\t\t响应时间(ms)：" + str(self.time))
        # check result
        self.checkResult()
        print("第五步：检查结果")

    def tearDown(self):
        """
        :return:
        """
        try:
            # self.log.build_case_line(self.case_name, str(self.return_json.status_code), str(self.info['result']),self.time)
            WeChatClient.sendmsg("DCCJ-还款用例",
                                 "\nDCCJ-还款用例" + "\n用例名：" + self.case_name + "\n响应时间(ms):" + str(self.time))
        except KeyError:
            # self.log.build_case_line(self.case_name, str(self.return_json.status_code), str(self.info['message']),self.time)
            WeChatClient.sendmsg("DCCJ-还款用例",
                                 "\nDCCJ-还款用例" + "\n用例名：" + self.case_name + "\n响应时间(ms):" + str(self.time))
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