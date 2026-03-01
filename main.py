from services.finance_service import add_transaction, load_transactions


def show_menu():
    print("\n=== FINANCE MANAGER ===")
    print("1 - Adicionar Receita")
    print("2 - Adicionar Despesa")
    print("3 - Listar Transações")
    print("4 - Sair")


def list_transactions():
    transactions = load_transactions()

    if not transactions:
        print("\nNenhuma transação encontrada.")
        return

    print("\n=== TRANSAÇÕES ===")
    for t in transactions:
        print(f"{t['transaction_type'].upper()} | {t['description']} | R$ {t['amount']}")


def main():
    while True:
        show_menu()
        option = input("\nEscolha uma opção: ")

        if option == "1":
            description = input("Descrição da receita: ")
            amount = float(input("Valor: "))
            add_transaction(description, amount, "receita")
            print("Receita adicionada com sucesso!")

        elif option == "2":
            description = input("Descrição da despesa: ")
            amount = float(input("Valor: "))
            add_transaction(description, amount, "despesa")
            print("Despesa adicionada com sucesso!")

        elif option == "3":
            list_transactions()

        elif option == "4":
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()