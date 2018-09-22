# -*- coding: utf-8 -*-
# author: kiven

from rest_framework import viewsets
from dnsmanager.models import DnsApiKey, DnsDomainType, DnsDomain, DnsRecord
from dnsmanager.serializers import DnsApiKeySerializer, DnsDomainTypeSerializer, DnsDomainSerializer, \
    DnsRecordSerializer


class DnsApiKeyViewSet(viewsets.ModelViewSet):
    queryset = DnsApiKey.objects.all()
    serializer_class = DnsApiKeySerializer
    filter_fields = ['name', 'type']
    search_fields = ['name']


class DnsDomainTypeViewSet(viewsets.ModelViewSet):
    queryset = DnsDomainType.objects.all()
    serializer_class = DnsDomainTypeSerializer
    filter_fields = ['name']


class DnsDomainViewSet(viewsets.ModelViewSet):
    queryset = DnsDomain.objects.all().order_by('-update_time')
    serializer_class = DnsDomainSerializer
    filter_fields = ['name', 'type']
    search_fields = ['name']


class DnsRecordViewSet(viewsets.ModelViewSet):
    queryset = DnsRecord.objects.all()
    serializer_class = DnsRecordSerializer
    filter_fields = ['name', 'type', 'domain__name']
    search_fields = ['name']
