# -*- coding: utf-8 -*-
# author: timor

from rest_framework import viewsets
from rest_framework.response import Response
from firewall.models import CdnSite, WhiteIp
from firewall.serializers import CdnSiteSerializer, WhiteIpSerializer, ActionWhiteIpSerializer
from utils.cdnbest_api import CDNBEST
from users.models import User


class CdnSiteViewSet(viewsets.ModelViewSet):
    queryset = CdnSite.objects.all()
    serializer_class = CdnSiteSerializer
    filter_fields = ['name']


class WhiteIpViewSet(viewsets.ModelViewSet):
    queryset = WhiteIp.objects.all()
    serializer_class = WhiteIpSerializer
    search_fields = ['vhost']


# class BlackIpViewSet(viewsets.ModelViewSet):
#     queryset = BlackIp.objects.all()
#     serializer_class = BlackIpSerializer
#     search_fields = ['vhost']


class ActionWhiteIpViewSet(viewsets.ViewSet):
    serializer_class = ActionWhiteIpSerializer

    def list(self, request):
        uid = User.objects.get(username=request.user).uid
        vhost = request.GET['vhost']
        cdnapi = CDNBEST(uid, vhost)
        query = cdnapi.getFirewallWhiteips()
        return Response(query)

    def post(self, request):
        uid = User.objects.get(username=request.user).uid
        vhost = request.data['vhost']
        cdnapi = CDNBEST(uid, vhost)

        action = request.data['action']
        if action == '2':
            query = cdnapi.deleteFirewallWhiteips(1)
            WhiteIp.objects.create(vhost=vhost, value='', action=action)
        else:
            value = request.data['value']
            query = cdnapi.postFirewallWhiteips(1, value)
            WhiteIp.objects.create(vhost=vhost, value=value, action=action)
        return Response(query)
