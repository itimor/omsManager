# -*- coding: utf-8 -*-
# author: kiven

import requests
import json
from datetime import datetime, timedelta


def whois(domain):
    url = "https://whois.tt80.xin/whoisapi?domain=%s" % domain
    html = requests.get(url, verify=False).text
    d = json.loads(html)
    if not d:
        create_time = datetime.now()
        expire_time = datetime.now()
        dnsService = 'www.kiven.cn'
    else:
        create_time = datetime.strptime(d["creationTime"],
                                        get_time_format(d["creationTime"])) + timedelta(
            hours=8)
        expire_time = datetime.strptime(d["expiryTime"],
                                        get_time_format(d["expiryTime"])) + timedelta(
            hours=8)
        dnsService = d["domainnNameServer"]

    return {"create_time": create_time, "expire_time": expire_time, "dnsService": dnsService}


def get_time_format(time):
    if len(time) > 19:
        TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
    else:
        TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

    return TIME_FORMAT


if __name__ == '__main__':
    print(whois('kiven.com'))
