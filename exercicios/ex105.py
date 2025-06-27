''' Ex105 - Analisando e gerando Dicionários
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

Quantidade de notas
A maior nota
A menor nota
A média da turma
A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
'''

def notas(* nts:float, sit:bool=False) -> dict:
    '''
    Função que retorna um dicionário de notas informando quantidade de notas, maior nota, menor nota, média da turma e situação.

    **PARÂMETROS**
    
    > (float) *nts: Notas dos alunos

    > (bool) sit: Se quiser incluir situação da turma ou não no dicionário (False por padrão)

    **RETORNA**

    > Dicionário
    '''
   
    dicio_notas = {}


    # Inicializa com a primeira nota
    maior_nota = menor_nota = nts[0]
    soma = 0 # Cálculo da média

    # Maior e menor nota
    for n in nts:
        if n > maior_nota:
            maior_nota = n

        if n < menor_nota:
            menor_nota = n


        soma += n

    # Cálculo da média
    media = soma / len(nts)

    
    dicio_notas["qtd_notas"] = len(nts)
    dicio_notas["maior"] = maior_nota
    dicio_notas["menor"] = menor_nota
    dicio_notas["media"] = media
    

    if sit:
        if media >= 9.0:
            dicio_notas["situacao"] = "Otima"
        elif media >= 7.0:
            dicio_notas["situacao"] = "Boa"
        elif media >= 5.0:
            dicio_notas["situacao"] = "Razoavel"
        else:
            dicio_notas["situacao"] = "Ruim"



    return dicio_notas


#Programa principal
turma = notas(5.5, 2.5, 1.5, sit=True)
print(turma)
print()
help(turma)