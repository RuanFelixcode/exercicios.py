'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
def maior (*maio):
    for i in maio:
        print(f'analisando valores {i}',end=' ')
    print(f'o maior valor foi {max(maio)}')
        
            
maior(10,11,3,4)
