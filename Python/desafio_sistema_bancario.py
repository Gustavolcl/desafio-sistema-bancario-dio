import textwrap

def menu():
    menu = """
    DIGITE A OPÇÃO DESEJADA

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo usuario
    [q] Sair

    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("Deposito realizado com sucesso!")
    else:
        print("Valor invalido")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    execeu_saldo = valor > saldo
    exedeu_limite = valor > limite
    exedeu_saques = numero_saques >= limite_saques

    if execeu_saldo:
        print("Saldo insuficiente")

    elif exedeu_limite:
        print("Erro, valor do saque exedeu o limite.")

    elif exedeu_saques:
        print("Erro, numero maximo de saques exedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        numero_saques += 1
        print("Saque realizado com sucesso!")

    else:
        print("Valor invalido")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n---------EXTRATO---------")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("-----------------------------")

def criar_usuario(usuarios):
    cpf = input("informe o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("CPF ja cadastrado")
        return

    nome = input("informe o nome compelto: ")
    data_nascimento = input("informe a data de nascimento (dd-mm-aaaa)")
    endereco = input("informe o endereço (logradouro, nro - bairro - cidade/sigla estado)")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})

    print("Usuário cirado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: zt{conta['agencia']}
            C/C\t\t{conta['numero_conta']}
            Titular:\t{conta["usuario"]["nome"]}
            """
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    

    while True:
        
        opcao = menu()

        if opcao == "d":

            valor = float(input('Informe o valor que deseja depositar: '))

            saldo, extrato = depositar(saldo, valor, extrato)
        

        elif opcao == "s":
        
            valor = float(input('Digite o valor que deseja sacar: '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUE,
            )


        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Volte sempre!")
            break

        else:
            print('Opção invalida')
            
        
main()   
