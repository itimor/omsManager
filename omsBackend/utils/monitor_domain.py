# -*- coding: utf-8 -*-
# author: kiven

import requests
import datetime
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


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


# 判断过期时间
def count_expire(expire_time, safe_day=30):
    s_day = datetime.datetime.now()
    d_day = datetime.datetime.strptime(expire_time, '%Y-%m-%d')
    d_diff = (d_day - s_day).days
    if 1 < d_diff < safe_day:
        return True
    else:
        return False


# 发送邮件函数
def send_mail(MAIL_ACOUNT, to_list, sub, content):
    me = MAIL_ACOUNT["mail_user"] + "<" + MAIL_ACOUNT["mail_user"] + "@" + MAIL_ACOUNT["mail_postfix"] + ">"
    msg = MIMEMultipart('alternative')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = to_list
    context = MIMEText(content, _subtype='html', _charset='utf-8')  # 解决乱码
    msg.attach(context)
    try:
        smtpserver = smtplib.SMTP(MAIL_ACOUNT["mail_host"], 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.login(MAIL_ACOUNT["mail_user"], MAIL_ACOUNT["mail_pass"])
        print("successful login")
        smtpserver.sendmail(me, to_list, msg.as_string())
        smtpserver.close()
        return {"code": 'success', "msg": "通知邮件发送成功"}
    except Exception as e:
        print(e)
        return {"code": 'error', "msg": "通知邮件发送失败"}


if __name__ == '__main__':
    url = 'http://oms.e-veb.info/api/'
    username = "admin"
    password = "qwert@12345"
    oms = OMSAPI(url, username, password)
    domains = oms.get_domains()
    expire_domains = []
    for domain in domains:
        if count_expire(domain['expire_time']):
            print('{} expire'.format(domain["name"]))
            expire_domains.append({"name": domain["name"], "expire_time": domain["expire_time"], "type": domain["type"],
                                   "account": domain["dnsname"]})
        else:
            print('{} ok'.format(domain["name"]))

    # 发送邮件
    MAIL_ACOUNT = {
        "mail_host": "smtp.gmail.com",
        "mail_user": "server@e-veb.com",
        "mail_pass": "ouci4fae3Oow9vohZoh7o",
        "mail_postfix": "e-veb.com",
    }
    to_list = 'server@e-veb.com'
    sub = '过期域名'
    if expire_domains:
        print(send_mail(MAIL_ACOUNT, to_list, sub, json.dumps(expire_domains)))
    else:
        print("not found will expire domains")
