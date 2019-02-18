import urllib.parse
from api import getVerifyCode


class Testt:
    def __init__(self):
        pass
    #构造一个编码函数，对一个字符串进行编码，返回编码后的字符串
    def percentEncode(p):
        p=str(p)
        res = urllib.parse.quote(p.encode('utf8'), '')
        print(res)
        print(type(res))
        res = res.replace('+', '%20')
        res = res.replace('*', '%2A')
        res = res.replace('%7E', '~')
        return res

if __name__ == "__main__":
    #print("ConfigHTTP")
    # test1 = Testt
    # sign = ''
    # dic = {"abc":123,"b&c":"23","c/d&e":"xxx"}
    # #由于签名要求唯一性，包括顺序，所以需要按照参数名称排序
    # sortedD = sorted(dic.items(), key=lambda x: x[0])  # 先通过 dic.items() 转化为 List, 然后利用 sorted 方式按照 key 排序
    # if dic is not None:
    #     for k,v in sortedD:
    #         sign += test1.percentEncode(k) + '=' +test1.percentEncode(v)+'&'
    #     if sign[-1]=='&':
    #         sign=sign[:-1]
    #         print(sign)
    # m = hashlib.md5()
    # sign = m.update(sign.encode('utf8'))
    # print(m.hexdigest())

    s = getVerifyCode.GetVerifyCode.getVerifyCode("15726940779")
    print(s)
