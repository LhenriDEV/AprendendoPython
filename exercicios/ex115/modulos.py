from colorama import Fore, Style, init

init(autoreset=True)

largura = 40

# Função cadastrar
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

# Testes
if __name__ == "__main__":
    cadastrar()
    listar()
    