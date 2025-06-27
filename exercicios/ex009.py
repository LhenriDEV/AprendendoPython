''' EX009 - Tabuada
Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuda.
'''

def tabuada(num):
    '''Imprime tabuada do numero informado.'''

    print("-"*15)
    for c in range(1, 11):
        print(f"{num} x {c:<3} = {num*c}")
    print("-"*15)

num = int(input("Digite um número para ver sua tabuada: "))

tabuada(num)

