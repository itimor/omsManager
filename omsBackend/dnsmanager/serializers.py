# -*- coding: utf-8 -*-
# author: kiven

from rest_framework import serializers
from dnsmanager.models import DnsApiKey, DnsDomain, DnsRecord


class DnsApiKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = DnsApiKey
        fields = ['url', 'id', 'name', 'key', 'secret', 'type', 'desc']


class DnsDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = DnsDomain
        fields = ['url', 'id', 'title', 'dnsname', 'name', 'dnsService', 'type', 'create_time', 'expire_time', 'desc']


class DnsRecordSerializer(serializers.ModelSerializer):
    domain = serializers.SlugRelatedField(queryset=DnsDomain.objects.all(), slug_field='name')

    class Meta:
        model = DnsRecord
        fields = ['url', 'id', 'title', 'domain', 'name', 'status', 'type', 'value', 'value2', 'ttl', 'record_id',
                  'use', 'desc']


class GodaddyDomainSerializer(serializers.Serializer):
    domainId = serializers.IntegerField()
    domain = serializers.CharField()
    status = serializers.CharField()
    createdAt = serializers.DateTimeField()
