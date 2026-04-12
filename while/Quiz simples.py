'''Quiz (perguntas e respostas)
Funções obrigatórias:
• Fazer perguntas ao usuário
• Verificar se a resposta está correta
• Contar pontuação
• Mostrar resultado final'''
cont = 0
erro = 0
while True:
    pergunta1 = input('qual e a cor do ceu?').lower()
    pergunta2 = input('a terra e redonda?').lower()
    pergunta3 = input('quanto e 1 + 1?').lower()
    if pergunta1 == 'azul':
        cont += 1
    else:
        erro += 1
    if pergunta2 == 'redondo':
        cont += 1
    else:
        erro += 1
    if pergunta3 == '2':
        cont += 1
    else:
        erro += 1
    break
print(f'total de acertos {cont} total de erros {erro}')
        
