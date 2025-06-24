''' Ex099 - Função que descobre o maior
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''

from time import sleep

def linha():
    print("-="*30)


def maior(* nums):

    maior = 0
    
    linha()
    print("Analisando os valores passados...")

    for n in nums:
        if n > maior:
            maior = n
        
        print(n, end=' ', flush=True)
        sleep(0.5)
    
    print(f"Foram passados {len(nums)} valores.")
    print(f"O maior valor informado foi {maior}.")
    linha()



maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
