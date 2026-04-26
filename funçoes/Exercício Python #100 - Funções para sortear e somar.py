'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''
from random import randint
def  sorteia():
    numeros = [randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10)]
    print('-='*30)
    print(f'numeros sorteados -> {numeros}')
    print('-='*30)
    return numeros

lista = sorteia() 
def  somaPar():
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma = i + soma
    print(f'a soma de todos os pares e = {soma}')
somaPar()
