'''Ex107 - Exercitando módulos em Python
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

Adapte o código do desafio 107 criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

# TODO: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
'''

from modulos import moeda

preco = float(input("Digite o preço: R$"))

dobro = moeda.dobro(preco)
metade = moeda.metade(preco)
aumento = moeda.aumentar(preco, 10)
desconto = moeda.diminuir(preco, 50)

print(f"A metade de {moeda.moeda(preco)} é {moeda.moeda(metade)}")
print(f"O dobro de {moeda.moeda(preco)} é {moeda.moeda(dobro)}")
print(f"Aumentando 10% de {moeda.moeda(preco)}, temos {moeda.moeda(aumento)}")
print(f"Diminuindo 50% de {moeda.moeda(preco)}, temos {moeda.moeda(desconto)}")
