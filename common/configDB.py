import datetime
import pymysql
import cx_Oracle
import common.common as common
import readConfig as readConfig
from common.log import MyLog as Log
import os

#oracle 设置字符集
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'



localReadConfig = readConfig.ReadConfig()


class MyDB:
    # global host, username, password, port, database, config
    # host = localReadConfig.get_database("dc_host")
    # username = localReadConfig.get_database("dc_username")
    # password = localReadConfig.get_database("dc_password")
    # port = localReadConfig.get_database("dc_port")
    # database = localReadConfig.get_database("dc_database")
    # config = {
    #     'host': str(host),
    #     'user': username,
    #     'passwd': password,
    #     'port': int(port),
    #     'db': database
    # }

    def __init__(self):
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.db = None
        self.cursor = None

    def connectDB(self,dbname):
        """
        connect to database
        :return:
        """
        db_info = common.get_db_info(dbname)
        host = db_info['host']
        username = db_info['username']
        password = db_info['password']
        port = db_info['port']
        database = db_info['database']
        self.type = db_info['type']
        config = {
            'host': str(host),
            'user': username,
            'passwd': password,
            'port': int(port),
            'db': database,
            'charset':'utf8'
                }
        if self.type.lower() =='mysql':  #全部转换成小写再匹配
            try:
                # connect to DB
                print("Connect DB!")
                self.time_s = datetime.datetime.now()
                self.db = pymysql.connect(**config)
                self.time_e = datetime.datetime.now()
                # create cursor
                self.cursor = self.db.cursor()
                print("Connect DB successfully!")
                print("连接时长：",(self.time_e -self.time_s).total_seconds(),'s')
            except ConnectionError as ex:
                self.logger.error(str(ex))
        elif self.type.lower()  =='oracle':  #全部转换成小写再匹配
            try:
                # connect to DB
                par = username+'/'+password+'@'+host+':'+port+'/'+dbname
                # print(par)
                self.db = cx_Oracle.connect(par)
                # create cursor
                self.cursor = self.db.cursor()
                print("Connect DB successfully!")
            except ConnectionError as ex:
                self.logger.error(str(ex))

    # def executeSQL(self, sql, params):
    #     """
    #     execute sql
    #     :param sql:
    #     :return:
    #     """
    #     self.connectDB()
    #     # executing sql
    #     self.cursor.execute(sql, params)
    #     # executing by committing to DB
    #     self.db.commit()
    #     return self.cursor

    def executeSQL(self, database_name, table_name, sql_id, params):
        """
        execute sql
        :param sql:
        :return:
        """
        db = common.get_xml_dict(database_name, table_name)
        sql = db.get(sql_id)
        self.connectDB(database_name)
        # executing sql
        print("操作:sql:" + sql)
        self.cursor.execute(sql, params)
        # executing by committing to DB
        self.db.commit()
        return self.cursor

    # def executeSQLofOracle(self, database_name, table_name,sql_id, params):
    #     """
    #     execute sql
    #     :param sql:
    #     :return:
    #     """
    #     db = common.get_xml_dict(database_name, table_name)
    #     sql = db.get(sql_id)
    #     self.connectDB(database_name)
    #     # executing sql
    #     self.cursor.execute(sql, params)
    #     # executing by committing to DB
    #     self.db.commit()
    #     return self.cursor

    def get_all(self, cursor):
        """
        get all result after execute sql
        :param cursor:
        :return:
        """
        value = cursor.fetchall()
        return value

    def get_one(self, cursor):
        """
        get one result after execute sql
        :param cursor:
        :return:
        """
        value = cursor.fetchone()
        return value

    def closeDB(self):
        """
        close database
        :return:
        """
        self.db.close()
        print("Database closed!")

