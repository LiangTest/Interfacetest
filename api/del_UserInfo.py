from flask import Flask,jsonify,request
from api import delUserInfo
from api import sendSMSCode,getAccessToken
from api import dbManager

app = Flask(__name__)#创建一个服务，赋值给APP


'''删除用户信息'''
@app.route('/del_uinfo',methods=['get'])#指定接口访问的路径，支持什么请求方式get，post

#请求后直接拼接入参方式
def del_user():
    phone = request.args.get('phone')#使用request.args.get方式获取拼接的入参数据
    if any(phone):  # 判断请求传入的参数是否在字典里
        return delUserInfo.delUserInfo(phone)
    #如果在的话，则返回data对应key的值转成的json串信息
    else:
        return jsonify({'status': 9999,'msg': '参数phon请传入正确手机号'})
    #如果不在的话，返回err对应key的value转成的json串信息


'''获取登录验证码'''
@app.route('/get_login_code',methods=['get'])#指定接口访问的路径，支持什么请求方式get，post

def get_login_code():
    phone = request.args.get('phone')#使用request.args.get方式获取拼接的入参数据
    if any(phone):  # 判断请求传入的参数是否在字典里
        return sendSMSCode.send_Login_Code(phone)
    #如果在的话，则返回data对应key的值转成的json串信息
    else:
        return jsonify({'status': 9999,'msg': '参数phon请传入正确手机号'})


'''获取注册验证码'''
@app.route('/get_register_code',methods=['get'])#指定接口访问的路径，支持什么请求方式get，post

def get_register_code():
    phone = request.args.get('phone')#使用request.args.get方式获取拼接的入参数据
    if any(phone):  # 判断请求传入的参数是否在字典里
        return sendSMSCode.send_Register_Code(phone)
    #如果在的话，则返回data对应key的值转成的json串信息
    else:
        return jsonify({'status': 9999,'msg': '参数phon请传入正确手机号'})


'''删除银行卡信息，包括实名信息'''
@app.route('/del_bankcard',methods=['get'])#指定接口访问的路径，支持什么请求方式get，post

#请求后直接拼接入参方式
def del_bankcard():
    phone = request.args.get('phone')#使用request.args.get方式获取拼接的入参数据
    if any(phone):  # 判断请求传入的参数是否在字典里
        return delUserInfo.delBankCard(phone)
    #如果在的话，则返回data对应key的值转成的json串信息
    else:
        return jsonify({'status': 9999,'msg': '参数phon请传入正确手机号'})
    #如果不在的话，返回err对应key的value转成的json串信息


'''删除实名信息'''
@app.route('/del_auth',methods=['get'])#指定接口访问的路径，支持什么请求方式get，post

#请求后直接拼接入参方式
def del_auth():
    phone = request.args.get('phone')#使用request.args.get方式获取拼接的入参数据
    if any(phone):  # 判断请求传入的参数是否在字典里
        return delUserInfo.delAuth(phone)
    #如果在的话，则返回data对应key的值转成的json串信息
    else:
        return jsonify({'status': 9999,'msg': '参数phon请传入正确手机号'})
    #如果不在的话，返回err对应key的value转成的json串信息


'''只删除银行卡'''
@app.route('/del_bankcard1',methods=['get'])#指定接口访问的路径，支持什么请求方式get，post

#请求后直接拼接入参方式
def del_bankcard1():
    phone = request.args.get('phone')#使用request.args.get方式获取拼接的入参数据
    if any(phone):  # 判断请求传入的参数是否在字典里
        return delUserInfo.delBankCard1(phone)  #仅仅删除银行卡
    #如果在的话，则返回data对应key的值转成的json串信息
    else:
        return jsonify({'status': 9999,'msg': '参数phon请传入正确手机号'})

'''通过姓名删除银行卡'''
@app.route('/del_bankcard_by_name',methods=['get'])#指定接口访问的路径，支持什么请求方式get，post

#请求后直接拼接入参方式
def del_bankcard_by_name():
    name = request.args.get('name')#使用request.args.get方式获取拼接的入参数据
    if any(name):  # 判断请求传入的参数是否在字典里
        return delUserInfo.delBankCard2(name)  #仅仅删除银行卡
    #如果在的话，则返回data对应key的值转成的json串信息
    else:
        return jsonify({'status': 9999,'msg': '参数name请传入正确姓名'})


'''登录并获取token'''
@app.route('/login_Get_AccessToken',methods=['get'])#指定接口访问的路径，支持什么请求方式get，post

#请求后直接拼接入参方式
def login_Get_AccessToken():
    phone = request.args.get('phone')#使用request.args.get方式获取拼接的入参数据
    if any(phone):  # 判断请求传入的参数是否在字典里
        user_info = getAccessToken.loginToGetAccessToken(phone)
        return jsonify({'status': 0000,'phone':phone ,'memberId':user_info['memberId'],'accessToken': user_info['accessToken']})
    #如果在的话，则返回data对应key的值转成的json串信息
    else:
        return jsonify({'status': 9999,'msg': '参数phon请传入正确手机号'})

'''获取token'''
@app.route('/get_Token',methods=['get'])#指定接口访问的路径，支持什么请求方式get，post

#请求后直接拼接入参方式
def get_AccessToken():
    phone = request.args.get('phone')#使用request.args.get方式获取拼接的入参数据
    if any(phone):  # 判断请求传入的参数是否在字典里
        user_info = getAccessToken.getToken(phone)
        if 'accessToken' in user_info:
            return jsonify({'status': 0000,'phone':phone ,'memberId':user_info['memberId'],'accessToken': user_info['accessToken']})
    #如果在的话，则返回data对应key的值转成的json串信息
        else:
            return jsonify({'status': 1111,'msg':user_info['msg'] })
    else:
        return jsonify({'status': 9999,'msg': '参数phon请传入正确手机号'})


'''获取短信验证码'''
@app.route('/get_sms_code',methods=['get'])#指定接口访问的路径，支持什么请求方式get，post

def get_sms_code():
    phone = request.args.get('phone')#使用request.args.get方式获取拼接的入参数据
    if any(phone):  # 判断请求传入的参数是否在字典里
        res=dbManager.getVerifyCode(phone)
        if 'code' in res:
            return jsonify({'status': 0000,'phone':phone ,'code':res['code']})
        #如果在的话，则返回data对应key的值转成的json串信息
        else:
            return jsonify({'status': 9999,'msg':res['msg'] })

'''获取信用生活发的短信验证码'''
@app.route('/get_verify_code',methods=['get'])#指定接口访问的路径，支持什么请求方式get，post

def getverifycode():
    phone = request.args.get('phone')#使用request.args.get方式获取拼接的入参数据
    if any(phone):  # 判断请求传入的参数是否在字典里
        res=delUserInfo.get_verify_code(phone)
        if 'code' in res:
            return jsonify({'status': 0000,'phone':phone ,'code':res['code']})
        #如果在的话，则返回data对应key的值转成的json串信息
        else:
            return jsonify({'status': 1111,'msg':res['msg'] })


    #如果在的话，则返回data对应key的值转成的json串信息
    else:
        return jsonify({'status': 9999,'msg': '参数phon请传入正确手机号'})

'''通过姓名删除信用账户相关信息'''
@app.route('/del_all_account_by_name',methods=['get'])#指定接口访问的路径，支持什么请求方式get，post

#请求后直接拼接入参方式
def del_all_account_by_name():
    phone = request.args.get('phone')#使用request.args.get方式获取拼接的入参数据
    if any(phone):  # 判断请求传入的参数是否在字典里
        msg = delUserInfo.del_all_account(phone)
        return jsonify({'status': 0000,'msg': msg})
    #如果在的话，则返回data对应key的值转成的json串信息
    else:
        return jsonify({'status': 9999,'msg': '参数name请传入正确手机号'})

'''删除用户信息'''
@app.route('/del_forstage',methods=['get'])#指定接口访问的路径，支持什么请求方式get，post

#请求后直接拼接入参方式
def del_forstage():
    phone = request.args.get('phone')#使用request.args.get方式获取拼接的入参数据
    if any(phone):  # 判断请求传入的参数是否在字典里
        return delUserInfo.delforstage(phone)
    #如果在的话，则返回data对应key的值转成的json串信息
    else:
        return jsonify({'status': 9999,'msg': '参数phon请传入正确手机号'})
    #如果不在的话，返回err对应key的value转成的json串信息


app.run(host='0.0.0.0',port=8802,debug=True)
#这个host：windows就一个网卡，可以不写，而liux有多个网卡，写成0:0:0可以接受任意网卡信息
#通过访问127.0.0.1:8802/get_user，form—data里输入username参数，则可看到返回信息