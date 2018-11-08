# -*- coding: utf-8 -*-
# author: timor

import datetime
import time
import urllib
from hashlib import md5

import requests


class CDNAPI(object):
    def __init__(self, uid, vhost):
        self.api_url = 'http://itgocdn.com/api2/site/index.php/'
        self.skey = "Wactat3CtTJxwwGT"
        self.uid = uid
        self.vhost = vhost
        self.__header = dict()
        self.__token = self.get_token()

    def get_token(self):
        """
        登录获取token
        """
        t = str(int(time.time()))
        m1 = md5()
        m2 = md5()
        m1.update((str(self.uid) + self.skey).encode(encoding='utf-8'))
        m2.update((m1.hexdigest() + t).encode(encoding='utf-8'))

        data = {
            "uid": self.uid,
            "t": t,
            "vhost": self.vhost,
            "sign": m2.hexdigest()
        }
        url = self.api_url + 'token'
        self.__header["Accept"] = "application/x-www-form-urlencoded"
        req = requests.post(url, data=data, headers=self.__header, verify=False)
        try:
            token = req.json()
            self.token_s_time = datetime.datetime.now()
            return token['token']
        except KeyError:
            raise KeyError

    def http_request(self, method, url, __data=None):
        """
        接收请求，返回结果
        """
        self.__header["Accept"] = "application/json"

        data = {
            'uid': self.uid,
            'vhost': self.vhost,
            'token': self.__token
        }

        if __data != None:
            data.update(**__data)

        params = urllib.parse.urlencode(data)
        # 传入data参数字典，data为None 则方法为get，有date为post方法
        if method == 'GET':
            req = requests.get(url, params=params)
        elif method == 'POST':
            req = requests.post(url, data=data, headers=self.__header, verify=False)
        elif method == 'PUT':
            req = requests.put(url, data=data, headers=self.__header, verify=False)
        elif method == 'DELETE':
            req = requests.delete(url, data=data, headers=self.__header, verify=False)
        else:
            return {'msg': 'router mathod not match!'}

        try:
            return req.json()
        except:
            return req.json()

    def getDomainList(self):
        """
        获得域名
        :return:
        """
        method = 'POST'
        url = self.api_url + 'domain/list'
        return self.http_request(method, url)

    def getFirewall(self):
        """
        获取防火墙配置
        :return:
        """
        method = 'GET'
        url = self.api_url + 'firewall'
        return self.http_request(method, url)

    def postFirewallWhiteips(self, id, ips):
        """
        添加/修改白名单ips
        :param id: 1
        :param ips: 1.1.1.1|2.2.2.2
        :return:
        """
        method = 'POST'
        url = self.api_url + 'firewall/whiteips'
        data = {
            "id": id,
            "ips": ips
        }
        return self.http_request(method, url, data)

    def deleteFirewallWhiteips(self, id):
        """
        删除白名单
        :param id: 1
        :return:
        """
        method = 'POST'
        url = self.api_url + 'firewall/whiteips'
        data = {
            "id": id
        }
        return self.http_request(method, url, data)


if __name__ == '__main__':
    uid = 1001
    vhost = "w8ikychrt.com"
    cdn = CDNAPI(uid, vhost)
    print(cdn.getDomainList())
