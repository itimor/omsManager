# -*- coding: utf-8 -*-
# author: kiven

from rest_framework import viewsets
from users.serializers import UserSerializer, RoleSerializer
from users.models import User, Role


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    search_fields = ['username']
    filter_fields = ['username', 'roles__name']


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    filter_fields = ['name']
