''' EX008 - Conversor de Medidas
Escreva um programa que leia um valor em metros e o exiba convertido em centimentos e milimetros.
'''

val = float(input("Uma distância em metros: "))

val_km = val / 1000
val_hm = val / 100
val_dam = val / 10
val_dm = val * 10
val_cm = val * 100
val_mm = val * 1000


print(f"\nA medida de {val}m corresponde a: ")
print(f"{val_km}km")
print(f"{val_hm}hm")
print(f"{val_dam}dam")
print(f"{val_dm}dm")
print(f"{val_cm}cm")
print(f"{val_mm}mm")
