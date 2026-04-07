'''4. Pesquisa de satisfação
Uma empresa faz uma pesquisa onde:
• O cliente dá uma nota de 1 a 5
• O programa deve parar quando a nota for 0
• Ignorar notas inválidas (menores que 1 ou maiores que 5)
Mostrar:
• Quantas pessoas responderam
• Média das notas1'''
pessoas = 0
soma = 0
while True:
    
    nota = float(input('digite a nota '))
    if nota < 1 or nota > 5 :
        print('erro')
    elif nota == 0 :
        break
    else:
        soma = soma + nota
        pessoas += 1
    
media = soma/pessoas      
print(f'a media e {media:.2f}')
    
    
    
