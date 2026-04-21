'''7.
Um sistema de cadastro precisa validar nomes.
Crie um programa que:
• Leia nomes até o usuário digitar "fim"
• Armazene em uma lista
• Mostre apenas os nomes com mais de 5 letras'''
lista = []
letras = []
while True:
    n = input('digite seu nome:').lower()
    if n == 'fim':
        break
    lista.append(n)
for i in lista:
    if len(i) >= 5:
        letras.append(i)
print(letras)
