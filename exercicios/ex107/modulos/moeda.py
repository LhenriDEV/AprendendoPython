def dobro(num: float | int, f=False, f_moeda='R$') -> float | int:
    '''
    Retorna o dobro de um número. Se parâmetro 'f' for especificado, retorna string do número formatado.

    **PARÂMETROS:**

    > (float | int) num: Número ou preço.

    > (bool) f: Formatação. Determina se o preço deve ser formatado como um valor monetário de acordo com sua moeda.

    > (str) f_moeda: Formato de moeda a ser definido na formatação. Ex: "R$", "$", etc.

    **RETORNA**

    > (float | int): Caso f=False

    > (str): Caso f=True
    '''
    res = num * 2

    if f:
        # Formatado (retorna string)
        return moeda(res, f_moeda)
    else:
        # Não formatado (retorna float/int)
        return res


def metade(num: float | int, f=False, f_moeda='R$') -> float | int:
    '''
    Retorna a metade de um número.

     **PARÂMETROS:**

    > (float | int) num: Número ou preço.

    > (bool) f: Formatação. Determina se o preço deve ser formatado como um valor monetário de acordo com sua moeda.

    > (str) f_moeda: Formato de moeda a ser definido na formatação. Ex: "R$", "$", etc.

    **RETORNA**

    > (float | int): Caso f=False

    > (str): Caso f=True
    '''
    res = num / 2

    if f:
        return moeda(res, f_moeda)
    else:
        return res


def aumentar(num: float | int, por: int, f=False, f_moeda='R$') -> float | int:
    '''
    Aumenta em n% um número.

     **PARÂMETROS:**

    > (float | int) num: Número ou preço.

    > (int) por: Porcentagem do valor. Ex: 10%

    > (bool) f: Formatação. Determina se o preço deve ser formatado como um valor monetário de acordo com sua moeda.

    > (str) f_moeda: Formato de moeda a ser definido na formatação. Ex: "R$", "$", etc.

    **RETORNA**

    > (float | int): Caso f=False

    > (str): Caso f=True
    '''

    res = num + (num * (por / 100)) # Ex: 10% -> 0.10

    if f:
        return moeda(res, f_moeda)
    else:
        return res


def diminuir(num: float | int, por: int, f=False, f_moeda='R$') -> float | int:
    '''
    Desconta em n% um número.

     **PARÂMETROS:**

    > (float | int) num: Número ou preço.

    > (int) por: Porcentagem do valor. Ex: 10%

    > (bool) f: Formatação. Determina se o preço deve ser formatado como um valor monetário de acordo com sua moeda.

    > (str) f_moeda: Formato de moeda a ser definido na formatação. Ex: "R$", "$", etc.

    **RETORNA**

    > (float | int): Caso f=False

    > (str): Caso f=True
    '''

    res = num - (num * (por / 100))

    if f:
        return moeda(res, f_moeda)
    else:
        return res


def moeda(num: float, moeda="R$") -> str:
    '''
    Retorna string de um preço float com uma formatação monetária, incluindo cifrão.

    **PARÂMETROS:**

    > (float) num: Número ou preço.

    > (str) moeda: Cifrão de moeda.

    **RETORNA**

    > (str)
    '''

    # Criar string do número, formatado da mesma forma que um valor monetário tradicional
    num = f"{moeda}{num:.2f}".replace('.', ',')

    return num


def mostrar_resumo(p, por_a=0, por_d=0):
    '''
    Imprime na tela um resumo formatado de variações de preço do valor informado: Dobro, metade, aumento e redução.

    **PARÂMETROS**

    > p: Preço/valor (float ou int)

    > por_a: Porcentagem de aumento, por padrão 0 (int)

    > por_d: Porcentagem de desconto, por padrão 0 (int)


    **RETORNA**

    > None
    '''

    print("-"*40)
    print("RESUMO DO VALOR".center(40))
    print("-"*40)

    print(f"{'Preço analisado:'.ljust(25)} {moeda(p)}")
    print(f"{'Dobro do preço:'.ljust(25)} {dobro(p, f=True)}")
    print(f"{'Metade do preço:'.ljust(25)} {metade(p, f=True)}")
    print(f"{f'Aumento em {por_a}%:'.ljust(25)} {aumentar(p, por_a, f=True)}")
    print(f"{f'Redução em {por_d}%:'.ljust(25)} {diminuir(p, por_d, f=True)}")

    print("-"*40)

# Rode este bloco apenas se modulo for executado diretamente
if __name__ == '__main__':
    
    preco = float(input("Digite preço: R$"))
    
    '''
    # Testando moeda()
    print(f"ORIGINAL: {preco}\nFORMATADO: {moeda(preco, "$")}")
    '''

    '''
    # Testando parâmetro f ---> utiliza moeda()
    print(f"Dobro: {dobro(preco, f=True)}")
    print(f"Metade: {metade(preco, f=True)}")
    print(f"Aumentado em 20%: {aumentar(preco, 20, f=True)}")
    print(f"Descontado em 50%: {diminuir(preco, 50, f=True)}")
    '''

    # Teste resumo()
    mostrar_resumo(preco, 60, 50)
