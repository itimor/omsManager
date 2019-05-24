# -*- coding: utf-8 -*-
# author: itimor

from celery import shared_task
from utils.sendskype import skype_bot
from utils.sendmail import send_mail
from dnsmanager.godaddy_api import GodaddyApi
from dnsmanager.namesilo_api import NameSiloApi
from dnsmanager.models import DnsDomain
from datetime import datetime, timedelta

@shared_task
def send_to_skype(user, content):
    skype_bot(user, content)


@shared_task
def send_to_mail(to_list, cc_list, sub, content):
    send_mail(to_list, cc_list, sub, content)


@shared_task
def post_godaddy_domain(key, secret, dnsname):
    dnsapi = GodaddyApi(key, secret)
    query = dnsapi.get_domains()
    query_domains = []
    for item in query:
        if item['status'] == 'ACTIVE':
            from time import sleep
            sleep(1)
            print(f'sync_domain: {item}')
            dnsdomain = dict()
            dnsdomain['dnsname'] = dnsname
            dnsdomain['type'] = 'godaddy'
            dnsdomain['name'] = item['domain']
            dnsdomain['expire_time'] = datetime.strptime(item['expires'][:10], "%Y-%m-%d") + timedelta(hours=8)
            DnsDomain.objects.update_or_create(name=dnsdomain['name'], defaults=dnsdomain)

            # 把api查询出来的域名放入列表中
            query_domains.append(dnsdomain['name'])

    # 把数据库查询出来的域名放入列表中
    db_domains = DnsDomain.objects.filter(dnsname=dnsname).values("name")

    # 两两对比，得到需要删除的列表
    delete_domains = [domain['name'] for domain in db_domains if domain['name'] not in query_domains]
    print(f'delete_domains: {delete_domains}')

    # 循环列表并删除
    for domain in delete_domains:
        DnsDomain.objects.filter(dnsname=dnsname, name=domain).delete()


@shared_task
def post_namesilo_domain(key, secret, dnsname):
    dnsapi = NameSiloApi(key, secret)
    query = dnsapi.get_domains()
    query_domains = []
    for item in query:
        domain_info = dnsapi.get_domain_info(item['domain'])
        if domain_info['status'] == 'Active':
            from time import sleep
            sleep(1)
            print(f'sync_domain: {item}')
            dnsdomain = dict()
            dnsdomain['dnsname'] = dnsname
            dnsdomain['type'] = 'namesilo'
            dnsdomain['name'] = item['domain']
            dnsdomain['expire_time'] = datetime.strptime(domain_info['expires'][:10], "%Y-%m-%d") + timedelta(hours=8)
            DnsDomain.objects.update_or_create(name=dnsdomain['name'], defaults=dnsdomain)

            # 把api查询出来的域名放入列表中
            query_domains.append(dnsdomain['name'])

    # 把数据库查询出来的域名放入列表中
    db_domains = DnsDomain.objects.filter(dnsname=dnsname).values("name")

    # 两两对比，得到需要删除的列表
    delete_domains = [domain['name'] for domain in db_domains if domain['name'] not in query_domains]
    print(f'delete_domains: {delete_domains}')

    # 循环列表并删除
    for domain in delete_domains:
        DnsDomain.objects.filter(dnsname=dnsname, name=domain).delete()
