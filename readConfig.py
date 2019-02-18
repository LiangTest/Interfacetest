import os
import codecs
import configparser
import unittest

proDir = os.path.split(os.path.realpath(__file__))[0]  #返回工程目录  os.path.realpath(path) 返回path的真实路径;os.path.split(path) 将path分割成目录和文件名二元组返回;__file__为被执行代码所在文件的绝对路径名
configPath = os.path.join(proDir, "config.ini")  #凭借configPath

class ReadConfig:
    def __init__(self):
        fd = open(configPath)
        data = fd.read()

        # Windows系统的txt文件在使用utf-8编码保存时会默认在文件开头插入三个不可见的字符（0xEF 0xBB 0xBF）称为BOM头，
        # 这个BOM头在python的codecs库中已经定义为常量（codecs.BOM_UTF8）
        #  remove BOM 去掉BOM头
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf=configparser.ConfigParser()  #实例化
        self.cf.read(configPath)  #读取配置文件，以列表形式返回


    def get_Email(self,name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self,name):
        value = self.cf.get("HTTP",name)
        return value

    def get_headers(self,name):
        value = self.cf.get("HEADERS",name)
        return value

    def set_headers(self,name,value):
        self.cf.set("HEADERS",name,value)
        with open(configPath,"w+") as fw:
            self.cf.write(fw)

    def get_database(self,name):
        value = self.cf.get("DATABASE",name)
        return value

    def get_url(self,name):
        value = self.cf.get("URL",name)
        return value

    def get_WeChat(self,name):
        value = self.cf.get("WeChat",name)
        return value

    def get_Secure(self,name):
        value = self.cf.get("SECURE",name)
        return value

    #设置并读取loan_id
    def get_loan(self,name):
        value = self.cf.get("loan",name)
        return value

    def set_loan(self,name,value):
        self.cf.set("loan", name, value)
        with open(configPath, "w+") as fw:
            self.cf.write(fw)
            fw.close()
    #设置并读取绑卡serialno
    def get_bindSerialNo(self,name):
        value = self.cf.get("BindCard",name)
        return value
    def set_bindSerialNo(self,name,value):
        self.cf.set("BindCard", name, value)
        with open(configPath, "w+") as fw:
            self.cf.write(fw)
            fw.close()
    #读取下载对账单参数
    def get_downloadState(self,name):
        value = self.cf.get("downloadstatement",name)
        return value







