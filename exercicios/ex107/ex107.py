'''Ex107 - Exercitando módulos em Python
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

Adapte o código do desafio 107 criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

# TODO: Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
'''

from modulos import moeda

preco = float(input("Digite o preço: R$"))

# (f de formatado)
f_preco = moeda.moeda(preco)
f_dobro = moeda.dobro(preco, f=True)
f_metade = moeda.metade(preco, f=True)
f_aumento = moeda.aumentar(preco, 10, f=True)
f_desconto = moeda.diminuir(preco, 50, f=True)

print(f"A metade de {f_preco} é {f_metade}")
print(f"O dobro de {f_preco} é {f_dobro}")
print(f"Aumentando 10% de {f_preco}, temos {f_aumento}")
print(f"Diminuindo 50% de {f_preco}, temos {f_desconto}")
