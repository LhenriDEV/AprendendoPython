''' Ex106 - Sistema interativo de ajuda em Python
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.

Obs: help() aqui não funciona com minhas funções
'''

from colorama import Fore, Back, init
from os import get_terminal_size
import sys
from io import StringIO
from time import sleep

def preencher_linha(txt:str) -> str:
    '''
    Preenche a linha restante de um texto string com substrings vazias de acordo com a largura do terminal. Suporta quebras de linha.

    **PARÂMETROS:**

    > - txt (string): Texto a ser manipulado.

    **RETORNA**

        > - String preenchida.
    '''

    larg_terminal = get_terminal_size().columns # Largura do terminal

    
    # Método para textos que tem quebra de linha
    linhas_separadas = txt.split('\n')
    linhas_preenchidas = []

    for linha in linhas_separadas:
        espacos_restantes = larg_terminal - len(linha)

        if espacos_restantes < 0:
            linha = linha[:larg_terminal]
        else:
            linha = linha + " " * espacos_restantes

        linhas_preenchidas.append(linha)


    # Junta tudo numa string só
    string_preenchida = '\n'.join(linhas_preenchidas)

    return string_preenchida


# Função para imprimir título/tópico centralizado
def topico(txt: str, desc: str = None) -> str:
    '''
    Constroi uma string no formato de um tópico centralizado.

    **PARÂMETROS:**

    > - txt (str): Texto que se deseja construir um tópico
    
    > - desc (str) (opcional): Descrição inserida logo abaixo do tópico.

    **RETORNA**

    > - String do tópico formatado
    '''
    
    # Definir a largura do texto + padding
    tam_txt = len(txt) + 4


    if desc == None:
        return "~" * tam_txt + "\n" + txt.center(tam_txt) + "\n" + "~" * tam_txt
    else:
        tam_desc = len(desc) + 4
        return "~" * tam_txt + "\n" + txt.center(tam_txt) + "\n" + "~" * tam_txt + "\n" + desc + "\n" + "=" * tam_desc


# Função para capturar help() na saída em uma string
def capturar_help(comando) -> str:
    '''
    Retorna string do texto de saída do comando help()
    '''

    # Cria um objeto StringIO para capturar saída
    buffer = StringIO()

    # Salvar o stdout original
    stdout_original = sys.stdout

    # Saída original agora é o objeto StringIO
    sys.stdout = buffer

    try:
        help(comando)
    finally:
        sys.stdout = stdout_original

    
    return buffer.getvalue()
    

# Menu ajuda interativa
def pyhelp():
    '''
    Menu interativo de ajuda de funções do Python, imprimindo help() de maneira mais agradável na tela.
    '''

    # Resetar automaticamente o colorama
    init(autoreset=True)


    while True:

        # (Forma 1 de chamada: definindo uma variável para cada função chamada)
        txt_pyhelp = "SISTEMA DE AJUDA PYHELP"
        desc = "Digite 'fim' para finalizar o programa // Digite 'q' para sair da explicação atual"

        topico_pyhelp = topico(txt_pyhelp, desc)
        topico_pyhelp_preenchido = preencher_linha(topico_pyhelp)
        print(Back.GREEN + Fore.BLACK + topico_pyhelp_preenchido)
        

        # requested function
        req_function = str(input("Função ou Biblioteca > ")).strip().lower()

        if req_function == "fim":
            print(Back.RED + Fore.BLACK + preencher_linha(topico("ATÉ LOGO!")))
            break

        else:

            # (Forma 2 de chamada: usando funções diretamente)
            txt_acessando = preencher_linha(topico(f"Acessando o manual do comando {req_function}"))
            print(Back.BLUE + Fore.BLACK + txt_acessando)

            sleep(0.5)
            
            help_str = capturar_help(req_function) # help() em string
            print(Back.WHITE + Fore.BLACK + preencher_linha(help_str))
            
        sleep(1)
        
# Programa principal
pyhelp()
