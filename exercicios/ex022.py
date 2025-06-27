''' Ex022 - Analisador de Textos
Crie um programa que leia o nome completo de uma pessoa e mostre:
> O nome com todas as letras maiúsculas e minúsculas.
> Quantas letras ao todo (sem considerar espaços).
> Quantas letras tem o primeiro nome.
'''

nome = ' '.join(input("Digite o nome: ").split()) # split() retorna uma lista com cada substring sem espaço, e join() junta as subs com um espaço em branco


# Calcular tamanho do nome
nome_tamanho = len(nome.replace(' ', '')) # Coloca '' no lugar de ' ' (tira qualquer whitespace)


# Partes do nome separados numa lista (sem espaços incluídos)
nome_separado = nome.split()

primeiro_nome_tamanho = len(nome_separado[0]) # Quantidade de letras no primeiro nome


# Impressão final
print(f"Nome em maiúsculo: {nome.upper()}")
print(f"Nome em minúsculo: {nome.lower()}")
print(f"Nome tem {nome_tamanho} letras ao todo.")
print(f"Primeiro nome tem {primeiro_nome_tamanho} letras ao todo.")

