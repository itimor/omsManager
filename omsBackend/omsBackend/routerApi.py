# -*- coding: utf-8 -*-
# author: timor

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

from firewall.views import CdnSiteViewSet, WhiteIpViewSet, ActionWhiteIpViewSet

router.register(r'cdnsites', CdnSiteViewSet)
router.register(r'whiteips', WhiteIpViewSet)
router.register(r'actionwhiteip', ActionWhiteIpViewSet, base_name='actionwhiteip')
