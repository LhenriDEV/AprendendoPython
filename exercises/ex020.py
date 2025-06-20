''' Ex020 - Sorteando uma ordem na lista
O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

from random import shuffle

alunos = []

for c in range(1, 5):
    aluno = input(f"{c}º aluno: ").strip().title()

    alunos.append(aluno)

shuffle(alunos)

print(f"A ordem de apresentação será:")

for a in alunos:
    print(f"> {a}")