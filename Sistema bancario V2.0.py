# Funções

def exibir_menu():
    menu = '''
    Olá, selecione uma opção:

    (1) Depósito
    (2) Saque
    (3) Extrato
    (4) Lista de Contas-Correntes
    (5) Lista de Clientes
    (6) Criar Conta-Corrente
    (7) Cadastrar Cliente
    (0) Sair

    ==>
    '''
    print(menu)

def sacar(saldo, valor, limite, qtd_saques, limite_saques, extrato):
    if valor <= saldo and qtd_saques < limite_saques and valor <= limite:
        print('Saque realizado')
        saldo -= valor
        qtd_saques += 1
        extrato += f'Saque: R$ {valor:.2f}\n'
    elif valor > saldo:
        print('Saldo insuficiente')
    elif qtd_saques >= limite_saques:
        print('Limite de saques atingido')
    elif valor > limite:
        print('Valor maior que o limite de saque')
    return saldo, extrato

def depositar(saldo, extrato, valor):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print(f'Saldo Conta: R${saldo:.2f}')
    else:
        print("Valor incorreto. Tente novamente")
    return saldo, extrato

def novo_usuario(clientes):
    cpf = input("Insira seu CPF: ")

    cliente = filtro_cpf(cpf, clientes)

    if cliente:
        print("CPF já cadastrado")
    else:
        nome = input("Insira seu nome completo: ")
        dtnascimento = input("Insira sua data de nascimento: ")
        endereco = input("Insira seu endereço (logradouro, nr - bairro - cidade/sigla do estado): ")
        clientes.append({"cpf": cpf, "nome": nome, "data de nascimento": dtnascimento, "endereco": endereco})
        print("Cadastro realizado com sucesso")

def filtro_cpf(cpf, clientes):
    return next((cliente for cliente in clientes if cliente["cpf"] == cpf), None)

def criar_conta(agencia, clientes):
    cpf = input("Insira seu CPF: ")

    cliente = filtro_cpf(cpf, clientes)

    if cliente:
        conta = {"Agencia": agencia, "conta": len(CCs) + 1, "cliente": cliente}
        CCs.append(conta)
        print('Conta criada com sucesso')
    else:
        print("Usuário não encontrado")

# Variáveis
saldo_conta = 0
limite = 500
qtd_saques = 0
limite_saques = 3
extrato = ''
clientes = []
CCs = []
Agencia = "0001"

# Interface
while True:
    exibir_menu()
    opcao = input()

    # Depósito
    if opcao == "1":
        valor = float(input("Valor do depósito: "))
        saldo_conta, extrato = depositar(saldo_conta, extrato, valor)

    # Saque
    elif opcao == "2":
        valor = float(input("Valor do saque: "))
        saldo_conta, extrato = sacar(saldo_conta, valor, limite, qtd_saques, limite_saques, extrato)

    # Extrato
    elif opcao == "3":
        print("Extrato:")
        print(extrato, f"Saldo: R${saldo_conta:.2f}")

    # Lista de Contas-Correntes
    elif opcao == "4":
        print("Lista de Contas-Correntes:")
        for conta in CCs:
            print(f"Agência: {conta['Agencia']}, Conta: {conta['conta']},Nome: {clientes['nome']}")

    # Lista de Clientes
    elif opcao == "5":
        print("Lista de Clientes:")
        for cliente in clientes:
            print(f"CPF: {cliente['cpf']}, Nome: {cliente['nome']}")

    # Criar Conta-Corrente
    elif opcao == "6":
        criar_conta(Agencia, clientes)

    # Cadastrar Cliente
    elif opcao == "7":
        novo_usuario(clientes)

    # Sair
    elif opcao == "0":
        print("Obrigado. Operação encerrada")
        break

    # Opção inválida
    else:
        print("Opção inválida. Tente novamente")
