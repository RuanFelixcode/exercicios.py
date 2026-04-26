'''Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
início,fim,passo
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''
from time import sleep
def contador():
    for i in range(1,11,1):
        print(i)
        sleep(1)
    print('contagem inversa')
    for j in range(10,0,-2):
        print(j)
        sleep(1)
    inicio = int(input('digite o inicio:'))
    fim = int(input('digite o fim:'))
    passo = int(input('digite o passo:'))
    for k in range(inicio,fim,passo):
        print(k)
        sleep(1)
contador()
