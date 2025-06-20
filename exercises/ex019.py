''' Ex019 - Sorteando um item na lista
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
'''

from random import randint, choice

alunos = []

for c in range(1, 5):
    aluno = input(f"{c}º aluno: ").title()
    
    alunos.append(aluno)

escolhido = choice(alunos) # Randomiza um index de uma sequencia

print(f"O aluno escolhido foi {escolhido}.")
