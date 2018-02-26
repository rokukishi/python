#!/usr/bin/python
#-*- coding: utf8 -*-
import os, re, time
os.system("clear")
print("Formulário")
NASCIMENTO = raw_input('Data de nascimento (DD/MM/AAAA): ')
if re.match ('^(0[1-9]|1[0-9]|2[0-9])/(02)/(190(0|4|8)|19(12|16|20|24|28|32|36|40|44|48|52|56|60|64|68|72|76|80|84|88|92|96)|200(0|4|8)|201(2|6))$', NASCIMENTO):
    print "."
    time.sleep(0.25)
    print "."
    time.sleep(0.25)
    print "."
    time.sleep(0.25)
    execfile('/python/.ip.py')
elif re.match ('^(0[1-9]|1[0-9]|2[0-9]|3[0-1])/(0(1|3|5|7|8)|1(0|2))/(19[0-9]{2}|200[0-9]|201[0-8])$', NASCIMENTO):
    print "."
    time.sleep(0.25)
    print "."
    time.sleep(0.25)
    print "."
    time.sleep(0.25)
    execfile('/python/.ip.py')
elif re.match ('^(0[1-9]|1[0-9]|2[0-9]|30)/(0(4|6|9)|11)/(19[0-9]{2}|200[0-9]|201[0-8])$', NASCIMENTO):
    print "."
    time.sleep(0.25)
    print "."
    time.sleep(0.25)
    print "."
    time.sleep(0.25)
    execfile('/python/.ip.py')
else:
    print("Data de nascimento inválida")
    time.sleep(2)
    execfile('/python/.nascimento.py')

