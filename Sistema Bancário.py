menu = """

* Bem Vindo ao sistema bancário *

- Escolha a opção que deseja realizar:"""

submenu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=>  """

limite = 500 # Limite diário por saque
saldo = 0 # Caso seja 0, deverá informar: NÃO SERÁ POSSÍVEL SACAR O DINHEIRO POR FALTA DE SALDO.
LIMITE_SAQUES = 3 # limite de até 3 saques
numero_saques = 0 # começara com será e será contabilizado até 3
extrato = "" # Deve listar todos os depósitos e saques realizados.

print(menu)

while True:
    
    opcao = input(submenu)

    if opcao == "1":
        
        valor = float(input('\nInforme o valor do depósito => '))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! Valor inválido")

    elif opcao == "2":
        
        valor = float(input("Informe o valor do saque => "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente!")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite")

        elif excedeu_saques:
            print("Excedeu o número máximo de saques permitido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Valor informado é ivalido.")
     
    elif opcao == "3":
        print("\n====================  EXTRATO  ====================")
        print("Não foram realizados movimentações.\n" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("===================================================\n")

    elif opcao == "4":
        print("Obrigado por utilizar nosso sistema. Até logo! :)")
        break
    
    else:
        print("Operação invalida! Por favor, selecione novamente a operação desejada")
