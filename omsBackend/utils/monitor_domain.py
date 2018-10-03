# -*- coding: utf-8 -*-
# author: kiven

import requests
import datetime


class OMSAPI(object):
    def __init__(self, api_url, username, password):
        self.api_url = api_url
        self.username = username
        self.password = password
        self.__header = dict()
        self.token_s_time = ''
        self.__token = self.get_token()

    def get_token(self):
        """
        登录获取token
        """
        self.__header["Accept"] = "application/json"
        data = {
            "username": self.username,
            "password": self.password
        }
        url = self.api_url + 'api-token-auth/'
        req = requests.post(url, data=data, headers=self.__header, verify=False)
        try:
            token = req.json()["token"]
            self.token_s_time = datetime.datetime.now()
            return token
        except KeyError:
            raise KeyError

    def get_request(self, url):
        """
        接收请求，返回结果
        """
        self.__header["Authorization"] = "ooxx " + self.__token
        token_e_time = datetime.datetime.now()
        print("token_e_time: %s" % token_e_time)
        print("token_s_time: %s" % self.token_s_time)

        if (token_e_time - self.token_s_time).seconds > 4000:
            print("token is Expired")
            self.get_token()

        req = requests.get(url, headers=self.__header)
        try:
            return req.json()
        except:
            print(req.content)

    def get_domains(self):
        url = self.api_url + 'dnsdomains/'
        content = self.get_request(url)
        try:
            return content
        except:
            return {'msg': 'send msg error'}


def count_expire(expire_time, safe_day=30):
    s_day = datetime.datetime.now()
    d_day = datetime.datetime.strptime(expire_time, '%Y-%m-%d')
    d_diff = (d_day - s_day).days
    if d_diff < safe_day:
        return True
    else:
        return False


if __name__ == '__main__':
    url = 'http://127.0.0.1:8000/api/'
    username = "admin"
    password = "qwert@12345"
    oms = OMSAPI(url, username, password)
    domains = oms.get_domains()
    expire_domains = []
    for domain in domains:
        if count_expire(domain['expire_time']):
            print(f'{domain["name"]} expire')
            expire_domains.append(domain)
        else:
            print(f'{domain["name"]} ok')

        import time
        time.sleep(1)

    print(expire_domains)
