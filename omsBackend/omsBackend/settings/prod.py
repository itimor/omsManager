# -*- coding: utf-8 -*-
# author: kiven

import os

DEBUG = True
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

# 使用ldap认证
# AUTHENTICATION_BACKENDS = ("django_python3_ldap.auth.LDAPBackend",)
LDAP_AUTH_URL = "ldap://192.168.6.101:389"
LDAP_AUTH_SEARCH_BASE = "ou=AllUser,dc=oms,dc=com"
LDAP_AUTH_CONNECTION_USERNAME = r'oms\admin'
LDAP_AUTH_CONNECTION_PASSWORD = r'jjyy'

# email账号
MAIL_ACOUNT = {
    "mail_host": "mail@oms.com",
    "mail_user": "admin@oms.com",
    "mail_pass": "jjyy",
    "mail_postfix": "oms.com",
}

# skype账号
# from skpy import Skype

# SK_ACOUNT = {
#     'sk_user': 'admin@oms.com',
#     'sk_pass': 'jjyy'
# }
# SK = Skype(SK_ACOUNT["sk_user"], SK_ACOUNT["sk_pass"])
SK = 'skype'

REDIS_URL = 'redis://127.0.0.1:6379/'
# celery配置
CELERY_BROKER_URL = REDIS_URL + '0'

# celery结果返回，可用于跟踪结果
CELERY_RESULT_BACKEND = 'django-db'

# celery内容等消息的格式设置
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

# celery时区设置，使用settings中TIME_ZONE同样的时区
CELERY_TIMEZONE = TIME_ZONE

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL + '1',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

from datetime import timedelta
from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    'add-30-seconds': {
        'task': 'tasks.tasks.tty',
        'schedule': timedelta(seconds=3)
    },
    'add-every-day': {
        'task': 'tasks.tasks.tty',
        'schedule': crontab(hour=17, minute=50)
    }
}
