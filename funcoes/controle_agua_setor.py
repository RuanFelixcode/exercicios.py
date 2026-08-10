def nome_setor():
    input_setor = input("Digite o nome do setor: ").replace(" ", "")
    if not input_setor.isalpha():
        print("Nome do setor inválido. Por favor, digite apenas letras.")
        return False
    return input_setor


def consumo_agua():
    try:
        consumo_passado = float(input("Digite o consumo de água do mês passado: "))
        if consumo_passado < 0:
            print("Consumo inválido. Por favor, digite um valor positivo.")
            return False,False


        consumo_atual = float(input("Digite o consumo de água do mês atual: "))
        if consumo_atual <= 0:
            print("Consumo atual inválido. Por favor, digite um valor positivo.")
            return False,False
       
        return consumo_passado,consumo_atual
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        return False,False


def calcular_custo(consumo):
    consumo_passado, consumo_atual = consumo
    porcentagem_aumento = ((consumo_atual - consumo_passado) / consumo_passado) * 100
    if porcentagem_aumento > 0:
        print(f"O consumo aumentou {porcentagem_aumento:.2f}% em relação ao mês passado.")
    elif porcentagem_aumento < 0:
        print(f"O consumo diminuiu {abs(porcentagem_aumento):.2f}% em relação ao mês passado.")
    else:
        print("O consumo foi igual ao mês passado.")
    print(f"Consumo do mês passado: {consumo_passado:.2f}")
    print(f"Consumo do mês atual: {consumo_atual:.2f}")


def main():
    setor = nome_setor()
    if not setor:
        return


    consumo_passado,consumo_atual = consumo_agua()
    if not consumo_passado:
        return


    calcular_custo((consumo_passado, consumo_atual))




   
if __name__ == "__main__":
    main()

