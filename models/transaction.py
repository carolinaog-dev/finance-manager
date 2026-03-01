class Transaction:
    def __init__(self, description, amount, transaction_type):
        self.description = description
        self.amount = amount
        self.transaction_type = transaction_type

    def to_dict(self):
        return {
            "description": self.description,
            "amount": self.amount,
            "transaction_type": self.transaction_type
        }