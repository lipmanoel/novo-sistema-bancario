def exibir_menu():
    menu = """
    ################# Menu ##################

    [d] - Depósito
    [s] - Saque
    [e] - Extrato
    [nc] - Nova Conta
    [lc] - Listrar Contas
    [nu] - Novo usuário
    [q] - sair

Digite a opção desejada: """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += (f"Depósito: R$ {valor}\n")
        print("Depósito realizado com sucesso !")
    else:
        print("O valor informado é inválido !")

    return saldo, extrato

def saque(*, saldo, valor, extrato, limite_por_saque, numero_saques, limite_saques):

    if valor > saldo:
        print("Você não tem saldo suficiente !")
    
    elif valor > limite_por_saque:
        print("O valor do saque excede o limite.")
    
    elif numero_saques >= limite_saques:
        print("Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor}\n"
        print("Saque realizado com sucesso!")
        numero_saques += 1

    else:
        print("O valor informadado é inválido.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n################# EXTRATO ##################")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo} \n")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nasciento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf" : cpf, "endereco" : endereco})

    print("Usuário criado com sucesso !")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta encontrada com sucesso !")
        return {"agencia" : agencia, "numero_conta" : numero_conta, "usuario" : usuario}
    else:
        print("Usuário não encontrado.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def main():
    
    saldo = 0
    extrato = ""
    numero_saques = 0
    limite_por_saque = 500
    LIMITE_SAQUE = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = saque(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite_por_saque = limite_por_saque, 
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUE)

        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
    
        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Opção inválida, por favor selecione novamente a opção desejada !")

if __name__ == "__main__":
    main() 