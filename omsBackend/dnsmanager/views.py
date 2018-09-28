# -*- coding: utf-8 -*-
# author: kiven

from rest_framework import viewsets
from rest_framework.response import Response
from dnsmanager.models import DnsApiKey, DnsDomain, DnsRecord
from dnsmanager.serializers import DnsApiKeySerializer, DnsDomainSerializer, DnsRecordSerializer, GodaddyDomainSerializer
from dnsmanager.godaddy_api import GodaddyApi
from tasks.tasks import post_godaddy_domain


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
    serializer_class = GodaddyDomainSerializer

    def list(self, request):
        dnsinfo = DnsApiKey.objects.get(name=request.GET['dnsname'])
        dnsapi = GodaddyApi(dnsinfo.key, dnsinfo.secret)
        query = dnsapi.get_domains()
        serializer = GodaddyDomainSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        dnsinfo = DnsApiKey.objects.get(name=request.data['dnsname'])
        dnsname = request.data['dnsname']
        print(dnsinfo)
        post_godaddy_domain.delay(dnsinfo, dnsname)
        return Response({'status': 'success'})
