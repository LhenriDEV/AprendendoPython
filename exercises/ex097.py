''' Ex097 - Um print especial
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
'''

def escreva(txt: str):

    # Tamanho da linha
    tam = len(txt) + 4

    print("~" * tam)
    print(txt.center(tam))
    print("~" * tam)



escreva("Olá, Mundo!")
escreva("CEV")
escreva("Curso de Python no YouTube")