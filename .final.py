#!/usr/bin/python
#-*- coding: utf8 -*-
import os, re, time
os.system("clear")
print("Formulário")
FINAL = raw_input('As informações digitadas estão corretas? (sim/nao): ')
if re.match ('sim', FINAL):
    print ("Finalizando programa em... ")
    print "3"
    time.sleep(1)
    print "2"
    time.sleep(1)
    print "1"
    time.sleep(1)
elif re.match ('nao', FINAL):
    time.sleep(2)
    execfile('/python/executar.py')
else:
    print("Opção inválida")
    time.sleep(2)
    execfile('/python/.final.py')
