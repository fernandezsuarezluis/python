#!/usr/bn/env python     --> script python
# -*- coding: utf-8 -*-  --> codificación utf8

__author__ = "Luis" 
__license__ = "GPL" 
__email__ = "a23luisfs@iessanclemente.net" 

import math
from math import pi
from math import pi as PI_VALUE

#1
num1 = int(input("Indica el primer número:"))
num2 = int(input("Indica el segundo número:"))
print("La suma de los dos números es", num1 + num2)

#2
num3 = int(input("Indica el primer número:"))
num4 = int(input("Indica el segundo número:"))
print("La resta de los dos números es", num3 - num4)

#3
num5 = int(input("Indica el primer número:"))
num6 = int(input("Indica el segundo número:"))
print("La multiplicación de los dos números es", num5 * num6)

#4
num7 = int(input("Indica el primer número:"))
num8 = int(input("Indica el segundo número:"))
print("La división entera de los dos números es", num7 // num8)

#5
num9 = int(input("Indica el primer número:"))
num10 = int(input("Indica el segundo número:"))
print("La división  de los dos números es", num9 / num10)

#6
num11 = int(input("Indica el primer número:"))
num12 = int(input("Indica el segundo número:"))
print("El resto de la división de estos dos números es", num11 / num12)

#7
frase1 = input("Introduce la primera frase:")
frase2 = input("Introduce la segunda frase:")
print("Al juntar las dos frases: " + frase1 + " " + frase2)

#8
base_triangulo = int(input("Introduce la base del triángulo:"))
altura_triangulo = int(input("Introduce la altura del triángulo:"))
print("El área del triángulo es: ", (base_triangulo * altura_triangulo) / 2)

#9
radio_circunferencia = float(input("Introduce el radio de la circunferencia:"))
print("El perímetro de la circunferencia es: ", 2 * pi * radio_circunferencia)
print("El área de la circunferencia es: ", pi * ((radio_circunferencia)*(radio_circunferencia)))
