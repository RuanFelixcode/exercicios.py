def leiaInt():
    while True:
        n = input('digite um numero:')
        if n .isnumeric():
            return f'{n} e um numero'
        else:
            return f'{n} nao e um numero'
           
print(leiaInt()) 
