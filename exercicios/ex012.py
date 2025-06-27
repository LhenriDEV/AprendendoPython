''' Ex012 - Calculando Descontos
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''

def aplicar_desconto(pre, por): # Preço, Porcentagem
    '''Retorna um valor descontado de acordo com a porcentagem indicada.\n\nParametros:\n\npre: Valor a ser descontado\n\npor: Porcentagem (percentual ou decimal)'''

    por = float(por) # Converter argumento para float

    # Se for passado percentual
    if por.is_integer():
        por /= 100 # por = por / 100

    return pre - (pre * por)


preco = float(input("Preço do produto: "))
novo_preco = aplicar_desconto(preco, 5)

print(f"O produto que custava R${preco:.2f}, na promoção com desconto de 5% vai custar R${novo_preco:.2f}.")
