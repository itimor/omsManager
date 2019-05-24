# -*- coding: utf-8 -*-
# author: itimor

import os

with open('target', 'r', encoding='utf8', errors='ignore') as fn:
    f = fn.readlines()
    for a in f:
        i = a.split()
        os.system('python zabbix_cli.py addhost -h %s -i %s' % (i[1], i[2]))
