# -*- coding: utf-8 -*-
# author: timor

from rest_framework import serializers
from greycdn.models import CdnSite, WhiteIp
from users.models import User


class CdnSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CdnSite
        fields = ['url', 'id', 'name', 'siteid', 'desc']


class WhiteIpSerializer(serializers.ModelSerializer):
    create_user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = WhiteIp
        fields = ['url', 'id', 'name', 'value', 'create_user', 'create_time']


class ActionWhiteIpSerializer(serializers.Serializer):
    value = serializers.CharField()
