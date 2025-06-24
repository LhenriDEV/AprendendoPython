''' Ex102 - Função para Fatorial
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''

def fatorial(num: int, show: bool = False) -> int:
    '''
    Função que calcula o fatorial de um número inteiro.
    
    PARÂMETROS:

    > (int) num: Número a ser calculado

    > (boolean) show: Determina se o processo de cálculo de fatorial será mostrado na tela. (False por padrão)

    RETORNA:

    > (int) Fatorial do número
    '''

    fat = 1

    for c in range(num, 0, -1):
        
        fat *= c

        # Impressão do cálculo
        if show: 
            if c > 1:
                print(f"{c} x ", end='')
            else:
                print(f"{c} = {fat}") # Inclui o resultado no final.


    return fat


# Programa principal
fat = fatorial(6, show=True)
help(fatorial)
