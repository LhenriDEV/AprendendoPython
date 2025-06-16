'''
Criar Class Carro com no minimo 3 propriedades e 3 metodos
'''

from colorama import Fore, Style

class Carro:
    # Construtor
    def __init__(self, marca, modelo, ano, cod):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cod = cod

    def info(self): # Mostrar informações de instancia x de Carro
        print(f"\n{Fore.YELLOW}Informações do carro {self.cod}:{Style.RESET_ALL} ")
        print(f"> Marca: {self.marca}")
        print(f"> Modelo: {self.modelo}")
        print(f"> Ano: {self.ano}\n")

    def ligar(self):
        print(f"{Fore.GREEN}Carro ligado.{Style.RESET_ALL}")

    def desligar(self):
        print(f"{Fore.RED}Carro desligado.{Style.RESET_ALL}")

carro1 = Carro("Toyota", "Corolla", 2014, 12985)

carro1.ligar()
carro1.info()
carro1.desligar()
