#!/usr/bin/python
#-*- coding: utf8 -*-
import os, re, time
os.system("clear")
IP = raw_input('IP: ')
if re.findall ('^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3}$', IP):
    print "."
    time.sleep(0.25)
    print "."
    time.sleep(0.25)
    print "."
    time.sleep(0.25)
    execfile('/python/.mascara.py')
else:
    print("IP inválido")
    time.sleep(3)
    execfile('/python/.ip.py')

