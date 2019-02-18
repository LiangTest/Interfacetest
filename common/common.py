import requests
import readConfig as readConfig
import os
from xlrd import open_workbook
from xml.etree import ElementTree as ElementTree
from common.log import MyLog as Log
from common import configHttp
import json

localReadConfig = readConfig.ReadConfig()
proDir = readConfig.proDir
localConfigHttp = configHttp.ConfigHttp()
log = Log.get_log()
logger = log.get_logger()

caseNo = 0


# def get_visitor_token():
#     """
#     create a token for visitor
#     :return:
#     """
#     host = localReadConfig.get_http("BASEURL")
#     response = requests.get(host+"/v2/User/Token/generate")
#     info = response.json()
#     token = info.get("info")
#     logger.debug("Create token:%s" % (token))
#     return token


# def set_visitor_token_to_config():
#     """
#     set token that created for visitor to config
#     :return:
#     """
#     token_v = get_visitor_token()
#     localReadConfig.set_headers("TOKEN_V", token_v)


def get_value_from_return_json(json, name1, name2):
    """
    get value by key
    :param json:
    :param name1:
    :param name2:
    :return:
    """
    info = json['info']
    group = info[name1]
    value = group[name2]
    return value


def show_return_msg(response):
    """
    show msg detail
    :param response:
    :return:
    """
    url = response.url
    msg = response.text
    print("\n请求地址："+url)
    # 可以显示中文
    print("\n请求返回值："+'\n'+json.dumps(json.loads(msg), ensure_ascii=False, sort_keys=True, indent=4))
# ****************************** read testCase excel ********************************


def get_xls(xls_name, sheet_name):
    """
    从Excel中读取测试用例
    :param xls_name:文件名
    :param sheet_name:
    :return:
    """
    cls = []
    # 获取Excel文件路径
    xlsPath = os.path.join(proDir, "testFile", 'case', xls_name)
    # 打开Excel文件
    file = open_workbook(xlsPath)
    # 获取sheet
    sheet = file.sheet_by_name(sheet_name)
    # 获取每一行数据（除了表头）
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
    return cls

# ******************************  从xml文件中读取sql语句 ********************************
database = {}


def set_xml():
    """
    set sql xml
    :return:
    """
    if len(database) == 0:
        sql_path = os.path.join(proDir, "testFile", "SQL.xml")
        tree = ElementTree.parse(sql_path)  #利用xml.etree.Element来对xml文件进行操作
        for db in tree.findall("database"):
            db_name = db.get("name")
            db_info = {'db_info':{'database' : db_name,'type' : db.get("type"),'host' : db.get("host"),'username':db.get("username"),'password' :db.get("password"),'port' :db.get("port")}}

            table = {}
            for tb in db.getchildren():
                table_name = tb.get("name")
                #print(table_name)
                sql = {}
                for data in tb.getchildren():
                    sql_id = data.get("id")
                    #print(sql_id)
                    sql[sql_id] = data.text
                table[table_name] = sql
            db_info.update(table)
            database[db_name] = db_info


def get_xml_dict(database_name, table_name):
    """
    get db dict by given name
    :param database_name:
    :param table_name:
    :return:
    """
    set_xml()
    database_dict = database.get(database_name).get(table_name)
    return database_dict

def get_db_info(database_name):
    """
    get sql by given name and sql_id
    :param database_name:
    :param table_name:
    :param sql_id:
    :return:
    """
    set_xml()
    # print('database')
    # print(database)
    db_info = database.get(database_name).get('db_info')
    # print('db_info')
    # print(db_info)
    return db_info


def get_sql(database_name, table_name, sql_id):
    """
    get sql by given name and sql_id
    :param database_name:
    :param table_name:
    :param sql_id:
    :return:
    """
    db = get_xml_dict(database_name, table_name)
    sql = db.get(sql_id)
    return sql
# ****************************** 从xml文件中读取接口url ********************************


def get_url_from_xml(name):
    """
    By name get url from interfaceURL.xml
    :param name: interface's url name
    :return: url
    """
    url_list = []
    url_path = os.path.join(proDir, 'testFile', 'interfaceURL.xml')
    tree = ElementTree.parse(url_path)
    for u in tree.findall('url'):
        url_name = u.get('name')
        if url_name == name:
            for c in u.getchildren():
                url_list.append(c.text)

    url = '/v2/' + '/'.join(url_list)
    return url

if __name__ == "__main__":
    # print(get_xls("queryVerifyCode"))
    # set_visitor_token_to_config()
    print(get_sql("test","testtable1","queryVerifyCode"))
