# -*- coding: utf-8 -*-
# author: Toby
# e-mail: toby@e-veb.com

import requests
import xml.sax.handler


class RequestsException(Exception):
    def __init__(self, err="Unable to open URL"):
        Exception.__init__(self, err)


class DataException(RequestsException):
    def __init__(self, err="Unable to request data"):
        RequestsException.__init__(self, err)


class XMLHandler(xml.sax.handler.ContentHandler):
    """解析xml原始数据"""
    def __init__(self):
        self.data_list = []

    def characters(self, data):
        self.data_list.append(data)


class NameSiloApi:
    def __init__(self, key, secret):
        """
        :param urls: API的URL
        :param keys: 用于验证的key
        """
        self.url = 'https://www.namesilo.com/api'
        self.params = {'version': '1', 'type': 'xml', 'key': secret}
        self.xh = XMLHandler()

    def _request_api_data(self, operating):
        """
        基于不同的操作，请求原始xml数据
        :param operating: 操作
        :return: 原始xml数据
        """
        try:
            return requests.get("{}/{}".format(self.url, operating), params=self.params).content
        except requests.exceptions.ConnectionError:
            raise RequestsException

    def _parsing(self, raw_xml_data):
        """
        接受xml原始数据并传递给xml解析类（XMLHandler）
        :param raw_xml_data: xml原始数据
        """
        try:
            xml.sax.parseString(raw_xml_data, self.xh)
        except Exception:
            raise DataException

    def get_domains(self):
        """
        获取所有活动域名列表
        :return: 原始xml数据
        """
        raw_xml_data = self._request_api_data('listDomains')
        if not raw_xml_data:
            raise DataException
        self._parsing(raw_xml_data)  # 解析xml
        already_parsed_data = self.xh.data_list  # 得到解析后的数据
        summary = []
        try:
            for i in range(len(already_parsed_data)):
               summary.append(dict(domain=already_parsed_data[i+4]))
        except IndexError:
            return summary

    def get_domain_info(self, domain_name):
        """
        获取域名信息
        :param domain_name: 域名
        :return: 原始xml数据
        """
        self.params['domain'] = domain_name
        raw_xml_data = self._request_api_data('getDomainInfo')
        if not raw_xml_data:
            raise DataException
        self._parsing(raw_xml_data)  # 解析xml
        already_parsed_data = self.xh.data_list  # 得到解析后的数据
        for i in range(len(already_parsed_data)):
            summary = dict(
                ip=already_parsed_data[1],
                created=already_parsed_data[4],
                expires=already_parsed_data[5],
                status=already_parsed_data[6],
                locked=already_parsed_data[7],
                private=already_parsed_data[8],
                auto_renew=already_parsed_data[9],
                traffic_type=already_parsed_data[10],
                email_verification_required=already_parsed_data[11],
            )
            return summary


if __name__ == '__main__':
    secret = "d4efac6c29fa9ac6b77d2cc"

    n = NameSiloApi(1, secret)
    dt1 = n.get_domains()
    print(dt1)
