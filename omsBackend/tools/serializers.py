# -*- coding: utf-8 -*-
# author: kiven

from rest_framework import serializers
from tools.models import Upload, Sendmail, Sendmessage,FileUpload


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = ['url', 'id', 'username', 'file', 'filename', 'filepath', 'archive', 'type', 'size', 'create_time']


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ['url', 'id', 'file']


class SendmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sendmail
        fields = ['url', 'id', 'to', 'cc', 'sub', 'content', 'create_time']


class SendmessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sendmessage
        fields = ['url', 'id', 'action_user', 'title', 'message']
