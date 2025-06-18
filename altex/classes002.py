''' Classes002 — Classe Pessoa
Crie uma classe chamada Pessoa que tenha:

Atributos: nome (string) e idade (int)

Método: aniversario() que aumenta a idade em 1.

Método: apresentar() que imprime: "Olá, meu nome é {nome} e tenho {idade} anos."
'''

class Pessoa:

    # Construtor
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        print(f"{self.nome} fez aniversário!")
        self.idade += 1

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Instancia de Pessoa
nome = input("Nome: ")
idade = int(input("Idade: "))
p1 = Pessoa(nome, idade)

del nome
del idade

p1.apresentar()
p1.aniversario()
p1.apresentar()
