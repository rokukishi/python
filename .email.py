#!/usr/bin/python
#-*- coding: utf8 -*-
import os, re, time
os.system("clear")
EMAIL = raw_input('E-mail: ')
if re.findall ('^[a-z]([a-z0-9\._])+[@][a-z]([a-z\._])+(\.com|\.com\.br|\.br)$', EMAIL):
    print "."
    time.sleep(0.25)
    print "."
    time.sleep(0.25)
    print "."
    time.sleep(0.25)
    execfile('/python/.telefone.py')
else:
    print("E-mail inválido")
    time.sleep(3)
    execfile('/python/.email.py')

