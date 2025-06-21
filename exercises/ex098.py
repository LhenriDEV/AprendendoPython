''' Ex098 - Função de Contador
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada

(Obs: 
> Contagem pode receber tanto valor negativo e positivo, e o programa deve identificar quando é pra contar para trás e para frente, independente do sinal
> Se o passo for dado 0, considerar o passo sendo 1

# TODO: (Tentar inverter o sinal do passo antes da lógica da contagem na função contador()) Dica: Multiplica o pas por -1 ou (pas = -pas)

'''

from time import sleep

def contador(ini: int, fim: int, pas: int):

    # Primeira estrutura cond. (Impede passo de ser 0)
    if pas == 0:
        pas = 1


    print("-="*30)
    print(f"Contagem de {ini} até {fim} de {pas} em {pas}")


    # Segunda estrutura cond. (Lógica da contagem) 
    # Contagem crescente
    if ini <= fim:
        if pas > 0:
            for c in range(ini, fim + 1, pas):
                print(c, end=' ', flush=True)
                sleep(0.5)
        elif pas < 0: # (Garante que passo seja positivo)
            for c in range(ini, fim + 1, -pas):
                print(c, end=' ', flush=True)
                sleep(0.5)

    # Contagem decrescente
    elif ini > fim:
        if pas > 0: # (Garante que passo seja negativo)
            for c in range(ini, fim - 1, -pas):
                print(c, end=' ', flush=True)
                sleep(0.5)
        elif pas < 0:
            for c in range(ini, fim - 1, pas):
                print(c, end=' ', flush=True)
                sleep(0.5)


    print("FIM!")


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)

print("-="*30)
print("Agora é sua vez de personalizar a contagem!")
contador(int(input("Inicio: ")), int(input("Fim: ")), int(input("Passo: ")))
