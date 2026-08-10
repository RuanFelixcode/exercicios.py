
produtos =  {'maionese':[{'preco':5.00},{'quantidade': 10}], 'ketchup':[{'preco':4.00},{'quantidade': 15}], 'mostarda':[{'preco':3.50},{'quantidade': 20}]}
def solicitacao_do_cliente():
    produto_solicitado = input("Digite o produto que que o cliente pediu:  ")
    try:
        quantidade_solicitada = int(input("Digite a quantidade que o cliente pediu:  "))
    except ValueError:
        print("Quantidade inválida.")
        return None, None
    return produto_solicitado, quantidade_solicitada


def verificar_estoque(produto, quantidade):
    if produto in produtos:
        preco = produtos[produto][0]['preco']
        quantidade_estoque = produtos[produto][1]['quantidade']
        if quantidade <= quantidade_estoque:
            total = preco * quantidade
            produtos[produto][1]['quantidade'] -= quantidade
            print(f"Pedido atendido! Total a pagar: R${total:.2f}")
        else:
            print("Desculpe, não temos estoque suficiente.")
    else:
        print("Produto não encontrado.")




produto_solicitado, quantidade_solicitada = solicitacao_do_cliente()
verificar_estoque(produto_solicitado, quantidade_solicitada)


