''' Ex114 - Site está acessível?
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
'''

from colorama import Fore, Style, init
import urllib.request, urllib.error


init(autoreset=True)

try:
    resposta = urllib.request.urlopen("https://www.pudim.com.br/")

except urllib.error.URLError:
    print(f"{Fore.RED}Site não está acessível.")

except Exception as e:
    print(f"{Fore.RED}Ocorreu o seguinte erro: {type(e)}")

else:
    print(f"{Fore.GREEN}Site está acessível.")
    print(resposta.read())