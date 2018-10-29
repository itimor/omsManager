# -*- coding: utf-8 -*-
# author: itimor

from celery import shared_task
from utils.sendskype import skype_bot
from utils.sendmail import send_mail

@shared_task
def send_to_skype(user, content):
    skype_bot(user, content)


@shared_task
def send_to_mail(to_list, cc_list, sub, content):
    send_mail(to_list, cc_list, sub, content)

