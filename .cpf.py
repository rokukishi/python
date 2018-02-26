#!/usr/bin/python
#-*- coding: utf8 -*-
import os, re, time
os.system("clear")
CPF = raw_input('CPF (xxx.xxx.xxx-xx): ')
if re.findall ('^([0-9]){3}(\.([0-9]){3}){2}-([0-9]){1,2}$', CPF):
    print "."
    time.sleep(0.25)
    print "."
    time.sleep(0.25)
    print "."
    time.sleep(0.25)
    execfile('/python/.nascimento.py')
else:
    print("CPF inválido")
    time.sleep(3)
    execfile('/python/.cpf.py')


