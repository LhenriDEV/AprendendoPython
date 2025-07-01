'''Ex107-112 - Exercitando módulos em Python
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

Adapte o código do desafio 107 criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

Adicione no módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

No módulo dados.py, crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários. Obs: também deve aceitar vírgulas que serão interpretadas como ponto flutuante.
'''

from modulos import moeda, dados

preco = dados.leiaDinheiro("Digite o preço: R$")
moeda.mostrar_resumo(preco, 35, 22)
