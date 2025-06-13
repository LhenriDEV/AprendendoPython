'''
Create a program that simulates an ATM machine. At the start, ask user how much money they want to take out (must be int). The program will inform how many bills will be given. (Consider bills of $50, $20, $10 and $1)

DADOS INICIAIS:
> Valor a ser retirado pelo usuario
> Variaveis para quantidade de cedulas de cada nota

Calculo das cedulas a serem dadas:
> Pegar o valor a ser retirado e dividir pela maior nota = resultado inteiro será qtd de cedulas da nota
    > Se tiver resto, pegar o resto e dividir pela proxima maior nota (no caso $20) = resultado inteiro será qtd de cedulas da nota
        > Se tiver resto, pegar o resto e dividir pela proxima maior nota, e assim por diante
'''

from colorama import Fore, Style

print("-=" * 15)
print("ATM Machine".center(30))
print("-=" * 15)


req_money = int(input("\nHow much do you want to cash out? $"))

tot_50d = tot_20d = tot_10d = tot_1d = 0 # Total x dollar bills


if (req_money / 50) > 0: # se for divisivel por 50...
    tot_50d = req_money // 50
    req_money = req_money % 50 

if (req_money / 20) > 0:
    tot_20d = req_money // 20
    req_money = req_money % 20

if (req_money / 10) > 0:
    tot_10d = req_money // 10
    req_money = req_money % 10

if (req_money / 1) > 0:
    tot_1d = req_money // 1
    req_money = req_money % 1


print(f"\nYou will receive:\n{Fore.GREEN}{tot_50d} bills of $50\n{tot_20d} bills of $20\n{tot_10d} bills of $10\n{tot_1d} bills of $1{Style.RESET_ALL}")
