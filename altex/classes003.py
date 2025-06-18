'''Classes003: Lista de Pessoas
Crie um programa que:

Peça para o usuário digitar os dados de 3 pessoas (nome e idade).

Para cada pessoa, crie uma instância da classe Pessoa (a mesma que você já fez).

Armazene essas instâncias em uma lista.

Percorra a lista e chame o método apresentar() de cada pessoa.

Em seguida, para cada pessoa, chame o método aniversario() e depois chame apresentar() novamente para mostrar a idade atualizada.

'''

class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

    def aniversario(self):
        self.idade += 1
        print(f"{self.nome} fez aniversário. Agora tem {self.idade} anos.")


lista_pessoas = []

# 3 instancias de Pessoa()
for c in range(0, 3):
    nome = input(f"Digite o nome da {c + 1}ª pessoa: ")
    idade = int(input(f"Digite a idade da {c + 1}ª pessoa: "))

    pessoa = Pessoa(nome, idade)
    lista_pessoas.append(pessoa)



# Apresentação inicial
print()

for p in lista_pessoas:
    p.apresentar()


# Aniversário
print()

for p in lista_pessoas:
    p.aniversario()

