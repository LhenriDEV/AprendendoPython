from colorama import Fore, Style, init

init(autoreset=True)

largura = 40


def cadastrar():
    '''
    Cadastra uma pessoa no arquivo pessoas.txt
    '''

    # Leitura Nome
    print("-"*largura)
    print("NOVO CADASTRO".center(largura))
    print("-"*largura)

    while True:
        p = str(input("Nome da pessoa: ")).strip()

        if p == '': # (Verifica se apenas whitespace ou nada foi informado)
            print(f"{Fore.RED}Erro! Nada foi digitado...")

        else:
            p_subs = p.split() # Separar nome da pessoa em substrings para verificação individual de cada nome, sem contar whitespaces

            # Verifica se substrings são apenas alfabéticas
            valido = True

            for sub in p_subs:
                if not sub.isalpha():
                    valido = False
                    break
            
            if valido:
                p = ' '.join(p_subs)
                break
            else:
                print(f"{Fore.RED}Erro! Digite um nome válido!")


   # Leitura Idade 
    while True:
        idade = str(input("Idade da pessoa: ")).strip()

        if idade.isnumeric():
            break
        else:
            print(f"{Fore.RED}Erro! Digite uma idade válida!")


    # Concatenar tudo em uma só string
    atributos = p + ',' + idade + '\n' # (quebra linha para separar diferentes atributos)


    # Escrita dos dados num arquivo
    with open("exercicios/ex115/pessoas.txt", "a", encoding="utf-8") as arq: # (encoding necessario para aceitar acentuações)
        arq.write(atributos)

    print(f"{Fore.GREEN}Novo registro de {p} adicionado.")


def listar():
    '''
    Imprime lista formatada das pessoas cadastradas no arquivo pessoas.txt
    '''
    
    print("-"*largura)
    print("PESSOAS CADASTRADAS".center(largura))
    print("-"*largura)

    with open("exercicios/ex115/pessoas.txt", "r", encoding="utf-8") as arq:

        for linha in arq: # Por padrão, for loops iteram linhas de arquivo
            atributos = linha.strip().split(',')
            
            nome = atributos[0]
            idade = atributos[1]

            print(f"{nome.ljust(largura-10)} {idade} anos")


def topico(txt):
    print("-"*largura)
    print(txt.center(largura))
    print("-"*largura)


def menu():

    loop_menu = True

    while loop_menu:
        # Impressão
        topico("MENU PRINCIPAL")
        print(f"{Fore.YELLOW}1 - {Fore.BLUE}Ver pessoas cadastradas\n{Fore.YELLOW}2 - {Fore.BLUE}Cadastrar nova Pessoa\n{Fore.YELLOW}3 - {Fore.BLUE}Sair do Sistema")
        print("-"*largura)

        # Validação opção
        while True:
            
            # Validação de valor da opção
            while True:
                try:
                    opcao = int(input(f"{Fore.YELLOW}Sua Opção:{Style.RESET_ALL} "))
                except ValueError:
                    print(f"{Fore.RED}Opção deve ser um número!")
                except Exception as e:
                    print(f"Ocorreu o seguinte erro: {type(e)}")
                else:
                    break
            
            # Validar opção existente
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


# Testes
if __name__ == "__main__":
    menu()
    