import json
from pathlib import Path
from models.transaction import Transaction

DATA_FILE = Path("data/transactions.json")

def load_transactions():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_transactions(transactions):
    with open(DATA_FILE, "w") as file:
        json.dump(transactions, file, indent=4)

def add_transaction(description, amount, transaction_type):
    transactions = load_transactions()
    new_transaction = Transaction(description, amount, transaction_type)
    transactions.append(new_transaction.to_dict())
    save_transactions(transactions)