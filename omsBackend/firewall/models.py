# -*- coding: utf-8 -*-
# author: timor

from django.db import models
from users.models import User


class CdnSite(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name=u'名称')
    desc = models.TextField(null=True, blank=True, verbose_name=u'备注')

    def __str__(self):
        return self.name


Actions = {
    0: '增',
    1: '改',
    2: '删',
}


class WhiteIp(models.Model):
    vhost = models.CharField(max_length=20, verbose_name=u'站点')
    value = models.TextField(null=True, blank=True, verbose_name=u'值')
    action = models.CharField(choices=Actions.items(), default=0, max_length=1, verbose_name=u'操作')
    create_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=u'操作用户')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'操作时间')

    def __str__(self):
        return 'white_' + self.action

    class Meta:
        ordering = ['-create_time']

