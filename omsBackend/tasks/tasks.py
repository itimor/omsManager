# -*- coding: utf-8 -*-
# author: itimor

from celery import shared_task
from utils.sendskype import skype_bot
from utils.sendmail import send_mail
from dnsmanager.godaddy_api import GodaddyApi
from dnsmanager.models import DnsDomain


@shared_task
def send_to_skype(user, content):
    skype_bot(user, content)


@shared_task
def send_to_mail(to_list, cc_list, sub, content):
    send_mail(to_list, cc_list, sub, content)


@shared_task
def tty(x, y):
    print("123")


@shared_task
def post_godaddy_domain(key, secret, dnsname):
    dnsapi = GodaddyApi(key, secret)
    query = dnsapi.get_domains()
    for item in query:
        print(f'domain: {item}')
        dnsdomain = dict()
        dnsdomain['dnsname'] = dnsname
        dnsdomain['type'] = 'godaddy'
        dnsdomain['name'] = item['domain']
        DnsDomain.objects.update_or_create(name=dnsdomain['name'], defaults=dnsdomain)
