# -*- coding: utf-8 -*-
# author: timor

try:
    from omsBackend.settings import SK
except:
    SK = 'xxoo'

def skype_bot(user, content):
    chat = SK.chats[user]
    chat.sendMsg(content)


if __name__ == '__main__':
    for chatId in SK.chats.recent():
        print(chatId)
