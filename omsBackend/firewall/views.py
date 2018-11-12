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
    search_fields = ['vhost', 'create_time']


# class BlackIpViewSet(viewsets.ModelViewSet):
#     queryset = BlackIp.objects.all()
#     serializer_class = BlackIpSerializer
#     search_fields = ['vhost']


class ActionWhiteIpViewSet(viewsets.ViewSet):
    serializer_class = ActionWhiteIpSerializer

    def list(self, request):
        vhost = request.GET['vhost']
        cdnapi = CDNBEST(vhost)
        query = cdnapi.getFirewallWhiteips()
        return Response(query)

    def post(self, request):
        vhost = request.data['vhost']
        cdnapi = CDNBEST(vhost)

        action = request.data['action']
        if action == '2':
            query = cdnapi.deleteFirewallWhiteips(1)
            WhiteIp.objects.create(vhost=vhost, value='', action=action, create_user=request.user)
        else:
            value = request.data['value']
            query = cdnapi.postFirewallWhiteips(1, value)
            WhiteIp.objects.create(vhost=vhost, value=value, action=action, create_user=request.user)
        return Response(query)
