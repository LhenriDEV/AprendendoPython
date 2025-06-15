''' Ex013 - Reajuste Salarial
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''

def aplicar_aumento(val, por):

    por = float(por)

    if por.is_integer():
        por /= 100 # por / 100

    return val + (val * por)


salario = float(input("Qual é o salário do Funcionário? R$"))
novo_salario = aplicar_aumento(salario, 15)

print(f"Um funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${novo_salario:.2f}.")
