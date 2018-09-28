# -*- coding: utf-8 -*-
# author: kiven

from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_auth.views import PasswordChangeView
from rest_framework_jwt.views import obtain_jwt_token
from django.views.generic.base import TemplateView
from omsBackend import settings
from omsBackend.routerApi import router

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    url(r'^api/', include(router.urls)),
    # 用户认证
    url(r'^api/changepasswd/', PasswordChangeView.as_view(), name='changepasswd'),
    url(r'^api/api-token-auth/', obtain_jwt_token, name='rest_framework_token'),
    url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'', TemplateView.as_view(template_name="index.html")),
]
