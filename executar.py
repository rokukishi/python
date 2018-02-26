#!/usr/bin/python
#-*- coding: utf8 -*-
import os, re, time
os.system("clear")
print("Formulário")
NOME = raw_input('Nome completo: ')
if re.match ('^[a-zA-Z ]+$', NOME):
    print "."
    time.sleep(0.25)
    print "."
    time.sleep(0.25)
    print "."
    time.sleep(0.25)
    execfile('/python/.email.py')
else:
    print("Nome inválido")
    time.sleep(2)
    execfile('/python/executar.py')



