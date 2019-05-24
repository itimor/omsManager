# -*- coding: utf-8 -*-
# author: timor

import requests
import json
from datetime import datetime, timedelta


def whois(domain):
    url = "https://whois.tt80.xin/whoisapi?domain=%s" % domain
    html = requests.get(url, verify=False).content
    try:
        d = json.loads(html)
    except:
        return {"create_time": datetime.date(), "expire_time": datetime.date(), "dnsService": 'invalid.domain'}
    if d['code'] < 0:
        create_time = datetime.date()
        expire_time = datetime.date()
        dnsService = 'invalid.domain'
    else:
        create_time = datetime.strptime(d["creationTime"][:10], "%Y-%m-%d") + timedelta(hours=8)
        expire_time = datetime.strptime(d["expiryTime"][:10], "%Y-%m-%d") + timedelta(hours=8)
        dnsService = d["domainnNameServer"]

    return {"create_time": create_time, "expire_time": expire_time, "dnsService": dnsService}


if __name__ == 'main':
    print(whois('agapi.mobi'))