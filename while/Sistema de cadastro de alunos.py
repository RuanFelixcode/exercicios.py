'''Sistema de cadastro de alunos
Funções obrigatórias:
• Cadastrar nome do aluno
• Permitir cadastrar vários alunos (repetição)
• Mostrar lista de alunos cadastrados
Extras:
• Contar quantos alunos foram cadastrados
• Buscar aluno pelo nome'''
lista = []
cont = 0
while True:
    print('''sair [0]
cadastrar aluno [1]
buscar aluno pelo nome [2]''')
    opc = int(input('selecione a opçao:'))
    if opc == 1 :
        nome = input('digite teu nome:')
        lista.append(nome)
        print('aluno cadastrado com sucesso')
        cont += 1
    elif opc == 2 :
        buscar = input('digite o nome do aluno que deseja saber:')
        if buscar in lista:
            print('esta cadastrado')
        else:
            print('nao esta cadastrado')
        
    elif opc == 0 :
        break
    else:
        print('opçao invalida')
for i in lista:
    print(f'alunos cadastrados: {i}')
print(f'totais de alunos cadastrados {cont}')
