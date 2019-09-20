# -*- coding: utf-8 -*-
# author: timor

from django.db import models
from users.models import User


class CdnSite(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=u'名称')
    siteid = models.CharField(max_length=100, unique=True, verbose_name=u'站点id')
    desc = models.TextField(null=True, blank=True, verbose_name=u'备注')

    def __str__(self):
        return self.name


class WhiteIp(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'站点')
    value = models.TextField(null=True, blank=True, verbose_name=u'值')
    create_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='greycdn_user', verbose_name=u'操作用户')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'操作时间')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-create_time']

