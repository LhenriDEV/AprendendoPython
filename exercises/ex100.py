''' Ex100 - Funções para sortear e somar
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''

from time import sleep
from random import randint

def sorteia(lista: list):

    print("Sorteando 5 valores da lista: ", end='')

    # Sorteia 5 vezes
    for c in range(1, 6):
        randnum = randint(1, 10)
        print(randnum, end=' ', flush=True)
        sleep(0.5)
        lista.append(randnum)
    
    print("PRONTO!")


def somaPar(numeros: list):
    soma = 0

    for n in numeros:
        if n % 2 == 0:
            soma += n

    print(f"Somando os valores pares de {numeros}, temos {soma}")



# Programa principal
numeros = []
sorteia(numeros)
somaPar(numeros)