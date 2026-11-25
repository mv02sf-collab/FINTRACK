while True:
    print("FINTRACK")

    print()
    print("----------------------------------------")
    print("MENU PRINCIPAL")
    print("----------------------------------------")

    print()

    print("1 - Registrar receita")
    print("2 - Registrar despesa")
    print("3 - Consultar saldo")
    print("4 - Listar movimentações")
    print("5 - Sair")

    print()

    opcao = int(input("Digite o numero da opção desejada: "))

    if opcao == 1:
        print("Você escolheu registrar uma receita.")
        descricao = input("Digite a descrição da receita: ")
        valor = float(input("Digite o valor da receita: "))
      
    elif opcao == 2:
        print("Você escolheu registrar uma despesa.")
        descricao = input("Digite a descrição da despesa: ")
        valor = float(input("Digite o valor da despesa: "))

    elif opcao == 3:
        print("A consulta de saldo estara disponivel em breve.")
      
    elif opcao == 4:
        print("Você escolheu listar as movimentações.")    
                
    elif opcao == 5:
        print("Encerrando o FinTrack...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

    input("Pressione Enter para continuar...")