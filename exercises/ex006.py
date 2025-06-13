''' EX006 - Dobro, Triplo, Raiz Quadrada
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''
from math import sqrt # Funcao raiz quadrada

num = float(input("Digite um número: "))

print(f"O dobro de {num} vale {num * 2}")
print(f"O triplo de {num} vale {num * 3}")
print(f"A raiz quadrada de {num} é igual a {sqrt(num):.2f}")
