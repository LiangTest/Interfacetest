import cx_Oracle
import MySQLdb
import time
import string
from DBUtils.PooledDB import PooledDB


def CreateConnectionpool(connstr,dbtype,maxconn):
    if dbtype=='oracle':
        try:
            db_conn = connstr.split("#");
            pool = PooledDB(cx_Oracle, user = db_conn[0], password = db_conn[1], dsn = db_conn[2],threaded=True,mincached=maxconn,maxcached=maxconn,maxshared=maxconn,maxconnections=maxconn)
            return pool
        except Exception as e:
            raise Exception('conn targetdb datasource Excepts,%s!!!(%s).' % (db_conn[2], str(e)))
            return None
    elif dbtype=='mysql':
        try:
            db_conn = connstr.split("#");
            pool = PooledDB(MySQLdb, user=db_conn[0],passwd=db_conn[1],host=db_conn[2],port=string.atoi(db_conn[3]),db=db_conn[4],mincached=maxconn,maxcached=maxconn,maxshared=maxconn,maxconnections=maxconn)
            return pool
        except Exception as e:
            raise Exception('conn datasource Excepts,%s!!!(%s).' % (db_conn[2], str(e)))
            return None

#oracle如下创建连接池：
connstring="alidba#alidba#test.db.alibaba.com:1525/testdb"
oraclepool=CreateConnectionpool(connstring,"oracle",10)
#获取连接：
conn=oraclepool.connection()
#返还连接:
conn.close()

#mysql如下创建连接池：
connstring="alibaba#alibaba#test.db.alibaba.com#3306#database";
mysqlpool=CreateConnectionpool(connstring,"mysql",10);
#获取连接:
conn=mysqlpool.connection()
#返还连接:
conn.close()