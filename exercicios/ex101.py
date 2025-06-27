''' Ex101 - Funções para votação
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''

def voto(by: int):
    '''
    Retorna string com a situação de votação para a idade de uma pessoa

    (int) by: Ano de nascimento da pessoa
    '''

    from datetime import datetime

    ano_atual = datetime.now().year
    idade = ano_atual - by


    if idade < 16:
        return f" Com {idade} anos: VOTO NEGADO"
    elif idade >= 16 and idade < 18 or idade >= 70:
        return f" Com {idade} anos: VOTO OPCIONAL"
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"
    



ano_nasc = int(input("Em que ano você nasceu? "))
print(voto(ano_nasc))
