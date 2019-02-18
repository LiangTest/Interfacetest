import common
import json
import configHttp
import readConfig as readConfig

localReadConfig = readConfig.ReadConfig()
localConfigHttp = configHttp.ConfigHttp()
localLogin_xls = common.get_xls("userCase.xlsx", "login")
localAddAddress_xls = common.get_xls("userCase.xlsx", "addAddress")


# login
def login():
    """
    login
    :return: token
    """
    # set url
    url = common.get_url_from_xml('login')
    localConfigHttp.set_url(url)

    # set header
    token = localReadConfig.get_headers("token_v")
    header = {"token": token}
    localConfigHttp.set_header(header)

    # set param
    data = {"email": localLogin_xls[0][3],
            "password": localLogin_xls[0][4]}
    localConfigHttp.set_data(data)

    # login
    response = localConfigHttp.post().json()
    token = common.get_value_from_return_json(response, "member", "token")
    return token


# logout
def logout(token):
    """
    logout
    :param token: login token
    :return:
    """
    # set url
    url = common.get_url_from_xml('logout')
    localConfigHttp.set_url(url)

    # set header
    header = {'token': token}
    localConfigHttp.set_header(header)

    # logout
    localConfigHttp.get()


def getLoginCode():
    smsCode = ''
    url = '/app/User/verifyCode'
    try:
        localConfigHttp.set_url(url)  #初始化url
        data = {'phoneNumber':'15726940779'}
        data["type"] = "0"
        localConfigHttp.set_data(data)
        return_json = localConfigHttp.postWithSign()
        print('---------------------------')
        print(return_json.json())
        print('---------------------------')
        print(return_json.json()['resultCode'])
        print('---------------------------')
        json.dumps(return_json.json()['resultMessage'])

        print(return_json)
    # smsCode = return_json['resultCode']
    # print(smsCode)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    getLoginCode()

