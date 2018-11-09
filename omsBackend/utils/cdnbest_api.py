# -*- coding: utf-8 -*-
# author: timor
# desc: cdnbest 黑白名单设置

import datetime
import time
from hashlib import md5

import requests


class CDNBEST(object):
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
        token_e_time = datetime.datetime.now()
        print("token_e_time: %s" % token_e_time)
        print("token_s_time: %s" % self.token_s_time)

        data = {
            'uid': self.uid,
            'vhost': self.vhost,
            'token': self.__token
        }

        if __data != None:
            data.update(**__data)

        # 传入data参数字典，data为None 则方法为get，有date为post方法
        if method == 'GET':
            req = requests.get(url, data=data, headers=self.__header, verify=False)
        elif method == 'POST':
            req = requests.post(url, data=data)
        elif method == 'PUT':
            req = requests.put(url, data=data, headers=self.__header, verify=False)
        elif method == 'DELETE':
            req = requests.delete(url, data=data, headers=self.__header, verify=False)
        else:
            return {'msg': 'router method not match!'}

        try:
            return req.json()
        except:
            return req.json()

    def getSiteinfo(self):
        """
        获得域名
        :return:
        """
        method = 'GET'
        url = self.api_url + 'site/list'
        req = self.http_request(method, url)
        return req

    def getFirewall(self):
        """
        获取防火墙配置
        :return:
        """
        method = 'GET'
        url = self.api_url + 'firewall'
        req = self.http_request(method, url)
        if req:
            return req['rows']
        else:
            return req

    def getFirewallWhiteips(self):
        """
        获取白名单ips
        :return:
        """
        req = self.getFirewall()
        hasWrite = False
        for res in req:
            if res['name'] == 'cc-white-ips':
                return [res]

        if not hasWrite:
            return []

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
        删除白名单ips
        :param id: 1
        :return:
        """
        method = 'DELETE'
        url = self.api_url + 'firewall/whiteips'
        data = {
            "id": id
        }
        return self.http_request(method, url, data)

    def getFirewallBlackips(self):
        """
        获取白名单ips
        :return:
        """
        req = self.getFirewall()
        blackips = []
        for res in req:
            if res['name'] == 'blackip':
                blackips.append(res)

        return blackips

    def postFirewallBlackip(self, ips):
        """
        添加/修改白名单ips
        :param ips: 127.0.0.1|127.0.0.0/24|127.0.0.1-127.0.0.255
        :return:
        """
        method = 'POST'
        url = self.api_url + 'firewall/blackip'
        data = {
            "ip": ips
        }
        return self.http_request(method, url, data)

    def putFirewallBlackip(self, id, ips):
        """
        添加/修改白名单ips
        :param id: 1
        :param ips: 127.0.0.1|127.0.0.0/24|127.0.0.1-127.0.0.255
        :return:
        """
        method = 'PUT'
        url = self.api_url + 'firewall/blackip'
        data = {
            "id": id,
            "ip": ips
        }
        return self.http_request(method, url, data)

    def deleteFirewallBlackip(self, id):
        """
        删除白名单ips
        :param id: 1
        :return:
        """
        method = 'DELETE'
        url = self.api_url + 'firewall/blackip'
        data = {
            "id": id
        }
        return self.http_request(method, url, data)


if __name__ == '__main__':
    uid = 1001
    vhost = "itgo88001"
    cdn = CDNBEST(uid, vhost)
    # print(cdn.getFirewall())
    # 白名单
    # print(cdn.postFirewallWhiteips(1, ''))
    # print(cdn.deleteFirewallWhiteips(1))
    # print(cdn.getFirewallWhiteips())
    # 黑名单
    # print(cdn.getFirewallBlackips())
    # print(cdn postFirewallBlackip('4.4.4.4'))
    # print(cdn.putFirewallBlackip(1, '4.4.4.4|2.2.2.2'))
    # print(cdn.deleteFirewallBlackip(1))
