'''6. Frequência de alunos
Um professor registra presença:
• Digite P para presente, F para falta
• O programa encerra quando digitar S
• Ignorar entradas inválidas
Mostrar:
• Total de presenças
• Total de faltas'''
Totalp = 0
Totalf = 0
while True : 
    presenca = input('digite a frquencia ').lower()
    if presenca == 'p' :
        Totalp += 1
    elif presenca == 'f' :
        Totalf += 1
    elif presenca == 's':
        break
print(f'total presente {Totalp} total falta {Totalf}')
    
