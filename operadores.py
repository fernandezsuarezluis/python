#!/usr/bn/env python     --> script python
# -*- coding: utf-8 -*-  --> codificación utf8

__author__ = "Luis" 
__license__ = "GPL" 
__email__ = "a23luisfs@iessanclemente.net" 

print(8+8) #suma
print(8-8) #resta
print(8*8) #multiplicación
print(8/6) #división
print(8//6) #división entera
print(8**2) #exponenciales
print(6%5) #resto

mi_numero = str(5) #castear un int a un string indicándolo en la variable
print(type(mi_numero))

mi_numero2 = 5
print(type(mi_numero2)) #como aqui no lo he casteado sigo teniendo un int

print(3 == "3") #me devuelve que es false porque el tipo que está manejando es diferente (int vs string). Es algo de python y depende del lenguaje, en JS daría "true" `pr ejemplo.

print(3>4) #es false

print(3 < 4 and 3 != 4) #es true, and

print(3 < 4 or 3 != 4 ) #es true, or


