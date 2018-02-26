#!/usr/bin/python
#-*- coding: utf8 -*-
import os, re, time
os.system("clear")
FONE = raw_input('TELEFONE DDD XXXXXXXXX : ')
if re.match ('^(1[1-9]|2[1-2]|24|2[7-8]|3[1-5]|3[7-8]|4[1-9]|51|5[3-5]|6[1-9]|71|7[3-5]|77|79|8[1-9]|9[1-9])[ ](9([1-9]){8}|[1-8]([0-9]){7})$', FONE):
    print "."
    time.sleep(0.25)
    print "."
    time.sleep(0.25)
    print "."
    time.sleep(0.25)
    execfile('/python/.rg.py')
else:
    print("Telefone inválido")
    time.sleep(3)
    execfile('/python/.telefone.py')

