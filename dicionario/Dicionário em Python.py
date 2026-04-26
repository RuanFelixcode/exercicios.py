'''Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''



situacao = {}
while True:
    aluno = input('digite o nome do aluno:')
    if aluno == 'fim':
        break
    media = float(input(f'digite a media de {aluno}:'))
    if media < 0 or  media > 10:
        print('media ivalida')
    elif media >= 0 and media < 5:
        situacao.update({aluno:media})
        print(f'situaçao {aluno}:{media} reprovado')
    elif media >= 5 and media < 7 :
        situacao.update({aluno:media})
        print(f'situaçao {aluno}:{media} recuperaçao')
    else:
        situacao.update({aluno:media})
        print(f'situaçao {aluno}:{media} aprovado')
        
print('turma') 
print(situacao)      
    
