# -*- coding: utf-8 -*-
# author: timor

from rest_framework import serializers
from firewall.models import CdnSite, WhiteIp


class CdnSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CdnSite
        fields = ['url', 'id', 'name', 'desc']


class WhiteIpSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhiteIp
        fields = ['url', 'id', 'vhost', 'value', 'action', 'create_time']


# class BlackIpSerializer(serializers.ModelSerializer):
#     site = serializers.SlugRelatedField(queryset=CdnSite.objects.all(), slug_field='name')
#
#     class Meta:
#         model = BlackIp
#         fields = ['url', 'id', 'site', 'bid', 'value', 'action', 'create_time']


class ActionWhiteIpSerializer(serializers.Serializer):
    value = serializers.CharField()
