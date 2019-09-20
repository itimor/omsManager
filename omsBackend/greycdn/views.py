# -*- coding: utf-8 -*-
# author: timor

from rest_framework import viewsets
from rest_framework.response import Response
from greycdn.models import CdnSite, WhiteIp
from greycdn.serializers import CdnSiteSerializer, WhiteIpSerializer, ActionWhiteIpSerializer
from utils.greycdn_api import GREYCDN


class GreyCdnSiteViewSet(viewsets.ModelViewSet):
    queryset = CdnSite.objects.all()
    serializer_class = CdnSiteSerializer
    filter_fields = ['name']


class GreyCdnWhiteIpViewSet(viewsets.ModelViewSet):
    queryset = WhiteIp.objects.all()
    serializer_class = WhiteIpSerializer
    search_fields = ['name', 'create_time']


class GreyCdnActionWhiteIpViewSet(viewsets.ViewSet):
    serializer_class = ActionWhiteIpSerializer

    def list(self, request):
        name = request.GET['name']
        siteid = CdnSite.objects.get(name=name).siteid
        cdnapi = GREYCDN()
        query = cdnapi.getWhiteips(siteid)
        return Response(query)

    def post(self, request):
        name = request.data['name']
        siteid = CdnSite.objects.get(name=name).siteid
        cdnapi = GREYCDN()
        value = request.data['value']
        query = cdnapi.putWhiteips(siteid, value)
        WhiteIp.objects.create(name=name, value=value, create_user=request.user)
        return Response(query)
