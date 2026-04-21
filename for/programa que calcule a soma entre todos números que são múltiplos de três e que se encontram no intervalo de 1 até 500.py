#Faça um programa que calcule a soma entre todos números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
for i in range(1,501,2):
    print(i)
    soma = i + soma
print(f'resultado {soma}')
