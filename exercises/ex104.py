''' Ex104 - Validando entrada de dados em Python
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')
'''

def leiaInt(msg_input: str = ''):
    '''
    Função que lê um número inteiro qualquer pelo teclado.

    PARÂMETROS:

    > (str) (opcional) msg_input: Mensagem impressa antecedida do input do usuário.
    '''

    # Módulo local
    from colorama import Fore, Style


    # Validação int
    while True:
        try:
            print(msg_input, end='')
            num = int(input())
            break
            
        except ValueError:
            print(f"{Fore.RED}Erro! Digite um número inteiro válido.{Style.RESET_ALL}")
    

    return num


# Programa principal
print("-"*40)
n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}.")
