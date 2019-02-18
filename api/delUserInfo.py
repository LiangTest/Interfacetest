from aifc import Error

from common.configDB import MyDB

myDB = MyDB()

#点车库相关
def delUser(cellphone):
    q = myDB.executeSQL("dccj_20161022","t_sys_user","delUser",cellphone)
    myDB.closeDB()

"""更改实名认证登记"""
def delAuthEntication(cellphone):
    q = myDB.executeSQL("dccj_20161022","t_sys_user","delAuthEntication",cellphone)
    myDB.closeDB()

def getMemberIdBycellphone(cellphone):
    q = myDB.executeSQL("dccj_20161022","t_sys_user","getMemberIdBycellphone",cellphone)
    if q.rowcount>0:
        memberId=q.fetchone()[0]
        return memberId
    else:
        return None
    myDB.closeDB()



def getMemberAccount(memberid):
    q = myDB.executeSQL("yongda_account", "member_account", "getMemberAccount", {'memberid':memberid})
    if q.rowcount>0:
        memberid = []
        for var in q.fetchall():
            print(var)
            memberid.append(var[0])
        return memberid
    else:
        return None
    myDB.closeDB()

def getMemberIdByname(name):
    q = myDB.executeSQL("dccj_20161022","t_sys_user","getMemberIdByname",name)
    if q.rowcount>0:
        memberId=q.fetchone()[0]
        return memberId
    else:
        return None
    myDB.closeDB()

def getMemberIdandNameBycellphone(cellphone):
    q = myDB.executeSQL("dccj_20161022","t_sys_user","getMemberIdandNameBycellphone",cellphone)
    if q.rowcount>0:
        return q.fetchone()
    else:
        return None
    myDB.closeDB()

def getNameBycellphone(cellphone):
    q = myDB.executeSQL("dccj_20161022","t_sys_user","getNameBycellphone",cellphone)
    if q.rowcount>0:
        name=q.fetchone()[0]
        return name
    else:
        return None
    myDB.closeDB()


def delUserLogin(cellphone):
    q = myDB.executeSQL("dccj_20161022","t_sys_user_login","delUserLogin",cellphone)
    myDB.closeDB()

"""通过银行预留手机号删除绑定银行卡"""
def delBankCardByPhon(mobile_num):
    q = myDB.executeSQL("dccj_20161022","t_sys_user_bank_card","delBankCardByPhon",mobile_num)
    myDB.closeDB()

"""通过memberId删除绑定银行卡"""
def delBankCardByMemberId(memberId):
    q = myDB.executeSQL("dccj_20161022","t_sys_user_bank_card","delBankCardByMemberId",memberId)
    myDB.closeDB()

"""通过姓名删除绑定银行卡"""
def delBankCardByName(name):
    q = myDB.executeSQL("dccj_20161022","t_sys_user_bank_card","delBankCardByName",name)
    myDB.closeDB()


"""删除绑定第三方账号"""
def delUserAuth(identity):
    # member_id = getMemberIdByidentity(identity)
    q = myDB.executeSQL("dccj_20161022","t_sys_user_auth","delUserAuth",identity)
    myDB.closeDB()

"""删除登录密码"""
def delLoginPSWSet(cellphone):
    q = myDB.executeSQL("dccj_20161022","t_sys_user","delLoginPSWSet",cellphone)
    myDB.closeDB()

"""删除支付密码"""
def delPayPSWSet(cellphone):
    q = myDB.executeSQL("dccj_20161022","t_sys_user","delPayPSWSet",cellphone)
    myDB.closeDB()

#支付核心库相关
"""获取MemberId"""
def getMemberIdByidentity(identity):
    par = {'identity':identity}
    q = myDB.executeSQL("pay15db","tm_member_identity","getMemberIdByidentity",par)
    if q.rowcount>0:
        memberId=q.fetchone()[0]
        return memberId
    else:
        return None
    myDB.closeDB()

"""删除identity信息"""
def delMemberIdByIdentity(identity):
    par = {'identity':identity}
    q = myDB.executeSQL("pay15db","tm_member_identity","delMemberIdByIdentity",par)
    myDB.closeDB()

"""删除identity信息"""
def delMemberIdByMemberId(MemberId):
    par = {'Member_Id':MemberId}
    q = myDB.executeSQL("pay15db","tm_member_identity","delMemberIdByMemberId",par)
    myDB.closeDB()

"""删除认证等级"""
def delMember(member_id):
    par = {'member_id':member_id}
    q = myDB.executeSQL("pay15db","TM_MEMBER","delMember",par)
    myDB.closeDB()

"""删除实名身份证信息"""
def delMemberVerify(member_id):
    par = {'member_id':member_id}
    q = myDB.executeSQL("pay15db","tr_verify_entity","delMemberVerify",par)
    myDB.closeDB()

"""获取VerifyID"""
def getVerifyID(member_id):
    par = {'member_id':member_id}
    q = myDB.executeSQL("pay15db","tr_verify_entity","getVerifyID",par)
    if q.rowcount>0:
        verifyID=q.fetchone()[0]
        return verifyID
    else:
        return None
    myDB.closeDB()

"""删除个人会员信息"""
def delPersonalMenmer(member_id):
    par = {'member_id':member_id}
    q = myDB.executeSQL("pay15db","TR_PERSONAL_MEMBER","delPersonalMenmer",par)
    myDB.closeDB()

"""删除支付核心的银行卡"""
def delBankAccount(member_id):
    par = {'member_id':member_id}
    q = myDB.executeSQL("pay15db","TR_BANK_ACCOUNT","delBankAccount",par)
    myDB.closeDB()

"""通过姓名删除支付核心的银行卡"""
def delBankAccountByName(name):
    par = {'name':name}
    q = myDB.executeSQL("pay15db","TR_BANK_ACCOUNT","delBankAccountByName",par)
    myDB.closeDB()

"""删除绑定用户"""
def delVerifyRef(member_id):
    par = {'member_id':member_id}
    q = myDB.executeSQL("pay15db","tr_verify_ref","delVerifyRef",par)
    myDB.closeDB()



#业务库相关
"""通过银行预留手机号删除绑定银行卡"""
def delBankCardByPhon1(mobile_num):
    q = myDB.executeSQL("dccj_cashier","channel_sign_info","delBankCardByPhon",mobile_num)
    myDB.closeDB()

"""通过memberId删除绑定银行卡"""
def delBankCardByMemberId1(memberId):
    q = myDB.executeSQL("dccj_cashier","channel_sign_info","delBankCardByMemberId",memberId)
    myDB.closeDB()

"""通过姓名删除绑定银行卡"""
def delBankCardByName1(name):
    q = myDB.executeSQL("dccj_cashier","channel_sign_info","delBankCardByName",name)
    myDB.closeDB()

"""删除实名信息"""
def delidentity(memberId):
    q = myDB.executeSQL("dccj_live","live_identity_info","delidentity",memberId)
    myDB.closeDB()
"""删除获取额度记录表"""
def delusercommit(memberid):
    q = myDB.executeSQL("dccj_live","user_commit_info","delusercommit",memberid)
    myDB.closeDB()
""""""
def delusercommitbyname(name):
    q = myDB.executeSQL("dccj_live","user_commit_info","delusercommitbyname",name)
    myDB.closeDB()

#信用账户相关
"""获取信用账户memberid"""
def getmemberid(name):
    q = myDB.executeSQL("yongda_account","member","getmemberid",name)
    if q.rowcount>0:
        memberid=q.fetchone()[0]
        return memberid
    else:
        return None
    myDB.closeDB()

"""获取信用账户fromid，用于删除user库中的表数据"""
def getfromid(name):
    q = myDB.executeSQL("yongda_account","member","getfromid",name)
    if q.rowcount>0:
        memberid=q.fetchone()[0]
        return memberid
    else:
        return None
    myDB.closeDB()

"""获取外部账户"""
def getout_account(memberid):
    q = myDB.executeSQL("yongda_dpm","out_account","getout_account",{'memberid':memberid})
    if q.rowcount>0:
        memberid=q.fetchone()[0]
        return memberid
    else:
        return None
    myDB.closeDB()

"""删除外部账户"""
def delout_account(memberid):
    q = myDB.executeSQL("yongda_dpm","out_account","delout_account",{'memberid':memberid})
    myDB.closeDB()

"""删除外部账户余额明细表"""
def deloutaccountdetail(memberid):
    q = myDB.executeSQL("yongda_dpm","out_account_detail","delout_account_detail",{'memberid':memberid})
    myDB.closeDB()

"""删除外部账户分账户表"""
def deloutaccountsubset(memberid):
    q = myDB.executeSQL("yongda_dpm", "out_account_subset", "delout_account_subset", {'memberid': memberid})
    myDB.closeDB()

"""删除外部账户分账户明细表"""
def deloutaccountsubsetdetail(memberid):
    q = myDB.executeSQL("yongda_dpm", "out_account_sub_detail", "delout_account_sub_detail", {'memberid': memberid})
    myDB.closeDB()

"""删除账户member信息"""
def delmemberformemberid(memberid):
    q = myDB.executeSQL("yongda_account","member","delmemberformemberid",memberid)
    myDB.closeDB()

"""删除账户信息"""
def delmemberaccount(memberid):
    q = myDB.executeSQL("yongda_account","member_account","delmemberaccount",memberid)
    myDB.closeDB()

"""删除会员与外部关系表"""
def delexternal(memberid):
    q = myDB.executeSQL("yongda_user","member_external_user","delexternal",memberid)
    myDB.closeDB()

"""删除基础ocr认证与职业认证表"""
def delmemberinfo(memberid):
    q = myDB.executeSQL("yongda_user","member_info","delmemberinfo",memberid)
    myDB.closeDB()

"""删除baseinfo信息"""
def delbaseinfo(name):
    q = myDB.executeSQL("dccj_live","base_info","delbaseinfo",name)
    myDB.closeDB()

"""删除联系人信息"""
def delcontactinfo(memberid):
    q = myDB.executeSQL("dccj_live","contacts_info","delcontacts_info",memberid)
    myDB.closeDB()

"""删除live_order信息"""
def dellive_order(name):
    q = myDB.executeSQL("dccj_live","live_order","dellive_order",name)
    myDB.closeDB()

"""删除用户联系信息"""
def deluser_contacts_info(memberid):
    q = myDB.executeSQL("dccj_live","user_contacts_info","deluser_contacts_info",memberid)
    myDB.closeDB()

"""删除清除用户天数限制表"""
def delcredit_result(memberid):
    q = myDB.executeSQL("yongda_user", "credit_result", "delcreditresult", memberid)
    myDB.closeDB()

"""删除personalmember信息"""
def delpersonalmember(memberid):
    q = myDB.executeSQL("yongda_user","personal_member","delpersonalmember",memberid)
    myDB.closeDB()

"""删除微商贷授信数据"""
def delusercredit(memberid):
    q = myDB.executeSQL("yongda_micromerchant","user_credit","delusercredit",memberid)
    myDB.closeDB()

def delmicro_credit_audit(memberid):
    q = myDB.executeSQL("yongda_user","micro_credit_audit","delmicro_credit_audit",memberid)
    myDB.closeDB()

"""删除授信中亲属配偶数据"""
def delmemberinforelation(memberid):
    q = myDB.executeSQL("yongda_user","member_info_relation","delmemberinforelation",memberid)
    myDB.closeDB()

"""删除慢慢花授信"""
def delmmh_credit_audit(memberid):
    q = myDB.executeSQL("yongda_user","mmh_credit_audit","delmmh_credit_audit",memberid)
    myDB.closeDB()

def delcar(memberid):
    q = myDB.executeSQL("yongda_micromerchant","car_info","delcar",memberid)
    myDB.closeDB()

def delmicroorder(memberid):
    q = myDB.executeSQL("yongda_micromerchant","micro_order","delmicroorder",memberid)
    myDB.closeDB()

#删除统一登录信息
def del_entry_login(memberid):
    q = myDB.executeSQL("yongda_entry","entry_user_login","del_entry_login",memberid)
    myDB.closeDB()

#删除达分期授信

def delworkorder_forstage(memberid):
    q=myDB.executeSQL("yongda_workbench","workorder_forstage","delworkorder_forstage",memberid)
    myDB.closeDB()

def delfor_stage_audit(memberid):
    q = myDB.executeSQL("yongda_user","for_stage_audit","delfor_stage_audit",memberid)
    myDB.closeDB()

#风控增加社会信息
def delrisk_baseinfo(memberid):
    q = myDB.executeSQL("yongda_risk", "risk_base_info", "delrisk_baseinfo", memberid)
    myDB.closeDB()

#达分期授信
def delsocial_info(memberid):
    q = myDB.executeSQL("dccj_live", "social_info", "delsocial_info", memberid)
    myDB.closeDB()


# 达分期相关订单信息

#达分期订单审核表
def delworkorder_forstage_order(memberid):
    q = myDB.executeSQL("yongda_workbench", "workorder_forstage_order", "delworkorder_forstage_order", memberid)
    myDB.closeDB()

#达分期首付表
def deldown_payment(memberid):
    q = myDB.executeSQL("dccj_live", "down_payment", "deldown_payment", memberid)
    myDB.closeDB()

#达分期，还款单表
def dellive_repay(memberid):
    q = myDB.executeSQL("dccj_live", "live_repay", "dellive_repay", memberid)
    myDB.closeDB()

#达分期订单
def delforstage_order(memberid):
    q = myDB.executeSQL("dccj_live", "forstage_order", "delforstage_order", memberid)
    myDB.closeDB()


#获取统一登录发的短信验证码
def get_verify_code(phone):
    q = myDB.executeSQL("yongda_entry","verify_code","get_verify_code",phone)
    if q.rowcount>0:
        list = q.fetchone()
        code = list[0]
        status = list[1]
        return {'code':code,'status':status}
    else:
        return {'msg':'该手机号无可用短信验证码'}
    myDB.closeDB()

#删除好美意相关业务数据
#删除好美意授信
def delhomecase_order(memberid):
    q = myDB.executeSQL("yongda_user", "home_case_audit", "delhome_case_audit", memberid)
    myDB.closeDB()



"""删除信用账户所有数据（包括微商贷、慢慢花等所有业务）"""
def del_all_account(phone):
    infolist = getMemberIdandNameBycellphone(phone)
    if infolist is not None:
        memberId = infolist[0]  # 支付核心的memberid
        name = infolist[1]  # 用户姓名
        if name != '' and name is not None:
            memberid = getmemberid(name)  # 获取信用核心的memberid
            dellive_order(name)
            delusercommitbyname(name)
            if memberid is not None:
                deldpm(memberid)
                delmember(memberid)
                delaccount(memberid)
                delexternal(memberid)
                delmemberinfo(memberid)
                delpersonalmember(memberid)
        if memberId is not None:
            '''删除业务库相关数据'''
            delcredit(memberId)
            deldelmicro_credit_audit(memberId)
            delcar(memberId)
            delmicroorder(memberId)
            delbaseinfo(name)
            delworkorder_forstage(memberId)
            delfor_stage_audit(memberId)
            delrisk_baseinfo(memberId)
            delsocial_info(memberId)
            delworkorder_forstage_order(memberId)
            deldown_payment(memberId)
            dellive_repay(memberId)
            delforstage_order(memberId)
            '''删除银行卡信息'''
            # delBankCardByMemberId(memberId)  # 删除银行卡时将点车成金库里面删掉
            # delBankAccount(memberId)
            # delBankCardByMemberId1(memberId)  # 删除银行卡时将业务库里面删掉
            '''删除实名信息'''
            delidentity(memberId)
            del_entry_login(memberId)

        return "已删除该用户信用账户信息"
    else:
        return "该手机号未查到用户信息"



def delBankCard(phone):
    memberId = getMemberIdBycellphone(phone)
    if memberId is not None:
        delBankCardByMemberId(memberId) #删除银行卡时将点车成金库里面删掉
        delBankAccount(memberId)
        delBankCardByMemberId1(memberId) #删除银行卡时将业务库里面删掉
        delAuth(phone)
        return "已删除银行卡和实名信息"
    else:
        return "该手机号未查到用户信息"

"""只删除银行卡"""
def delBankCard1(phone):
    memberId = getMemberIdBycellphone(phone)
    if memberId is not None:
        delBankCardByMemberId(memberId)
        delBankAccount(memberId)
        delBankCardByMemberId1(memberId) #删除银行卡时将业务库里面删掉
        return "已删除银行卡"
    else:
        return "该手机号未查到用户信息"

"""通过姓名删除银行卡"""
def delBankCard2(name):
    delBankCardByName(name)
    delBankCardByName1(name)
    delBankAccountByName(name)
    return "已删除银行卡"

"""删除实名信息"""
def delAuth(phone):
    infolist = getMemberIdandNameBycellphone(phone)
    if infolist is not None:
        memberId = infolist[0]
        name = infolist[1]
        if memberId != '' and memberId is not None:
            delUserAuth(memberId)
            delVerifyRef(memberId)
            delMemberIdByMemberId(memberId)
            # delMember(memberId)
            delPersonalMenmer(memberId)
            delidentity(memberId)
            delMemberVerify(memberId)
            delbaseinfo(name)
        else:
            return "该用户未实名"
        return "已删除还用户实名信息"
    else:
        return "该手机号未查到用户信息"

"""只删除信用账户授信信息"""
def delCredit(phone):
    # 通过查询支付核心库获取bus_id,和用户名，当用户通过手机app注册时，bus_id等同于信用生活member_id或external_user_id
    infolist = getMemberIdandNameBycellphone(phone)
    if infolist is not None:
        memberId = infolist[0]
        name = infolist[1]
        if name != '' and name is not None:
            fromid = getfromid(name)     #获取信用账户fromid，对应到user库的member_id
            memberid = getmemberid(name)
            delout_account(memberid)
            deloutaccountsubset(memberid)
            deloutaccountdetail(memberid)
            deloutaccountsubsetdetail(memberid)
            delhomecase_order(fromid)
            delcredit_result(fromid)
            delmemberinfo(fromid)
            delmemberinforelation(fromid)
            delpersonalmember(fromid)
            delmicro_credit_audit(fromid)
            delexternal(fromid)
            delmemberformemberid(memberid)
            delmemberaccount(memberid)


        if memberId != '' and memberId is not None:
            delsocial_info(memberId)
            delidentity(memberId)
            delmmh_credit_audit(memberId)
            delbaseinfo(name)
            delcontactinfo(memberId)
            delusercommit(memberId)
            deluser_contacts_info(memberId)
            delfor_stage_audit(memberId)
            delmemberinfo(memberId)
            delusercredit(memberId)
            delrisk_baseinfo(memberId)
        return "已删除用户信用账户业务授信信息"
    else:
        return "未查询到用户信息"





def delforstage(phone):
    infolist = getMemberIdandNameBycellphone(phone)
    if infolist is not None:
        memberid = infolist[0]
        if memberid != '' and memberid is not None:
            delworkorder_forstage(memberid)
            delfor_stage_audit(memberid)

            # 风控增加社会信息
            delrisk_baseinfo(memberid)

            # 达分期授信
            delsocial_info(memberid)

            # 达分期相关订单信息

            # 达分期订单审核表
            delworkorder_forstage_order(memberid)

            # 达分期首付表
            deldown_payment(memberid)

            # 达分期，还款单表
            dellive_repay(memberid)

            # 达分期订单
            delforstage_order(memberid)

            delusercommit(memberid)

        else:
            return "该用户未实名"
        return "已删除该用户达分期信息"
    else:
        return "该手机号未查到用户信息"



if __name__ == '__main__':
    try:
        delCredit('18006782508')
        # delAuth('18006782508')
        delBankCard1('18006782508')
        #delAuth('15726940779')
        #delmmh_credit_audit('100001470054')
        #print("删除用户授信及绑卡完成")
        #print(getMemberAccount('11083251997758115840'))

        #print(q)
        #print(getout_account('11087984954045550592'))
        #print(getMemberIdandNameBycellphone('18006782508'))

    except Error as e:
        print(e)

    # except(RuntimeError, TypeError, NameError):
    #     pass
    #delPayPSWSet('18058198172')