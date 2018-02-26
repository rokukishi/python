#!/usr/bin/python
#-*- coding: utf8 -*-
import os, re, time
os.system("clear")
MASCARA = raw_input('MÁSCARA: ')
if re.findall ('^0(\.0){3}|128(\.0){3}|192(\.0){3}|224(\.0){3}|240(\.0){3}|248(\.0){3}|252(\.0){3}|254(\.0){3}|255\.(0|128|192|224|240|248|252|254)(\.0){2}|255\.255\.(0|128|192|224|240|248|252|254)(\.0)|255\.255\.255\.(0|128|192|224|240|248|252|254|255)$', MASCARA):
    print "."
    time.sleep(0.25)
    print "."
    time.sleep(0.25)
    print "."
    time.sleep(0.25)
    execfile('/python/.final.py')
else:
    print("Máscara inválida")
    time.sleep(3)
    execfile('/python/.mascara.py')

