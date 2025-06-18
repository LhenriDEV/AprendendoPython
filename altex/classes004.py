'''📌 Exercício 2 — Classe ContaBancaria
Crie uma classe ContaBancaria com:

Atributos: titular (string) e saldo (float, inicia em 0)

Métodos:

depositar(valor): adiciona o valor ao saldo.

sacar(valor): retira o valor se houver saldo suficiente, senão imprime mensagem de erro.

exibir_saldo(): imprime o saldo atual.

'''

from random import randint
from colorama import Fore, Style

registered_ids = [0]

class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular


        # Gerando id
        random_id = 0

        while random_id in registered_ids: # Gera um id ainda não cadastrado para a conta
            random_id = randint(1, 100000)

        self.id = random_id
        registered_ids.append(self.id)
        del random_id


        self.saldo = 0.0
        
    
    def exibir_saldo(self):
        print(f"Saldo atual: {Fore.YELLOW}${self.saldo:.2f}{Style.RESET_ALL}")


    def depositar(self, valor: float):
        self.saldo += valor


    def sacar(self, valor: float):

        if valor > self.saldo:
            print(f"{Fore.RED}Erro! Você não tem saldo o suficiente para este saque!{Style.RESET_ALL}")
        else:
            self.saldo -= valor


titular = input("Titular da conta: ").strip().title()
conta1 = ContaBancaria(titular)
print(f"Conta cadastrada para o titular {conta1.titular}.")

conta1.exibir_saldo()

deposito = float(input("\nQuanto quer depositar para a conta? $"))
conta1.depositar(deposito)
conta1.exibir_saldo()

saque = float(input("\nQuanto você quer sacar? $"))
conta1.sacar(saque)
conta1.exibir_saldo()
