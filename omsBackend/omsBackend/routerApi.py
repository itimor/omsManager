# -*- coding: utf-8 -*-
# author: kiven

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from users.views import UserViewSet, RoleViewSet

router.register(r'users', UserViewSet)
router.register(r'roles', RoleViewSet)

from tools.views import UploadViewSet, SendmailViewSet, SendmessageViewSet, FileUploadViewSet

router.register(r'upload', UploadViewSet)
router.register(r'sendmail', SendmailViewSet)
router.register(r'sendmessage', SendmessageViewSet)
router.register(r'fileupload', FileUploadViewSet)

from dnsmanager.views import DnsApiKeyViewSet, DnsDomainViewSet, DnsRecordViewSet, GodaddyDomainViewSet, NamesiloDomainViewSet

router.register(r'dnsapikeys', DnsApiKeyViewSet)
router.register(r'dnsdomains', DnsDomainViewSet)
router.register(r'dnsrecords', DnsRecordViewSet)
router.register(r'godaddydomains', GodaddyDomainViewSet, base_name='godaddydomains')
router.register(r'namesilodomains', NamesiloDomainViewSet, base_name='namesilodomains')
