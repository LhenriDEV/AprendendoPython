''' Ex090 - Dicionário em Python
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

Media >= 7: Aprovado
Media >= 5: Recuperação
Media < 5: Reprovado 
'''

boletim = {
    "Aluno": None,
    "Media": None,
    "Situacao": None
}


boletim["Aluno"] = input("Nome: ")
boletim["Media"] = float(input(f"Média de {boletim['Aluno']}: "))


# Situação do aluno
if boletim["Media"] >= 7:
    boletim["Situacao"] = "Aprovado"
elif boletim["Media"] >= 5:
    boletim["Situacao"] = "Recuperação"
else:
    boletim["Situacao"] = "Reprovado"


print("-="*20)
for key, value in boletim.items():
    print(f" - {key}: {value}")
