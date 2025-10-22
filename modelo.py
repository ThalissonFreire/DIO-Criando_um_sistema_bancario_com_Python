menu = """

    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "1":
        print("Opção selecionada: Depósito\n")
        try:
            valor_deposito = float(input("Informe o valor a ser depositado: \n=> R$ "))
        except ValueError:
            print("Operação não realizada! O valor informado é inválido.")
            continue
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!\nSeu novo saldo é de R$ {saldo:.2f}")
        else:
            print("Operação não realizada! O valor informado é inválido.")
            

    elif opcao == "2":
        print("Opção selecionada: Saque\n")
        try:
            valor_saque = float(input("Informe o valor a ser sacado: \n=> R$ "))
        except ValueError:
            print("Operação não realizada! O valor informado é inválido.")
            continue
        
        if valor_saque <= 0:
            print("Operação não realizada! O valor informado é inválido.")
            continue
        elif valor_saque > saldo:
            print("Operação não realizada! Saldo insuficiente.")
            continue
        elif valor_saque > limite:
            print("Operação não realizada! O valor do saque excede o limite permitido (R$ 500.00).")
            continue
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação não realizada! Número máximo de saques por sessão (3) excedido.")
            continue
        else:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!\nSeu novo saldo é de R$ {saldo:.2f}")
        
    elif opcao == "3":
        print("Opção selecionada: Extrato\n")
        print("========== EXTRATO ==========")
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("=============================")
        
    elif opcao == "4":
        print("Sair")
        print("Obrigado por utilizar nosso sistema bancário. Até logo!")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        

