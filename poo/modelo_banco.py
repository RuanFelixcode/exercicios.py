import random
class Cliente:
    def __init__(self, nome, cpf, telefone):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone


class Conta:
    def __init__(self, dono):
        self.dono = dono
        self.identificador = self.gerar_identificador()
        self.saldo = 0

    def gerar_identificador(self):
        return random.randint(1000, 9999)

    def add_saldo(self,saldo):
        self.saldo += saldo

    def saque(self,valor):
        if valor > self.saldo:
            print('saque invalido')
            return

        self.saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

   

class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def add_conta(self, conta):
        self.contas.append(conta)


    def exibir_informacoes(self, identificador):
        for conta in self.contas:
            if conta.identificador == identificador:
                print("\n--- INFORMAÇÕES DA CONTA ---")
                print(f"Nome: {conta.dono.nome}")
                print(f"CPF: {conta.dono.cpf}")
                print(f"Telefone: {conta.dono.telefone}")
                print(f"Identificador da conta: {conta.identificador}")
                print(f"Saldo: R$ {conta.saldo:.2f}")
                return

        print("Conta não encontrada.")


banco = Banco()
cliente = None
conta =  None
while True:
   
    print("Bem-vindo ao Banco!")
    print("1. Criar conta")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Consultar informaçoes")
    print("5. Sair")


    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do cliente: ")
        cpf = input("Digite o CPF do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
        cliente = Cliente(nome, cpf, telefone)
        conta = Conta(cliente)
        banco.adicionar_cliente(cliente)
        banco.add_conta(conta)
        print(f"Cliente {nome} adicionado com sucesso!")


    elif opcao == "2":
        try:
            saldo = float(input('digite o saldo a ser depositado:').replace(' ',''))
            if saldo < 0:
                print('valor invalido')
                continue
               
            if  conta is None:
                print('crie uma conta primeiro')
                continue
               
            conta.add_saldo(saldo)
            print('saldo realizado com sucesso')
           
        except ValueError:
            print('valor invalido')

    elif opcao == "3":
        try:
            valor_saque = float(input('digite o valor do saque:').replace(' ',''))

            if valor_saque < 0:
                print('valor invalido')
                continue
           
            if conta is None:
                print('crie uma conta primeiro')
                continue
            conta.saque(valor_saque)

        except ValueError:
            print('valor invalido')

    elif opcao == "4":
        if conta is None:
            print('crie uma conta primeiro')
            continue

        identificador = conta.identificador
        banco.exibir_informacoes(identificador)



    elif opcao == "5":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")
