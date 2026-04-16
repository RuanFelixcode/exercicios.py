'''Crie um programa que:
Crie uma lista vazia
Peça 4 números ao usuário
Guarde esses números na lista
Mostre:
a lista completa
a soma dos números
a média
'''
vazio = []
soma = 0
for i in range(4):
    n = int(input('digite sua nota:'))
    soma = soma + n
    vazio.append(n)
print(soma/len(vazio))
