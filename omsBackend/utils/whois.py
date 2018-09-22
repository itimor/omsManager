# -*- coding: utf-8 -*-
# author: kiven

import requests
import json
from datetime import datetime, timedelta


def whois(domain):
    url = "http://whois.xinnet.com/php/domain_seo.php?domain=%s" % domain
    html = requests.get(url).text
    d = json.loads(html)
    if d["whoisFlag"] == 'false':
        create_time = datetime.now()
        expire_time = datetime.now()
        dnsService = 'www.kiven.cn'
    else:
        create_time = datetime.strptime(d["whois_registrantDate"],
                                        get_time_format(d["whois_registrantDate"])) + timedelta(
            hours=8)
        expire_time = datetime.strptime(d["whois_expirationDate"],
                                        get_time_format(d["whois_expirationDate"])) + timedelta(
            hours=8)
        dnsService = '|'.join(d["whois_dnsService"])

    return {"create_time": create_time, "expire_time": expire_time, "dnsService": dnsService}


def get_time_format(time):
    if len(time) > 19:
        TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
    else:
        TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

    return TIME_FORMAT


if __name__ == '__main__':
    print(whois('kiven.com'))
