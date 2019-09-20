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

from firewall.views import CdnBestSiteViewSet, CdnBestWhiteIpViewSet, CdnBestActionWhiteIpViewSet

router.register(r'cdnbestsites', CdnBestSiteViewSet)
router.register(r'cdnbestwhiteips', CdnBestWhiteIpViewSet)
router.register(r'actioncdnbest', CdnBestActionWhiteIpViewSet, base_name='actioncdnbest')

from greycdn.views import GreyCdnSiteViewSet, GreyCdnWhiteIpViewSet, GreyCdnActionWhiteIpViewSet

router.register(r'greycdnsites', GreyCdnSiteViewSet, base_name='greycdnsites')
router.register(r'greycdnwhiteips', GreyCdnWhiteIpViewSet, base_name='greycdnwhiteips')
router.register(r'actiongreycdn', GreyCdnActionWhiteIpViewSet, base_name='actiongreycdn')
