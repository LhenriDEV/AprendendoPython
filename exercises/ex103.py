''' Ex103 - Ficha do Jogador
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

# Fazer a validação fora da função
'''

def ficha(nome: str = "<desconhecido>", gols: int = 0):

    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")


# Programa principal
print("-"*40)
jogador = str(input("Nome do Jogador: ")).strip()
gols = str(input("Número de Gols: "))


# Validação dos dados
if gols.isnumeric():
    int(gols)
else:
    gols = 0

if jogador == '':
    ficha(gols=gols)
else:
    ficha(jogador, gols)
