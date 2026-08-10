def registro():
    nome = input("Digite o seu nome: ").strip()


    if not nome.isalpha():
        print("Nome inválido. Por favor, digite apenas letras.")
        return False,False
   
    try:
        idade = int(input("Digite a sua idade: ").strip())




    except ValueError:
        print("Idade inválida. Por favor, digite um número.")
        return False,False


    return nome, idade




def pagar():
    try:
        valor = float(input("Digite o valor a ser pago: ").strip())
        if valor <= 0:
            print("Valor inválido. Por favor, digite um número positivo.")
            return False


        if valor not in [15.0, 30.0, 50.0]:
            print("Valor inválido. Por favor, digite um dos valores permitidos: 15.0, 30.0 ou 50.0.")
            return False
       
    except ValueError:
        print("Valor inválido. Por favor, digite um número.")
        return False


    return valor




def menu():
    print('ingresso: Inteira (R$ 30,00), Meia (R$ 15,00) ou VIP (R$ 50,00). ')


def aplicar_desconto(idade, valor):
    if idade < 12:
        desconto = valor * 0.20
        valor_final = valor - desconto
        print(f"Desconto aplicado: R$ {desconto:.2f}. Valor final: R$ {valor_final:.2f}.")


    elif idade >= 60:
        desconto = 30.00
        valor_final = valor - desconto
        print(f"Desconto aplicado: R$ {desconto:.2f}. Valor final: R$ {valor_final:.2f}.")
    else:
        print(f"Valor a ser pago: R$ {valor:.2f}.")








def continuar():
    while True:
        resposta = input("Deseja continuar? (s/n): ").replace(" ", "").lower()
        if resposta in ('s','sim'):
            return False
        elif resposta in ('n','não','nao'):
            print("Obrigado por utilizar o sistema. Até logo!")
            return True
        else:
            print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")
         


def main():
    while True:
        menu()
        nome, idade = registro()
        if not nome:
            continue
        valor = pagar()
        if not valor:
            continue
        print(f"Olá, cliente {nome}. Sua idade é {idade} anos.")
        aplicar_desconto(idade, valor)
        if continuar():
            break

if __name__ == "__main__":
    main()
   
