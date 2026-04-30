lista = []
maior = int(input('digite um numero:'))
for i in range(4):
    n = int(input('digite um numero:'))
    lista.append(n)
for i in lista:
    if i > maior:
        maior = i
print(maior)
