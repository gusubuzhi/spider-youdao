import json
import re
import urllib.request
from urllib import parse

import requests
import time
import random
import hashlib

def getsalt():
    salt = int(time.time()*1000) +random.randint(0,10)
    return salt

def getMD5(v):
    md5 = hashlib.md5()
    md5.update(v.encode('utf-8'))
    sign = md5.hexdigest()
    return sign

def getsign(key,salt):
    sign = 'fanyideskweb' + key + str(salt) + "ebSeFb%=XZ%T[KZ)c(sy!"
    sign = getMD5(sign)
    return sign

def youdao(key):
    salt = getsalt()
    data = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": str(salt),
        "sign": getsign(key,salt),
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }

    da = parse.urlencode(data).encode()
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": str(len(da)),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=1743889798@10.168.8.61; JSESSIONID=aaajmlxC700jEbyphUArw; OUTFOX_SEARCH_USER_ID_NCOO=1758633876.1657476; fanyi-ad-id=46607; fanyi-ad-closed=1; ___rl__test__cookies=1530530811624",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    req = requests.post(url, data=data, headers = headers)
    req.encoding = 'utf-8'
    html = req.json()
    trans = html['translateResult'][0][0]['tgt']

    try:
        tans_content = html['smartResult']['entries'][1]
    except KeyError:
        pass

    print("【%s】 翻译："%key, trans)

    try:
        print("【%s】 详情内容："%key, tans_content)
    except UnboundLocalError:
        pass

if __name__ == '__main__':
    while True:
        show = input("请输入要翻译的内容(有道翻译)>>")
        print("------------------------------")
        print()
        data = youdao(show)
        print("------------------------------")