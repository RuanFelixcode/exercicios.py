aprovados = 0
dici = {}
while True:
    nome = input('digite nome:')
    if nome == 'fim':
        break
    nota = float(input('digite a nota:'))
    dici.update({nome:nota})
    if nota >= 7 :
        aprovados +=1
print(aprovados)
