import json
from time import sleep

from jpype import *
import jpype
from common.configDB import MyDB
import os

import readConfig

localReadConfig = readConfig.ReadConfig()
mydb = MyDB()
jvmPath = jpype.get_default_jvm_path()


#jarPath1 = "/Users/yongdapay/yongda/utils_jar/utils.jar"
jarPath1 = "/Users/yongdapay/yongda/dependencies.jar"
dependency = os.path.join(os.path.abspath('.'), "/Users/yongda/yongda/utils_jar")

if jpype.isJVMStarted():
    pass
else:
    jpype.startJVM(jvmPath, "-Djava.class.path=%s"%jarPath1)
securityUtilClass = jpype.JClass("yongda.util.ParamSecurityUtil")
spzxMainClass = jpype.JClass("yongda.SpzxMain")


# class JSONObejct(object):
#     def __init__(self,data):
#         self.__dict__ = json.loads(data)
# 获取组装后的接口参数，调用jar包中的JSON class，来生成token
def getParamSecure(params,publicKey,secretKey):
    params = json.JSONEncoder().encode(params)
    params = jpype.JClass("com.alibaba.fastjson.JSON").parseObject(params)
    return securityUtilClass.getParamSecure(params, publicKey, secretKey)


# 调用jar包中的yongda.SpzxMain，来自动通过借款单信审
def getSpzxMain(loan_id):
    params = {"auditResult":"1","auditMsg":"通过"}
    #执行查询数据库，通过loan_id获得记录
    sleep(1)
    q = mydb.executeSQL("yongda_workbench","workorder","getWorkorder",loan_id)
    result = q.fetchone()
    #result = [1,2,3]
    i = 0
    if result is not None:
        while not result[2]:
            sleep(1)
            i = i + 1
            q = mydb.executeSQL("yongda_workbench", "workorder", "getWorkorder", loan_id)
            result = q.fetchone()

        serialNo = result[0]
        orderNo = result[1]
        contractSerialNo = result[2]
        params.update(serialNo = serialNo)
        params.update(orderNo = orderNo)
        params.update(contractSerialNo = contractSerialNo)
        mydb.closeDB()
        params = json.JSONEncoder().encode(params)

        print(params)
    return spzxMainClass.main([params])



