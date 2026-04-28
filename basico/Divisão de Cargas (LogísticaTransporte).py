'''Exercício 3: Divisão de Cargas (Logística/Transporte)
Cenário: Uma transportadora precisa levar 1.250 caixas em caminhões pequenos. Cada
caminhão suporta exatamente 12 caixas. Objetivo: 1. Quantos caminhões sairão
totalmente cheios? (Use //) 2. Quantas caixas sobrarão para serem enviadas em uma
última viagem menor? (Use %)'''

caixa = 1250
print(f'quantidade de caminhões {caixa//12} resto {caixa%12}')
