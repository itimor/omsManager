# -*- coding: utf-8 -*-
# author: timor

import requests
import datetime
import time
from hashlib import md5
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class CDNAPI(object):
    def __init__(self, uid, t, vhost, sign, user_type='main'):
        if user_type == 'proxy':
            self.api_dir = 'https://www.cdnbest.com/api2/proxy/index.php/'
        else:
            self.api_dir = 'https://www.cdnbest.com/api2/user/index.php/'
        self.api_url = 'https://www.cdnbest.com/api2/site/index.php/'
        self.uid = uid
        self.t = t
        self.vhost = vhost
        self.sign = sign
        self.__header = dict()
        self.token_s_time = ''
        self.__token = self.get_token()

    def get_token(self):
        """
        登录获取token
        """
        self.__header["Accept"] = "application/x-www-form-urlencoded"
        data = {
            "uid": self.uid,
            "t": self.t,
            "vhost": self.vhost,
            "sign": self.sign
        }
        url = self.api_dir + 'token'
        print(data)
        print(url)
        req = requests.post(url, data=data, headers=self.__header, verify=False)
        try:
            token = req.json()
            self.token_s_time = datetime.datetime.now()
            return token
        except KeyError:
            raise KeyError

    # def http_request(self, url, data):
    #     """
    #     接收请求，返回结果
    #     """
    #     self.__header["Accept"] = "application/json"
    #     self.__header["Authorization"] = "Bearer " + self.__token
    #     token_e_time = datetime.datetime.now()
    #     print("token_e_time: %s" % token_e_time)
    #     print("token_s_time: %s" % self.token_s_time)
    #
    #     if (token_e_time - self.token_s_time).seconds > 4000:
    #         print("Bot token is Expired")
    #         self.get_token()
    #
    #     # 传入data参数字典，data为None 则方法为get，有date为post方法
    #     data["from"] = {"id": self.client_id}
    #     req = requests.post(url, json=data, headers=self.__header, verify=False)
    #     try:
    #         return req.json()
    #     except:
    #         print(req.content)


if __name__ == '__main__':
    t = str(int(time.time()))
    uid = 72910
    skey = "Wactat3CtTJxwwGT"
    m1 = md5()
    m2 = md5()
    m1.update((str(uid) + skey).encode(encoding='utf-8'))
    m2.update((m1.hexdigest() + t).encode(encoding='utf-8'))
    vhost = "itgocdn.com"
    user_type = 'proxy'
    cdn = CDNAPI(uid, t, vhost, m2.hexdigest())
    print(cdn.get_token())
