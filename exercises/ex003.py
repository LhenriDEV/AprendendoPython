''' EX003 - Somando dois números
Crie um programa que leia dois números e mostre a soma entre eles.
'''
from time import sleep

# Função mensagem de loading
def loading(msg="Processando"):

    msg = msg.title()

    print(f"\n{msg}...\n")
    sleep(0.5)


n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))

soma = n1 + n2

loading() # Chama função
print(f"A soma entre {n1} e {n2} é igual a {soma}!")
