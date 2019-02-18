import base64
import rsa
from Crypto.PublicKey import RSA
from base64 import b64decode, b64encode
from Crypto.Cipher import PKCS1_v1_5, PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
rsaPublicKeyString = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCbubAkC7qs1eQItadNIG5+6uFJ88nnCNxWQVdFMilt3hiTsD2wK9+xn1lgxGYlCfPBWHtYqo8dNInqisY/BBVt5mgAAM0EmITHZO37Q6/w/eJT0ACyhEP0AB3OPzlw9Q88l4CRQjKsMsRBkJaDHAz4W9SXLWQM8xAm/5giO9ZInwIDAQAB"

def str_To_Key(s):
    d_str = base64.b64decode(s)  #对字符串进行解码
    if len(d_str) < 162:
        return False

    hex_str = ''

    for x in d_str:

        h = hex(x)[2:]
        h = h.rjust(2, '0')

        hex_str += h


    # 找到模数和指数的开头结束位置
    m_start = 29 * 2
    e_start = 159 * 2
    m_len = 128 * 2
    e_len = 3 * 2

    modulus = hex_str[m_start:m_start + m_len]
    exponent = hex_str[e_start:e_start + e_len]
    return modulus,exponent


def modpow(b, e, m):
    result = 1
    while (e > 0):
        if e & 1:
            result = (result * b) % m
        e = e >> 1
        b = (b * b) % m
    return result

def str_to_int(string):
    n = 0
    for i in range(len(string)):
        n = n << 8
        n += ord(string[i])
    return n


def getRSA(message):
    # key = str_To_Key(rsaPublicKeyString)
    # print(key)
    # modulus = int(key[0], 16)
    # exponent = int(key[1], 16)
    modulus = int('30819f300d06092a864886f70d010101050003818d00308189028181009bb9b0240bbaacd5e408b5a74d206e7eeae149f3c9e708dc5641574532296dde1893b03db02bdfb19f5960c4662509f3c1587b58aa8f1d3489ea8ac63f04156de6680000cd049884c764edfb43aff0fde253d000b28443f4001dce3f3970f50f3c9780914232ac32c4419096831c0cf85bd4972d640cf31026ff98223bd6489f0203', 16)
    exponent = int('010001', 16)
    rsa_pubkey = rsa.PublicKey(modulus, exponent)
    print(rsa_pubkey)
    crypto = rsa.encrypt(message, rsa_pubkey)
    b64str = base64.b64encode(crypto)

    return b64str

if __name__ == '__main__':
    mess
    s = getRSA('123456')
    print(type(s))
    print(s)
