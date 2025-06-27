''' EX011 - Pintando Parede
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

Área em metros quadrados: larg * alt

1 litro = 2 metros quadrados

Dados iniciais:
> (float) Largura, Altura, Área, litro_necessario
> (int) metro_por_litro = 2
'''

from colorama import Fore, Style

larg = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))
area = larg * alt

m2_por_litro = 2
litro_necessario = area / m2_por_litro


print(f"\nSua parede tem a dimensão de {Fore.YELLOW}{larg}x{alt}{Style.RESET_ALL} e sua área é de {Fore.YELLOW}{area:.2f}m².{Style.RESET_ALL}")
print(f"Vai precisar de {Fore.GREEN}{litro_necessario:.2f} litros{Style.RESET_ALL} para pintar toda a parede.")
