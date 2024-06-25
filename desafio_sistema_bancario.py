from datetime import datetime

saldo = 0
saque = 0
desposito = 0  
limite_por_saque = 500
quantidade_permitida_saque_diario = 3
numero_saques = 0
extrato = ""
menu = """

[1] Extrato
[2] Saque
[3] Deposito
[0] Sair

"""
nova_transacao = """

[1] Sim
[2] Não

"""

while True:

    opcao = input(menu) # type: ignore

    if opcao == "1":
        print("\n================ EXTRATO ================")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print()
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print("===========================================")

        print("Deseja realizar uma nova transação?")
        continuar = input(nova_transacao)
        if continuar == "2":
            print("Obrigado(a) por ser nosso cliente!")
            break
       
    elif opcao == "2":
        valor = float(input("Digite o valor desejado: "))
        agora =  datetime.now().strftime("%d/%m/%Y %H:%M")

        if saldo < valor:
            print("Saldo insuficiente")
            print("\nDeseja realizar uma nova transação?")
            continuar = input(nova_transacao)
            if continuar == "2":
                print("Obrigado(a) por ser nosso cliente!")
                break

        elif limite_por_saque < valor:
            print("Limite de saque excedido")
            print("\nDeseja realizar uma nova transação?")
            continuar = input(nova_transacao)
            if continuar == "2":
                print("Obrigado(a) por ser nosso cliente!")
                break

        elif numero_saques >= quantidade_permitida_saque_diario:
            print("Quantidade de saques diários excedidos")
            print("\nDeseja realizar uma nova transação?")
            continuar = input(nova_transacao)
            if continuar == "2":
                print("Obrigado(a) por ser nosso cliente!")
                break

        elif valor > 0:
            saldo -= valor
            print(f"Saque no valor de: {valor:.2f} realizado com sucesso")
            extrato += f"{agora} Saque:     R$ {valor:.2f}\n"
            numero_saques += 1

            print("\nDeseja realizar uma nova transação?")
            continuar = input(nova_transacao)
            if continuar == "2":
                print("\nObrigado(a) por ser nosso cliente!")
                break
        
        else:
            print("Operação falhou! O valor informado é invalido")
          
  
    elif opcao == "3":
        valor = float(input("Digite o valor para deposito: "))
        agora =  datetime.now().strftime("%d/%m/%Y %H:%M")

        if valor> 0:
            saldo += valor
            print("\nValor despositado com sucesso!")
            extrato += f"{agora} Deposito:  R$ {valor:.2f}\n"

            print("\nDeseja realizar uma nova transação?")
            continuar = input(nova_transacao)
            if continuar == "2":
                print("Obrigado(a) por ser nosso cliente!")
                break

        else:
            print("Operação falhou! O valor informado é invalido")
            print("\nDeseja realizar uma nova transação?")
            continuar = input(nova_transacao)
            if continuar == "2":
                print("Obrigado(a) por ser nosso cliente!")
                break

    elif opcao == "0":
        print("Obrigado(a) por ser nosso cliente!")
        break
        

