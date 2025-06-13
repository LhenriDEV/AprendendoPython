''' EX010 - Conversor de Moedas
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
'''

dolar = 5.54

saldo = float(input("Quantos reais você tem na sua carteira? R$"))

print(f"Com {saldo:.2f} reais você pode comprar {saldo / dolar :.2f} dólares.")
