'''📌 Exercício 3 — Classe Produto
Crie uma classe Produto que tenha:

Atributos: nome (string), preco (float) e quantidade (int)

Métodos:

adicionar_estoque(qtd): adiciona a quantidade ao estoque.

retirar_estoque(qtd): retira do estoque, se possível.

exibir_informacoes(): mostra todas as informações do produto.

'''

# TODO: Fazer este exercício

class Produto:
    def __init__(self, nome, preco, qtd=0):
        pass
        
        self.nome = nome
        self.preco = preco
        self.qtd = qtd


    def exibir_info(self):
        print(f"Nome: {self.nome}")
        print(f"Preço atual: ${self.preco:.2f}")
        print(f"Quantidade no estoque: {self.qtd}")


    def adicionar_estoque(self, qtd):
        self.qtd += qtd


    def retirar_estoque(self, qtd):
        self.qtd -= qtd


prod1 = Produto("Caderno", 15.00)
prod1.exibir_info()
prod1.adicionar_estoque(19)
print()

prod1.exibir_info()
prod1.retirar_estoque(2)
print()

prod1.exibir_info()
