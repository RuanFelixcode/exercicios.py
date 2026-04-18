'''Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''
def area (l,c):
    print(f'calculando largura {l} e comprimento {c} {l*c}')
l = float(input('digite a largura:'))
c = float(input('digite o comprimento: '))
area(l,c)
