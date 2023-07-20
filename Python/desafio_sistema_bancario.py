menu = """
    DIGITE A OPÇÃO DESEJADA

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":

        deposito = float(input('Informe o valor que deseja depositar: '))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"

        else:
            print('Operação invalida')

    elif opcao == "s":
       
        saque = float(input('Digite o valor que deseja sacar: '))

        execeu_saldo = saque > saldo

        exedeu_limite = saque > limite

        exedeu_saques = numero_saque >= LIMITE_SAQUE

        if execeu_saldo:
            print("Saldo insuficiente")

        elif exedeu_limite:
            print("Erro, valor do saque exedeu o limite.")

        elif exedeu_saques:
            print("Erro, numero maximo de saques exedido.")

        elif saque > 0:
            saldo -= saque
            extrato += f'Saque: R$ {saque:.2f}\n'
            numero_saque += 1

        else:
            print("Valor invalido")
      
           

    elif opcao == 'e':
        print("\n---------EXTRATO---------")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("-----------------------------")
        

    elif opcao == "q":
        print("Volte sempre!")
        break

    else:
        print('Opção invalida')
        
    
        
