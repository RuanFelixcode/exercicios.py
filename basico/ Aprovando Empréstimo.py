salario_comprador = float(input('Qual é o salário do comprador? '))
valor_casa = float(input('Qual é o valor da casa? '))
anos_pagar = int(input('Em quantos anos vai pagar? '))

prestacao_mensal = valor_casa / (anos_pagar * 12)
limite = salario_comprador * 0.30

print(f'Prestação mensal: R$ {prestacao_mensal:.2f}')
print(f'Limite permitido: R$ {limite:.2f}')

if prestacao_mensal > limite:
    print('Empréstimo NEGADO')
else:
    print('Empréstimo APROVADO')
