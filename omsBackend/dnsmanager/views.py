# -*- coding: utf-8 -*-
# author: timor

from rest_framework import viewsets
from rest_framework.response import Response
from dnsmanager.models import DnsApiKey, DnsDomain, DnsRecord
from dnsmanager.serializers import DnsApiKeySerializer, DnsDomainSerializer, DnsRecordSerializer, CustomDomainSerializer
from dnsmanager.godaddy_api import GodaddyApi
from dnsmanager.namesilo_api import NameSiloApi
from tasks.tasks import post_godaddy_domain, post_namesilo_domain


class DnsApiKeyViewSet(viewsets.ModelViewSet):
    queryset = DnsApiKey.objects.all()
    serializer_class = DnsApiKeySerializer
    filter_fields = ['name']


class DnsDomainViewSet(viewsets.ModelViewSet):
    queryset = DnsDomain.objects.all().order_by('-expire_time')
    serializer_class = DnsDomainSerializer
    filter_fields = ['name']
    search_fields = ['name']


class DnsRecordViewSet(viewsets.ModelViewSet):
    queryset = DnsRecord.objects.all()
    serializer_class = DnsRecordSerializer
    filter_fields = ['name', 'type', 'domain__name']
    search_fields = ['name']


class GodaddyDomainViewSet(viewsets.ViewSet):
    serializer_class = CustomDomainSerializer

    def list(self, request):
        dnsinfo = DnsApiKey.objects.get(name=request.GET['dnsname'])
        dnsapi = GodaddyApi(dnsinfo.key, dnsinfo.secret)
        query = dnsapi.get_domains()
        serializer = CustomDomainSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        dnsname = request.data['dnsname']
        dnsinfo = DnsApiKey.objects.get(name=dnsname)
        # post_godaddy_domain.delay(dnsinfo.key, dnsinfo.secret, dnsname)
        dnsapi = GodaddyApi(dnsinfo.key, dnsinfo.secret)
        query = dnsapi.get_domains()
        query_domains = []
        for item in query:
            if 'deletedAt' not in item.keys():
                print(f'sync_domain: {item}')
                dnsdomain = dict()
                dnsdomain['dnsname'] = dnsname
                dnsdomain['type'] = 'godaddy'
                dnsdomain['name'] = item['domain']
                DnsDomain.objects.update_or_create(name=dnsdomain['name'], defaults=dnsdomain)
                # 把api查询出来的域名放入列表中
                query_domains.append(dnsdomain['name'])

        # 把数据库查询出来的域名放入列表中
        db_domains = DnsDomain.objects.filter(dnsname=dnsname).values("name")
        print(db_domains)

        # 两两对比，得到需要删除的列表
        delete_domains = [domain['name'] for domain in db_domains if domain['name'] not in query_domains]
        print(f'delete_domains: {delete_domains}')

        # 循环列表并删除
        for domain in delete_domains:
            DnsDomain.objects.filter(dnsname=dnsname, name=domain).delete()
        return Response({'status': 'success'})


class NamesiloDomainViewSet(viewsets.ViewSet):
    serializer_class = CustomDomainSerializer

    def list(self, request):
        dnsinfo = DnsApiKey.objects.get(name=request.GET['dnsname'])
        dnsapi = NameSiloApi(dnsinfo.key, dnsinfo.secret)
        query = dnsapi.get_domains()
        serializer = CustomDomainSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        dnsname = request.data['dnsname']
        dnsinfo = DnsApiKey.objects.get(name=dnsname)
        post_namesilo_domain.delay(dnsinfo.key, dnsinfo.secret, dnsname)
        return Response({'status': 'success'})
