# -*- coding: utf-8 -*-
# author: timor
# desc: greycdn 黑白名单设置

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class GREYCDN(object):
    def __init__(self):
        self.api_url = 'https://api.greypanel.com'
        self.username = 'B2B.OMaws@gmail.com'
        self.password = 'abcd1234'
        self.__header = dict()
        self.sid = self.login()

    def login(self):
        """
        登录获取sid
        """
        data = {
            "username": self.username,
            "password": self.password
        }
        url = self.api_url + '/api/login'
        self.__header["Content-Type"] = "application/x-www-form-urlencoded"
        req = requests.post(url, data=data, headers=self.__header, verify=False)
        try:
            token = req.json()
            self.__header["Cookie"] = 'sid=' + token['result']
            return token['result']
        except KeyError:
            raise KeyError

    def http_request(self, method, url, post_data=None):
        """
        接收请求，返回结果
        """
        print(url)
        print(self.__header)
        data = {}

        if post_data is not None:
            data.update(**post_data)

        # 传入data参数字典，data为None 则方法为get，有date为post方法
        if method == 'GET':
            req = requests.get(url, headers=self.__header, verify=False)
        elif method == 'POST':
            req = requests.post(url, data=data)
        else:
            return {'msg': 'router method not match!'}

        try:
            return req.json()
        except:
            return req.json()

    def getSites(self):
        """
        获得域名
        :return:
        """
        method = 'GET'
        url = self.api_url + '/api/site/find-sites' + '?keyWord=&page=1&pageSize=50'
        req = self.http_request(method, url)
        return req['result']['content']

    def getWhiteips(self, siteUid):
        """
        获取防火墙配置
        :return:
        """
        method = 'GET'
        url = self.api_url + '/api/site/find-white-ip' + '?siteUid=' + siteUid
        req = self.http_request(method, url)
        if req:
            return req['result']
        else:
            return req

    def putWhiteips(self, siteUid, whiteIps):
        """
        获取防火墙配置
        :return:
        """
        method = 'POST'
        url = self.api_url + '/api/site/modify-white-ip'
        data = {
            "siteUid": siteUid,
            "whiteIps": whiteIps
        }
        req = self.http_request(method, url, data)
        if req:
            return req
        else:
            return req


if __name__ == '__main__':
    cdn = GREYCDN()
    siteUid = 'b6358e98-5096-4530-8c80-fc799600965d'
    # print(cdn.getSites())
    # print(cdn.getWhiteips(siteUid))
    whiteIps = '127.0.0.1'
    print(cdn.putWhiteips(siteUid, whiteIps))
