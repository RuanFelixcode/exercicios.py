def menor (parametro):
    cont = 0
    menor = 0
    for i in parametro:
        if cont == 0:
            menor = i
            cont += 1
        if i < menor:
            menor = i
    return menor
lista = [1,23,4,0,5,6]
print(menor(lista))
