def dobro(num: float | int) -> float | int:
    '''
    Retorna o dobro de um número.
    '''
    res = num * 2

    return res


def metade(num: float | int) -> float | int:
    '''
    Retorna a metade de um número.
    '''
    res = num / 2

    return res


def aumentar(num: float | int, por: int) -> float | int:
    '''
    Aumenta em n% um número.
    '''

    res = num + (num * (por / 100)) # Ex: 10% -> 0.10

    return res


def diminuir(num: float | int, por: int) -> float | int:
    '''
    Desconta em n% um número.
    '''

    res = num - (num * (por / 100))

    return res


def moeda(num: float, moeda="R$") -> str:
    '''
    Retorna string de um preço float com uma formatação monetária, incluindo cifrão.
    '''

    # Criar string do número, formatado da mesma forma que um valor monetário tradicional
    num = f"{moeda}{num:.2f}".replace('.', ',')

    return num


# Rode este bloco apenas se modulo for executado diretamente
if __name__ == '__main__':
    
    # Testando moeda()
    preco = float(input("Digite preço: R$"))
    print(f"ORIGINAL: {preco}\nFORMATADO: {moeda(preco, "$")}")
