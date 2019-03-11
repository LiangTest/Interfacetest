from aifc import Error

from common.configDB import MyDB

myDB = MyDB()

#通过商户账户名称查询商户id
def getMerchant_id(login_name):
    q = myDB.executeSQL("yongda_merchant","merchant","getmerchant_id",login_name)
    if q.rowcount>0:
        merchantid=q.fetchone()[0]
        return merchantid
    else:
        return None
    myDB.closeDB()

#删除商户表基础数据
def delMerchant(merchantid):
    q = myDB.executeSQL("yongda_merchant","merchant","delmerchant",merchantid)
    myDB.closeDB()

#删除商户银行卡表数据
def delMerchant_bank(merchantid):
    q = myDB.executeSQL("yongda_merchant","merchant_bank","delmerchant_bank",merchantid)
    myDB.closeDB()

#删除商户联系人表数据
def delMerchant_contact(merchantid):
    q = myDB.executeSQL("yongda_merchant","merchant_contact","delmerchant_contact",merchantid)
    myDB.closeDB()

# 删除商户资料表数据
def delMerchant_info(merchantid):
    q = myDB.executeSQL("yongda_merchant","merchant_info","delmerchant_info",merchantid)
    myDB.closeDB()

#删除商户ip白名单数据
def delMerchant_ip_whitelist(merchantid):
    q = myDB.executeSQL("yongda_merchant","merchant_ip_whitelist","delmerchant_ip_whitelist",merchantid)
    myDB.closeDB()

#删除商户业务表数据
def delMerchant_product(merchantid):
    q = myDB.executeSQL("yongda_merchant","merchant_product","delmerchant_product",merchantid)
    myDB.closeDB()

#删除商户密钥表数据
def delMerchant_secret(merchantid):
    q = myDB.executeSQL("yongda_merchant","merchant_secret","delmerchant_secret",merchantid)
    myDB.closeDB()

#删除商户尽调表数据
def delMerchant_survey(merchantid):
    q = myDB.executeSQL("yongda_merchant","merchant_survey","delmerchant_survey",merchantid)
    myDB.closeDB()

#删除商户授信表数据
def delCredit_audit(merchantid):
    q = myDB.executeSQL("yongda_merchant","credit_audit","delcredit_audit",merchantid)
    myDB.closeDB()



#查询商户memberid
def getMerchant_memberid_formid(formid):
    q = myDB.executeSQL("yongda_account","member","getmemberforfromid",formid)
    if q.rowcount>0:
        memberid=q.fetchone()[0]
        return memberid
    else:
        return None
    myDB.closeDB()

#删除商户账户信息表
def delMerchant_member(memberid):
    q = myDB.executeSQL("yongda_account","member","delmemberformemberid",memberid)
    myDB.closeDB()

#删除商户账户信息表数据
def delMerchant_member_account(memberid):
    q = myDB.executeSQL("yongda_account","member_account","delmemberaccount",memberid)
    myDB.closeDB()

#通过memberid删除商户外部户
def delMerchant_outaccount(memberid):
    q = myDB.executeSQL("yongda_dpm","out_account","delout_account",{'memberid':memberid})
    myDB.closeDB()

# 通过memberid删除商户外部户，详细记录
def delMerchant_outaccount_detail(memberid):
    q = myDB.executeSQL("yongda_dpm","out_account_detail","delout_account_detail",{'memberid':memberid})
    myDB.closeDB()

# 通过memberid删除商户外部户余额，详细记录
def delMerchant_outaccount_subdetail(memberid):
    q = myDB.executeSQL("yongda_dpm", "out_account_sub_detail", "delout_account_sub_detail", {'memberid': memberid})
    myDB.closeDB()

# 通过memberid删除商户外部户的余额
def delMerchant_outaccount_sub(memberid):
    q = myDB.executeSQL("yongda_dpm", "out_account_subset", "delout_account_subset", {'memberid': memberid})
    myDB.closeDB()


def delAllmerchant_info(login_name):

    merchantid = getMerchant_id(login_name)
    memberid = getMerchant_memberid_formid(merchantid)

    if merchantid != '' and merchantid is not None:
        delMerchant(merchantid)
        delMerchant_bank(merchantid)
        delMerchant_contact(merchantid)
        delMerchant_info(merchantid)
        delMerchant_ip_whitelist(merchantid)
        delMerchant_product(merchantid)
        delMerchant_secret(merchantid)
        delMerchant_survey(merchantid)
        delCredit_audit(merchantid)


    if memberid != '' and memberid is not None:
        delMerchant_member(memberid)
        delMerchant_member_account(memberid)
        delMerchant_outaccount(memberid)
        delMerchant_outaccount_detail(memberid)
        delMerchant_outaccount_subdetail(memberid)
        delMerchant_outaccount_sub(memberid)












if __name__ == '__main__':
    try:
        delAllmerchant_info("test88@qq.com")
        #print(getMerchant_id("test05@qq.com"))
        #print(getMerchant_memberid_formid('36'))

    except Error as e:
        print(e)

    # except(RuntimeError, TypeError, NameError):
    #     pass
    #delPayPSWSet('18058198172')