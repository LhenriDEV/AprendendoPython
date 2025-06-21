''' Ex096 - Função que calcula área
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''

def mostra_area(larg, comp):
    area = larg * comp
    print(f"A área de um terreno {larg:.1f}x{comp:.1f} é de {area:.1f}m²")


# Programa principal
largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))

mostra_area(largura, comprimento)