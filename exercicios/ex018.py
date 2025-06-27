''' Ex018 - Seno, Cosseno e Tangente
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

import math

ang = float(input("Digite o ângulo em graus: "))

ang_radians = math.radians(ang) # Converte para radianos para o calculo do seno, cos e tan
ang_seno = math.sin(ang_radians)
ang_cosseno = math.cos(ang_radians)
ang_tangente = math.tan(ang_radians)

print(f"O ângulo de {ang} tem o SENO de {ang_seno:.2f}")
print(f"O ângulo de {ang} tem o COSSENO de {ang_cosseno:.2f}")
print(f"O ângulo de {ang} tem a TANGENTE de {ang_tangente:.2f}")