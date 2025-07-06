''' Ex115
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

# TODO: Modularizar o menu e as linhas de impressão
'''

from modulos import cadastrar, listar, largura
from colorama import Fore, Style, init

init(autoreset=True)


# Loop do Menu
loop_menu = True

while loop_menu:
    print("-"*largura)
    print("MENU PRINCIPAL".center(largura))
    print("-"*largura)
    print(f"{Fore.YELLOW}1 - {Fore.BLUE}Ver pessoas cadastradas\n{Fore.YELLOW}2 - {Fore.BLUE}Cadastrar nova Pessoa\n{Fore.YELLOW}3 - {Fore.BLUE}Sair do Sistema")

    # Validação de opção
    print("-"*largura)
    while True:

        # Validação de valor da opção
        while True:
            try:
                opcao = int(input(f"{Fore.YELLOW}Sua Opção:{Style.RESET_ALL} "))
            except ValueError:
                print(f"{Fore.RED}Opção inválida! Digite um número.")
            except Exception as e:
                print(f"Ocorreu o seguinte erro: {type(e)}")
            else:
                break

        valido = True

        match opcao:
            case 1:
                listar()
            case 2:
                cadastrar()
            case 3:
                print("-"*largura)
                print(Fore.BLUE + "Saindo do sistema... Até logo!".center(largura))
                print("-"*largura)
                loop_menu = False
            case _:
                print(f"{Fore.RED}Opção não existe! Tente novamente.")
                valido = False
        
        if valido:
            break
