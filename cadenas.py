#!/usr/bn/env python     --> script python
# -*- coding: utf-8 -*-  --> codificación utf8

__author__ = "Luis" 
__license__ = "GPL" 
__email__ = "a23luisfs@iessanclemente.net" 

nombre, edad = "Luis", 18 #definir varias variables en una misma línea
print(nombre, edad)

# nombre, edad = "Luis" #no puedo definir varias variables y luego poner menos de las que he definido
# print(nombre, edad)

# print(f"Hola, me llamo {nombre}") # la f y las llaves invocan a una variable que yo ya he definido con anterioridad

print(f"Hola, me llamo {nombre} y mi edad es {edad}") #indico las variables dentro de print
print("Hola, me llamo {} y mi edad {}".format(nombre, edad)) # otra forma de hacerlo, mas dificil mejor la otra

cadena = "hola"
print(len(cadena)) # indica la longitud de la cadena

print(cadena.capitalize()) # me permite escibir la primera letra de la cadena en mayúscula

print(cadena.upper()) # pone todas las letras en mayuscula

print(cadena.count("a")) # cuantas veces aparece algo en una misma cadena, una A en este ejemplo

print(type(cadena)) # es un string

print(cadena.isnumeric()) # false no es numérico

print(cadena.upper())

print(cadena.upper().isupper()) #devolver true o false concatenar tantos métodos como se desee, los caracteres se convierten a mayuscula y luego se comprueba que están en mayuscula

print("Ho" == "ho") # conversion a codigo ascii, el codigo de la h no es el mismo que el de ña H, por eso sale como false

print(cadena[-1]) # me devuelve la última letra de la palabra "hola" que es la "a"

print(cadena[1]) # me devuelve la o

cadena2 = "hola, a todos"

print(cadena2.split()) # separar los elementos de de la cadena y organizarlas en una lista

print(cadena2.split(",")) #indicar cuál es el elemento por el que deseo separar las palabras

nombre_2 = input("Dime tu nombre:") # solicito un input en string
print(nombre_2)

numero = int(input("Dime un número:")) # en caso de un int, tengo que castearlo para poder operar con élluis
print(numero + 3)



