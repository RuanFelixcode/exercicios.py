'''4.
Uma lista de números foi criada:
numeros = [10, 25, 30, 7, 18]
Percorra a lista e:
• Mostre os números pares
• Mostre os números ímpares'''
numeros = [10, 25, 30, 7, 18]
pares = 0
impares = 0
for i in numeros:
    if i % 2 == 0:
        
        print(f'numeros pares {i}')
    else:
        print(f'numeros impares:{i}')
    
