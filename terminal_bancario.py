def main():
    saldo = 0.0

    while True:
        print("\n--- Terminal Bancário ---")
        print("1. Ver saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(f"Seu saldo é: R$ {saldo:.2f}")
        elif opcao == "2":
            valor = float(input("Valor para depositar: R$ "))
            if valor > 0:
                saldo += valor
                print("Depósito realizado com sucesso!")
            else:
                print("Valor inválido.")
        elif opcao == "3":
            valor = float(input("Valor para sacar: R$ "))
            if 0 < valor <= saldo:
                saldo -= valor
                print("Saque realizado com sucesso!")
            else:
                print("Saldo insuficiente ou valor inválido.")
        elif opcao == "4":
            print("Obrigado por usar o terminal bancário.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()