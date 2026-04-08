'''Sistema de notas escolares
Funções obrigatórias:
• Ler notas do aluno
• Calcular média
• Mostrar situação:
o Aprovado
o Recuperação
o Reprovado
• Permitir repetir para vários alunos
Extras:
• Mostrar maior e menor nota'''
while True :
    print('digite notas e 0 para parar')
    nota1 = float(input('digite sua nota '))
    nota2 = float(input('digite sua nota '))
    media = nota1 / nota2
    print(media)
    if nota1 == 0 :
        break
    elif nota1 > nota2 :
        print('primeira nota e maior')
    elif nota2 > nota1 :
         print('segunda nota e maior')
    
        
