''' Ex106 - Sistema interativo de ajuda em Python
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
'''

# TODO: Função preencher_linha()

from colorama import Fore, Back, init
from os import get_terminal_size


def preencher_linha(txt):

    larg_terminal = get_terminal_size().columns # Largura do terminal
    txt = txt + " " * (larg_terminal - len(txt)) # Preencher com string vazia

    return txt


# Função para colorir o fundo de uma string
def colorir_fundo(txt, cor):
    
    init(autoreset=True)

    # Garantir que string cor seja passado em minusculo
    cor = cor.lower()

    if cor == "blue":
        txt = Back.BLUE + txt
    elif cor == "green":
        txt = Back.GREEN + txt
    elif cor == "white":
        txt = Back.WHITE + txt

    return txt


# Função para imprimir título/tópico centralizado
def topico(txt: str, desc: str = None):
    
    tam_txt = len(txt) + 4

    if desc == None:
        return "~" * tam_txt + "\n" + txt.center(tam_txt) + "\n" + "~" * tam_txt
    else:
        tam_desc = len(desc) + 4
        return "~" * tam_txt + "\n" + txt.center(tam_txt) + "\n" + "~" * tam_txt + "\n" + desc + "\n" + "=" * tam_desc


# Menu ajuda interativa
def pyhelp():

    while True:

        txt_pyhelp = "SISTEMA DE AJUDA PYHELP"
        desc = "f - finalizar programa // q - sair da explicação atual"

        topico_pyhelp = topico(txt_pyhelp, desc)
        topico_pyhelp_preenchido = preencher_linha(topico_pyhelp)
        print(Back.RED + topico_pyhelp_preenchido)
        

        # requested function
        req_function = str(input("Função ou Biblioteca > ")).strip().lower()

        if req_function == "f":
            break
        else:
            topico(f"Acessando o manual do comando {req_function}")
            help(req_function)

        
# Programa principal
pyhelp()

print("\nFIM DO PROGRAMA!")
