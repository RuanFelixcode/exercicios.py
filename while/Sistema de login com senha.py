'''Sistema de login com senha
Funções obrigatórias:
• Solicitar senha ao usuário
• Repetir até acertar a senha
• Limitar tentativas (opcional/desafio)
• Exibir mensagem de acesso permitido'''
cont = 0
while True :
    senha = int(input('digite a senha '))
    cont += 1
    if senha == 123:
        break
    elif cont == 3 :
        break
print('acesso permitido')
        
