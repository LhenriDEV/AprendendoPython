# Função que verifica se uma string é válido de ser preço. Para ser preço deve ser: int ou float; apenas composto de digitos 0-9, com exceção de um ponto flutuante.
def is_price(valor_str:str) -> bool:
    '''
    Verifica se string é válida de ser preço e convertido para float. Retorna True ou False.

    **PARÂMETROS**

    > valor_str (str): String com o valor a ser verificado.

    
    **RETORNA**

    > (bool): True ou False
    '''
    
    # Se a string for apenas decimais (0-9), desconsiderando uma ocorrência de ponto:
    if valor_str.replace('.', '', 1).isdecimal():
        return True
    else:
        return False
    

# Função para ler dinheiro/preço do usuário
def leiaDinheiro(prompt=""):
    '''
    Lê um valor float do usuário. Função similar ao input, implementando validação de float. (Vírgulas e pontos flutuantes são aceitas.)

    **PARÂMETROS**

    > prompt (str) (opcional): Mensagem de input.

    
    **RETORNA**

    > Valor convertido em float
    '''

    while True:

        print(prompt, end='')
        valor = input()

        # Coloca ponto no lugar de vírgula (se tiver)
        valor = valor.replace(',', '.', 1)

        if is_price(valor):
            break
        else:
            print(f'Erro! "{valor}" é um preço inválido.')


    return float(valor)


if __name__ == "__main__":
    
    # Teste leiaDinheiro()
    preco = leiaDinheiro("Digite preço: R$")
    print(f'{preco:.2f}')
