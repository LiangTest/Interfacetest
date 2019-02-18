import os
import unittest
from common.log  import MyLog as Log
import readConfig as readConfig
#import common.HTMLTestRunner as HTMLTestRunner
from HTMLTestRunner import HTMLTestRunner_PY3 as HTMLTestRunner
from common.configEmail import MyEmail
from api import WeChatClient


localReadConfig = readConfig.ReadConfig()


class AllTest:
    def __init__(self):
        global log, logger, resultPath, on_off
        log = Log.get_log()
        logger = log.get_logger()
        resultPath = log.get_report_path()
        on_off = localReadConfig.get_Email("on_off")
        self.caseListFile = os.path.join(readConfig.proDir, "caselist.txt")
        self.caseFile = os.path.join(readConfig.proDir, "testcase/dccj")
        # self.caseFile = None
        self.caseList = []
        self.email = MyEmail.get_email()

    def set_case_list(self):
        """
        从caselist.txt文件中读取需要执行的case名称
        :return:
        """
        fb = open(self.caseListFile)  #打开caseList文件
        for value in fb.readlines():  #读值
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))  #将caseList文件中测试用例放入caseList
        fb.close()  #关闭caseList文件

    def set_case_suite(self):
        """
        set case suite
        :return:
        """
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []

        #将caseList中测试用例添加测试集
        for case in self.caseList:
            case_name = case.split("/")[-1]
            print(case_name+".py")
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            #discover._tests=discover._tests[1:-1]
            suite_module.append(discover)

        if len(suite_module) > 0:

            for suite in suite_module:
                for test_name in suite:
                        test_suite.addTest(test_name)
        else:
            return None

        return test_suite

    def run(self):
        """
        run test
        :return:
        """
        try:
            suit = self.set_case_suite()
            if suit is not None:
                logger.info("********TEST START********")
                fp = open(resultPath, 'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
                res=runner.run(suit)
                WeChatClient.sendmsg("测试结果","接口测试概述"+"\n成功数"+str(res.success_count)+"\n失败数"+str(res.failure_count)+"\n错误数"+str(res.error_count))

            else:
                logger.info("Have no case to test.")
        except Exception as ex:
            logger.error(str(ex))
        finally:
            logger.info("*********TEST END*********")
            fp.close()
            # send test report by email
            if on_off == 'on':
                self.email.send_email()
            elif on_off == 'off':
                logger.info("Doesn't send report email to developer.")
            else:
                logger.info("Unknow state.")


if __name__ == '__main__':
    obj = AllTest()
    obj.run()
