# -*- coding: utf-8 -*-
# author: kiven

from django.db import models
from django.utils import timezone

Dns_Types = {
    'godaddy': 'godaddy',
    'dnspod': 'dnspod',
    'namesilo': 'namesilo',
}


class DnsApiKey(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name=u'名称')
    key = models.CharField(max_length=201, verbose_name=u'api_key')
    secret = models.CharField(max_length=201, verbose_name=u'api_secret')
    type = models.CharField(choices=Dns_Types.items(), default='godaddy', max_length=10, verbose_name=u'类型')
    desc = models.TextField(null=True, blank=True, verbose_name=u'备注')

    def __str__(self):
        return self.name


Dns_Status = {
    0: '使用中',
    1: '备用',
    2: '被墙',
}


class DnsDomain(models.Model):
    title = models.CharField(max_length=200, unique=True, null=True, blank=True, verbose_name=u'记录名')
    dnsname = models.CharField(max_length=20, verbose_name=u'归属dns')
    name = models.CharField(max_length=20, verbose_name=u'名称')
    dnsService = models.CharField(max_length=200, null=True, blank=True, verbose_name=u'dns服务商')
    type = models.CharField(choices=Dns_Types.items(), default='godaddy', max_length=10, verbose_name=u'类型')
    create_time = models.DateField(default=timezone.now, verbose_name=u'创建时间')
    expire_time = models.DateField(default=timezone.now, verbose_name=u'过期时间')
    desc = models.TextField(null=True, blank=True, verbose_name=u'备注')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        from utils.whois import whois
        domain_info = whois(self.name)
        self.create_time = domain_info["create_time"]
        self.expire_time = domain_info["expire_time"]
        self.dnsService = domain_info["dnsService"]
        self.title = '{}-{}'.format(self.type, self.name)
        super(DnsDomain, self).save(*args, **kwargs)


class DnsRecord(models.Model):
    title = models.CharField(max_length=200, unique=True, null=True, blank=True, verbose_name=u'记录名')
    domain = models.ForeignKey(DnsDomain, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=u'域名')
    name = models.CharField(max_length=20, verbose_name=u'名称')
    status = models.CharField(choices=Dns_Status.items(), default=0, max_length=1, verbose_name=u'状态')
    type = models.CharField(default='A', max_length=10, verbose_name=u'类型')
    value = models.CharField(max_length=300, verbose_name=u'值')
    value2 = models.CharField(max_length=50, null=True, blank=True, verbose_name=u"备用记录值")
    ttl = models.IntegerField(default=600, verbose_name=u'ttl')
    record_id = models.CharField(max_length=11, null=True, blank=True, verbose_name=u'record_id')
    use = models.TextField(null=True, blank=True, verbose_name=u'用途')
    tan = models.BooleanField(default=False, verbose_name=u"是否探测")
    desc = models.TextField(null=True, blank=True, verbose_name=u'备注')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = '{}-{}-{}-{}'.format(self.domain, self.name, self.type, self.value)
        super(DnsRecord, self).save(*args, **kwargs)
