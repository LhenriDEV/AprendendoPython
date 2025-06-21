''' Ex098 - Função de Contador
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada

(Obs: 
> Contagem pode receber tanto valor negativo e positivo, e o programa deve identificar quando é pra contar para trás e para frente, independente do sinal
> Se o passo for dado 0, considerar o passo sendo 1

'''

from time import sleep

def contador(ini: int, fim: int, pas: int):
    '''
    Simula uma contagem na tela dos valores passados de acordo com o passo definido.

    Parâmetros:
    
    ini (int): número inicial da contagem

    fim (int): número final da contagem

    pas (int): passo de contagem
    '''

    # Primeira estrutura cond. (Impede passo de ser 0 e de ser negativo)
    if pas == 0:
        pas = 1
    elif pas < 0:
        pas = -pas # Transforma passo num valor positivo

    print("-="*30)
    print(f"Contagem de {ini} até {fim} de {pas} em {pas}")


    # Segunda estrutura cond. (Lógica da contagem) 
    # Contagem crescente
    if ini <= fim:
        for c in range(ini, fim + 1, pas):
            print(c, end=' ', flush=True)
            sleep(0.5)

    # Contagem decrescente
    elif ini > fim:
        for c in range(ini, fim - 1, -pas):
            print(c, end=' ', flush=True)
            sleep(0.5)


    print("FIM!")


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)

print("-="*30)
print("Agora é sua vez de personalizar a contagem!")
contador(int(input("Inicio: ")), int(input("Fim: ")), int(input("Passo: ")))
