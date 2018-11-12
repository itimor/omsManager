# -*- coding: utf-8 -*-
# author: timor

from rest_framework import viewsets
from users.serializers import UserSerializer, RoleSerializer
from users.models import User, Role


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = ['username']
    filter_fields = ['username']


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    filter_fields = ['name']
