# -*- coding: utf-8 -*-
# author: timor

import os

DEBUG = False
TIME_ZONE = 'Asia/Shanghai'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'oms',
        'USER': 'oms',
        'PASSWORD': 'oms@123#',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}

# email账号
MAIL_ACOUNT = {
    "mail_host": "mail@oms.com",
    "mail_user": "admin@oms.com",
    "mail_pass": "jjyy",
    "mail_postfix": "oms.com",
}