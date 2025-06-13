''' EX004 - Dissecando uma Variável
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
'''

user_input = input("Digite algo: ")

print()
print(f"O tipo primitivo desse valor é {type(user_input)}")

print(f"Só tem espaços? {user_input.isspace()}")
print(f"É numérico? {user_input.isnumeric()}")
print(f"É alfabético? {user_input.isalpha()}")
print(f"É alfanumérico? {user_input.isalnum()}")
print(f"É todo maiúsculo? {user_input.isupper()}")
print(f"É todo minúsculo? {user_input.islower()}")
print(f"Está capitalizado? {user_input.istitle()}")
print(f"É um identificador válido? {user_input.isidentifier()}")
print(f"É um ASCII? {user_input.isascii()}")
print(f"É um decimal? {user_input.isdecimal()}")
print(f"É um dígito? {user_input.isdigit()}")
