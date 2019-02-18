from common.configDB import MyDB
myDB = MyDB()

def getVerifyCode(phone):
        #sql = root.getElementsByTagName('sql')
        # q = configDB.MyDB.executeSQL(sql,phone)
        # configDB.MyDB.closeDB()
        # return q
    #sql = common.get_sql("dccj_20161022","ch_msg_code","queryVerifyCode")
    q = myDB.executeSQL("dccj_20161022","ch_msg_code","queryVerifyCode",phone)
    result=q.fetchone()
    if result is not None:
        code=result[1]
        return {'code':code}
    else:
        return {'msg':'该手机号无短信验证码'}
    myDB.closeDB()


if __name__ == '__main__':
    print(getVerifyCode('18458104743'))












