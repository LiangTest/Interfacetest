import logging
from datetime import datetime
import threading
import os
import readConfig

localReadConfig = readConfig.ReadConfig()

class Log:
    def __init__(self):
        '''
        进行相关初始化操作
        '''
        global logPath , resultPath , proDir
        proDir = readConfig.proDir  #获取工程目录
        resultPath = os.path.join(proDir,"result")  #拼接resultPath
        #若文件不存在，则创建
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        logPath = os.path.join(resultPath,str(datetime.now().strftime("%Y%m%d%H%M%S")))  #日志文件存放在resultPath下，文件名为当前时间（年月日时分秒）
        #若文件不存在，则创建
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        self.logger = logging.getLogger()  #初始化logger对象
        self.logger.setLevel(logging.INFO)  #设置日志等级 共五个等级，从高到低：CRITICAL 严重错误信息、ERROR 错误信息、WARNING 警告信息、INFO 重要信息、DEBUG

        #定义handle
        handle = logging.FileHandler(os.path.join(logPath,"output.log"))
        #定义格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handle.setFormatter(formatter)
        self.logger.addHandler(handle)

    def get_logger(self):
        return self.logger

    def build_start_line(self,case_no):
        self.logger.info("--------"+case_no+"START--------")

    def build_end_line(self,case_no):
        self.logger.info("--------"+case_no+"END--------")

    def build_case_line(self,case_name,code,msg,time):
        self.logger.info("用例名："+case_name+"/code:"+code+"/msg:"+msg+"/响应时间(ms):"+str(time))

    def get_report_path(self):
        report_path = os.path.join(logPath,"report.html")
        return report_path

    def get_result_path(self):
        return logPath

    def write_result(self, result):
        result_path = os.path.join(logPath, "report.txt")
        fb = open(result_path, "wb")
        try:
            fb.write(result)
        except FileNotFoundError as ex:
            logger.error(str(ex))


class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():

        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()

        return MyLog.log

if __name__ == "__main__":
    log = MyLog.get_log()
    logger = log.get_logger()
    logger.debug("test debug")
    logger.info("test info")





