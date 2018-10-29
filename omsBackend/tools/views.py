# -*- coding: utf-8 -*-
# author: timor

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from tools.models import Upload, Sendmail, Sendmessage, FileUpload
from tools.serializers import UploadSerializer, SendmailSerializer, SendmessageSerializer, FileUploadSerializer
from users.models import User
from rest_framework.permissions import AllowAny


class UploadViewSet(viewsets.ModelViewSet):
    queryset = Upload.objects.all().order_by("-create_time")
    serializer_class = UploadSerializer
    filter_fields = ('username', 'type',)


class FileUploadViewSet(viewsets.ModelViewSet):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    permission_classes = (AllowAny,)


class SendmailViewSet(viewsets.ModelViewSet):
    queryset = Sendmail.objects.all()
    serializer_class = SendmailSerializer

    def create(self, request, *args, **kwargs):
        to = request.data["to"]
        try:
            to_list = User.objects.get(username=to).email
        except Exception as e:
            to_list = 'itsupport@tb-gaming.com'
        if not to_list:
            to_list = 'itsupport@tb-gaming.com'

        cc = set(request.data["cc"].split(','))
        cc_list = ''
        try:
            for c in cc:
                if c:
                    c_email = User.objects.get(username=c).email
                    cc_list = cc_list + c_email + ','
        except Exception as e:
            cc_list = cc_list
        sub = request.data["sub"]
        content = request.data["content"]
        send_to_mail.delay(to_list, cc_list, sub, content)

        return Response({"code": "1024"}, status=status.HTTP_201_CREATED)


class SendmessageViewSet(viewsets.ModelViewSet):
    queryset = Sendmessage.objects.all()
    serializer_class = SendmessageSerializer

    def create(self, request, *args, **kwargs):
        content = request.data["title"] + '\n' + request.data["message"]
        action_user = request.data["action_user"].split(',')
        for i in action_user:
            try:
                to_action_user = User.objects.get(username=i).skype
                print(to_action_user)
                send_to_skype.delay(to_action_user, content)
            except Exception as e:
                print(e)
        return Response({"code": "1024"}, status=status.HTTP_201_CREATED)
