''' Ex014 - Conversor de Temperaturas
Escreva um programa que converta uma temperatura digitado em graus Celsius e converta para graus Fahrenheit.
'''

def c_to_f(c_val: float):
    '''
    Retorna um valor em celsius convertido em Fahrenheit
    '''

    return (c_val * (9/5)) + 32 # Formula Celsius para Fahrenheint


c_val = float(input("Informe a temperatura em ºC: "))

print(f"A temperatura de {c_val:.1f}ºC corresponde a {c_to_f(c_val):.1f}ºF")
