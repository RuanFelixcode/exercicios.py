nome = input('digite seu nome:')
horario = float(input('qual o horario atual?:'))
if horario >= 6 and horario <=11.00:
    print(f'bom dia {nome}')
elif horario > 11.00 and horario <=17.00:
    print(f'boa tarde {nome}')
elif horario > 17.00 and horario <= 23.00:
    print(f'boa noite {nome}')
else:
    print(f'boa madrugada {nome}')
