# ARQUIVO PRINCIPAL

from Conta import Conta
from Cliente import Cliente

def printMenu() -> int:
    print("\n----------------------------------")
    print("1 - Criar Conta")
    print("2 - Operação de Saque")
    print("3 - Operação de Depósito")
    print("4 - Operação de Transferência")
    print("5 - Extrato (mostrar o histórico das transações)")
    print("6 - Cadastrar cliente")
    print("7 - Sair")
    escolha = int(input("ESCOLHA: "))
    return escolha

def getClienteCPF(listaClientes, cpf) -> Cliente:
    for cliente in listaClientes:
        if cliente.cpf == cpf:
            return cliente

def getContaNumero(listaContas, num) -> Conta:
    for conta in listaContas:
        if conta.numero == num:
            return conta

listaClientes = []
listaContas = []

menu = printMenu()
while menu != 7:
    if menu == 1:
        print("--------------- CRIAR CONTA ---------------")
        cliente = input("Digite o CPF do cliente responsável: ")
        cliente = getClienteCPF(listaClientes, cliente)
        numero = int(input("Digite o número da conta: "))
        limite = float(input("Digite o limite desejado: "))
        conta = Conta(numero, cliente, 0.0, limite)
        listaContas.append(conta)
        print("Conta criada!")
        print("-------------------------------------------")

    elif menu == 2:
        print("--------------- OPERAÇÃO SAQUE ---------------")
        conta = int(input("Digite o número da conta: "))
        conta = getContaNumero(listaContas, conta)
        saque = float(input("Digite o valor a ser sacado: "))
        conta.retira(saque)
        print("----------------------------------------------")

    elif menu == 3:
        print("--------------- OPERAÇÃO DEPÓSITO ---------------")
        conta = int(input("Digite o número da conta: "))
        conta = getContaNumero(listaContas, conta)
        dep = float(input("Digite o valor a ser depositado: "))
        conta.deposita(dep)
        print("-------------------------------------------------")

    elif menu == 4:
        print("--------------- OPERAÇÃO TRANSFERÊNCIA ---------------")
        conta = int(input("Digite o número da conta: "))
        conta = getContaNumero(listaContas, conta)
        destino = int(input("Digite o número da conta destino: "))
        destino = getContaNumero(listaContas, destino)
        transf = float(input("Digite o valor a ser transferido: "))
        conta.transfere(destino, transf)
        print("------------------------------------------------------")

    elif menu == 5:
        print("--------------- EXTRATO ---------------")
        conta = int(input("Digite o número da conta: "))
        conta = getContaNumero(listaContas, conta)
        conta.extrato()
        print("---------------------------------------")

    elif menu == 6:
        print("--------------- CADASTRAR CLIENTE ---------------")
        cpf = input("Digite o cpf do cliente: ")
        nome, sobrenome = input("Digite o nome e o sobrenome do cliente: ").split(" ")
        cliente = Cliente(nome, sobrenome, cpf)
        listaClientes.append(cliente)
        print("Cliente cadastrado!")
        print("-------------------------------------------------")
    else:
        break

    menu = printMenu()

print("Até mais!")