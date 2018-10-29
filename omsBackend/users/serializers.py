# -*- coding: utf-8 -*-
# author: timor

from users.models import User, Role
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    roles = serializers.SlugRelatedField(many=True, queryset=Role.objects.all(), slug_field='name', allow_null=True)
    skype = serializers.CharField(allow_null=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'avator', 'skype', 'roles', 'is_active', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        roles = validated_data.pop('roles')
        user = User.objects.create(**validated_data)
        user.roles.set(roles)
        try:
            user.set_password(validated_data['password'])
        except:
            pass
        user.save()
        return user

    def update(self, instance, validated_data):
        roles = validated_data.pop('roles')
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.avator = validated_data.get('avator', instance.avator)
        instance.skype = validated_data.get('skype', instance.skype)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        try:
            instance.set_password(validated_data['password'])
        except Exception as e:
            pass
        instance.roles.set(roles)
        instance.save()
        return instance


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('url', 'id', 'name', 'desc')
