import urllib
import json
import hashlib
import requests
import readConfig as readConfig
from common.log import MyLog as Log

localReadConfig = readConfig.ReadConfig()

class ConfigHttp:
    '''
    进行相关初始化
    '''
    def __init__(self):
        global scheme, host, port, timeout
        scheme = localReadConfig.get_http("scheme")
        host = localReadConfig.get_http("baseurl")
        port = localReadConfig.get_http("port")
        timeout = localReadConfig.get_http("timeout")
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.headers = {}
        self.params = {}
        self.cookies={}
        self.data = {}
        self.url = None
        self.files = {}
        self.state = 0

    #设置请求的url
    def set_url(self,url):
        self.url = scheme+"://"+host+":"+port+"/"+url  #协议://主机号+url

    # 设置请求的url
    def set_fullurl(self, url):
        self.url = url  # 协议://主机号+url

    # shezhi
    def set_url_intact(self,url):
        self.url = scheme+"://"+'192.168.130.193:10100/cashier/'+url  #协议://主机号+url

    #设置请求头
    def set_header(self,header):
        self.headers=header

    #设置Get请求的params
    def set_params(self, param):
        self.params = param

    #设置cookie
    def set_cookies(self,cookies):
        self.cookies= cookies

    #设置post请求的data
    def set_data(self, data):
        self.data = data

    #设置上传文件
    def set_files(self,filename):
        if not filename.strip():  #str.strip() 去除字符串头和尾的空格，以及把位于头尾的\n \t之类给删掉
            file_path = "../testFile/img/' + filename"  #文件地址
        self.files = {'file': open(file_path, 'rb')}  #文件字典

        if filename.strip() == "" or filename is None:
            self.state = 1  #若文件名为空，则状态码置为1

    #定义请求的get方法
    def get(self):
        try:
            response = requests.get(self.url, headers=self.headers, params=self.params, timeout=float(timeout))
            print(self.params)
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    #定义请求的post方法
    def post(self):
        """
        defined post method
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, cookies=self.cookies, data=self.data, timeout=float(timeout))
            print(self.url)
            # print(self.headers)
            print(self.data)
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    #定义请求的post方法,带签名
    def postWithSign(self):
        sign = ''
        if self.data is not None:
            #由于签名要求唯一性，包括顺序，所以需要按照参数名称排序
           # sortedD = sorted(self.data.items(), key=lambda x: x[0])  # 先通过 self.data.items() 转化为 List, 然后利用 sorted 方式按照 key 排序
            sortedD = json.loads(self.data).items()
            for k,v in sortedD:
                sign += self.percentEncode(k) + '=' +self.percentEncode(v)+'&'
                if sign[-1]=='&':
                    sign=sign[:-1]
        m = hashlib.md5()
        sign = m.update(sign.encode('utf8'))  #必须将文本字符串编码，转换为已编码的字节字符串类型
        self.headers["Content-Sign"]=m.hexdigest()  #将加密后的sign存入headers
        print(m.hexdigest())
        try:
            print(self.url)
            response = requests.post(self.url, headers=self.headers, params=self.params, data=self.data, timeout=float(timeout))
            # response.raise_for_status()
            #return response.json()
            print(self.headers)
            print(self.data)
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None
    # defined http post method
    # include upload file
    def postWithFile(self):
        """
        defined post method
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files, timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    # defined http post method
    # for json
    def postWithJson(self):
        """
        defined post method
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, json=self.data, timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    #构造一个编码函数，对一个字符串进行utf-8编码，返回编码后的字符串
    def percentEncode(self,p):
         p = str(p)
         res = urllib.parse.quote(p.encode('utf8'), '')
         res = res.replace('+', '%20')
         res = res.replace('*', '%2A')
         res = res.replace('%7E', '~')
         return res


if __name__ == "__main__":
    print("ConfigHTTP")








