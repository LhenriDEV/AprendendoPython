''' EX008 - Conversor de Medidas (Função)
Escreva um programa que leia um valor em metros e o exiba convertido em centimentos e milimetros.
Crie uma função que converte medidas.
'''

def converter_comp(v, uni_ini, uni_fin): # Valor, Unidade inicial, Unidade final

    unidades = ["km", "hm", "dam", "m", "dm", "cm", "mm"]

    if uni_ini not in unidades:
        raise ValueError("Argumento inválido. Deve ser uma unidade de comprimento.")
    
    if uni_fin not in unidades:
        raise ValueError("Argumento inválido. Deve ser uma unidade de comprimento.")



    # Converter km
    if uni_ini == "km":
        if uni_fin == "km":
            return v
        elif uni_fin == "hm":
            return v * 10
        elif uni_fin == "dam":
            return v * 100
        elif uni_fin == "m":
            return v * 1000
        elif uni_fin == "dm":
            return v * 10000
        elif uni_fin == "cm":
            return v * 100000
        elif uni_fin == "mm":
            return v * 1000000
    
    # Converter hm
    elif uni_ini == "hm":
        if uni_fin == "km":
            return v / 10
        elif uni_fin == "hm":
            return v
        elif uni_fin == "dam":
            return v * 10
        elif uni_fin == "m":
            return v * 100
        elif uni_fin == "dm":
            return v * 1000
        elif uni_fin == "cm":
            return v * 10000
        elif uni_fin == "mm":
            return v * 100000
        
    # Converter dam
    elif uni_ini == "dam":
        if uni_fin == "km":
            return v / 100
        elif uni_fin == "hm":
            return v / 10
        elif uni_fin == "dam":
            return v
        elif uni_fin == "m":
            return v * 10
        elif uni_fin == "dm":
            return v * 100
        elif uni_fin == "cm":
            return v * 1000
        elif uni_fin == "mm":
            return v * 10000

    # Converter m
    elif uni_ini == "m":
        if uni_fin == "km":
            return v / 1000
        elif uni_fin == "hm":
            return v / 100
        elif uni_fin == "dam":
            return v / 10
        elif uni_fin == "m":
            return v
        elif uni_fin == "dm":
            return v * 10
        elif uni_fin == "cm":
            return v * 100
        elif uni_fin == "mm":
            return v * 1000
        
    # Converter dm
    elif uni_ini == "dm":
        if uni_fin == "km":
            return v / 10000
        elif uni_fin == "hm":
            return v / 1000
        elif uni_fin == "dam":
            return v / 100
        elif uni_fin == "m":
            return v / 10
        elif uni_fin == "dm":
            return v
        elif uni_fin == "cm":
            return v * 10
        elif uni_fin == "mm":
            return v * 100
        
    # Converter cm
    elif uni_ini == "cm":
        if uni_fin == "km":
            return v / 100000
        elif uni_fin == "hm":
            return v / 10000
        elif uni_fin == "dam":
            return v / 1000
        elif uni_fin == "m":
            return v / 100
        elif uni_fin == "dm":
            return v / 10
        elif uni_fin == "cm":
            return v
        elif uni_fin == "mm":
            return v * 10
        
    # Converter mm
    elif uni_ini == "mm":
        if uni_fin == "km":
            return v / 1000000
        elif uni_fin == "hm":
            return v / 100000
        elif uni_fin == "dam":
            return v / 10000
        elif uni_fin == "m":
            return v / 1000
        elif uni_fin == "dm":
            return v / 100
        elif uni_fin == "cm":
            return v / 10
        elif uni_fin == "mm":
            return v



# Programa principal
print(converter_comp(7000, "cm", "km"))