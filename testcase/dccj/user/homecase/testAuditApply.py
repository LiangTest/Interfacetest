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

add_xls = common.get_xls("loan.xlsx", "auditApply")  #读取测试用例
localReadConfig = readConfig.ReadConfig()
configHttp = ConfigHttp.ConfigHttp()
info = {}


@paramunittest.parametrized(*add_xls)  #@parameterized.expand装饰接受列表或可迭代的元组或param(...)
class TestAuditApply(unittest.TestCase):
    def setParameters(self, case_name, method, birthday,externalUserId,merchantId,identifyNo,phone,realName, resultCode, success):
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
        self.birthday = str(birthday)
        if externalUserId != None and externalUserId !='':
            self.externalUserId = str(int(externalUserId))
        else:
            self.externalUserId = None
        if merchantId != None and merchantId !='':
            self.merchantId = str(int(merchantId))
        else:
            self.merchantId = None
        if phone != None and phone != '':
            self.phone = str(int(phone))
        else:
            self.phone = None
        self.identifyNo = str(identifyNo)[0:18]
        self.realName = realName
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

    def testAuditApply(self):
        """
        test body
        :return:
        """
        # set url
        #self.url = common.get_url_from_xml('getModuleList')  #从interfaceURL.xml文件中读取url
        self.url = 'user/homeCase/auditApply'    #接口地址
        configHttp.set_url(self.url)
        print("第一步：设置url  "+self.url)
        header = {}
        configHttp.set_header(header)
        print("第二步：设置header(token等)")
        params = {
            "birthday":self.birthday}
        params.update(business="信息传输、计算机服务和软件业")
        params.update(businessCode= "G")
        params.update(cityCode="330100")
        params.update(cityName="杭州市")
        params.update(contacts= [{
            "contactName": "妈妈",
            "contactPhone": "13333333333",
            "relations": 1
        }, {
            "contactName": "媳妇",
            "contactPhone": "13555555555",
            "relations": 2
        }])
        params.update(degreeCode= "4")
        params.update(deviceId="uihwewkgeuiy23tiueyqiwt4j")
        params.update(district="下城区71-8")
        params.update(duty= "一般管理")
        params.update(dutyCode= "2")
        params.update(eduCode= "02")
        params.update(externalUserId= self.externalUserId)
        params.update(merchantId= self.merchantId)
        params.update(highestDegree="学士")
        params.update(highestEdu="大学本科")
        params.update(idAddress= "杭州市余杭区闲林街道东市街岸上蓝山")
        params.update(idCardFront="http://www.baidu.com/idCardFront.jpg")
        params.update(idCardReverse="http://www.baidu.com/idCardReverse.jpg")
        params.update(identifyNo=self.identifyNo)
        params.update(ip="192.168.100.100")
        params.update(liveStatus="自建")
        params.update(liveStatusCode= "10")
        params.update(mail="123@qq.com")
        params.update(notifyUrl= "http://ydtest004:35000/live/daStage/notifyAction")
        params.update(phone= self.phone)
        params.update(postCode="5000")
        params.update(productCode=["18", "19", "20"])
        params.update(profession="1-医生")
        params.update(professionCode="01")
        params.update(marryStatus= "已婚")
        params.update(provinceCode= "330000")
        params.update(provinceName="浙江省")
        params.update(rangeCode= "330103")
        params.update(rangeName= "下城区")
        params.update(realName=self.realName)
        params.update(sex= "m")
        params.update(source="app")
        params.update(title= "中级")
        params.update(titleCode= "2")
        params.update(unitName="浙江钱塘江水利建筑工程公司")
        publicKey = localReadConfig.get_Secure("public_key")
        secureKey = localReadConfig.get_Secure("secret_key")
        secure = getSecureKey.getParamSecure(params, publicKey, secureKey)
        data = {'params': params}
        data.update(publicKey=publicKey)
        data.update(secureKey=secure)

        # set params
        # data = {"interfaceInfo":{"agent": "android","fingerPrint": "UYGIGVYUGHBNUYFYTGINOK","requestUUID": "6c268717-be27-4e6e-ba90-b27b6f5211fe","version": "1.0.0","latitude": 0,"longitude": 0,"deviceId": "d70a659c-31c3-403f-9160-c4476ea9d5f4","deviceModel": "xiaomi"},"type":1}

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
        time.sleep(5)
        # check result
        self.checkResult()
        print("第五步：检查结果")

    def tearDown(self):
        """

        :return:
        """
        try:
            # self.log.build_case_line(self.case_name, str(self.return_json.status_code), str(self.info['result']),self.time)
            WeChatClient.sendmsg("DCCJ-好美意授信用例","\nDCCJ-好美意授信用例"+"\n用例名："+self.case_name+"\n响应时间(ms):"+str(self.time))
        except KeyError:
            # self.log.build_case_line(self.case_name, str(self.return_json.status_code), str(self.info['message']),self.time)
            WeChatClient.sendmsg("DCCJ-好美意授信用例","\nDCCJ-好美意授信用例"+"\n用例名："+self.case_name+"\n响应时间(ms):"+str(self.time))
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
            self.assertEqual(self.info['success'], self.success)
        except KeyError:
            pass
        try:
            self.assertEqual(self.info['code'], self.code)
        except KeyError:
            pass
