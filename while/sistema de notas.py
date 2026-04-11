'''Funções obrigatórias:
• Ler notas do aluno
• Calcular média
• Mostrar situação:
o Aprovado
o Recuperação
o Reprovado
• Permitir repetir para vários alunos
'''
media = 0
while True:
    nota = float(input('digite sua nota:'))
    nota1 = float(input('digite sua nota:'))
    if nota < 0 or nota1 > 10:
        print('nota invalida')
        print('digite uma nota valida')
    else:
        media = (nota + nota1)/2
        print(f'sua nota foi {media:.1f}')
    if media >=7:
        print('aprovado')
    elif media == 5 or media == 6 :
        print('recuperaçao')
    elif media < 5 :
        print('reprovado')
    else:
        print('parabens voce quebrou o sistema')
       
