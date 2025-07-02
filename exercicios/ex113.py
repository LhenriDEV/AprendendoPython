''' Ex113 - Funções aprofundadas em Python
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''

from colorama import Fore, Style, init

def leiaInt(prompt=''):
    while True:
        try:
            valor = input(prompt)
            
            valor = int(valor) # Tenta converter para int

        except ValueError:
            print(f"{Fore.RED}Erro! '{valor}' não é um número inteiro válido.")

        except KeyboardInterrupt:
            print(f"{Fore.RED}Usuário preferiu não digitar esse número.")
            valor = 0
            break

        except Exception as erro:
            print(f"{Fore.RED}Ocorreu o seguinte erro: {type(erro)}")

        else:
            break

    return valor


def leiaFloat(prompt=''):
    while True:
        try:
            valor = input(prompt)

            valor = float(valor)

        except ValueError:
            print(f"{Fore.RED}Erro! '{valor}' não é um número real válido.")

        except KeyboardInterrupt:
            print(f"{Fore.RED}Usuário preferiu não digitar esse número.")
            valor = 0
            break

        except Exception as erro:
            print(f"{Fore.RED}Erro: {type(erro)}")

        else:
            break

    return valor


# Programa principal
init(autoreset=True) # (colorama)

n1 = leiaInt("Digite um Inteiro: ")
n2 = leiaFloat("Digite um Real: ")

print(f"{Fore.YELLOW}O valor inteiro digitado foi {n1} e o real foi {n2}")
