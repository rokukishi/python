#!/usr/bin/python
#-*- coding: utf8 -*-
import os, re, time
os.system("clear")
RG = raw_input('RG (xx.xxx.xxx-x): ')
if re.findall ('^([0-9]){2}(\.([0-9]){3}){2}-[0-9Xx]$', RG):
    print "."
    time.sleep(0.25)
    print "."
    time.sleep(0.25)
    print "."
    time.sleep(0.25)
    execfile('/python/.cpf.py')
else:
    print("RG inválido")
    time.sleep(3)
    execfile('/python/.rg.py')

