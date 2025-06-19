''' Ex017 - Catetos e Hipotenusa
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''

from math import sqrt


cat_op = float(input("Comprimento do cateto oposto: "))
cat_ad = float(input("Comprimento do cateto adjacente: "))

hipo = sqrt(cat_op**2 + cat_ad**2)

print(f"A hipotenusa vai medir {hipo:.2f}")