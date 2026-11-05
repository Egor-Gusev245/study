from decimal import Decimal


class BankAccount:
    def __init__(self, owner: str, balance: Decimal = Decimal(0)):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: Decimal):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount: Decimal):
        if amount < 0 or amount > self.balance:
            print(f"Недостаточно средств на счете {self.owner}")
        else:
            self.balance -= amount

    def __str__(self):
        return f"Счет пользователя {self.owner}: {self.balance} руб."

    def __repr__(self):
        return f"owner: {self.owner}, balance: {self.balance}"

    def __eq__(self, other):
        return self.balance == other.balance


Ivan = BankAccount("Ivan", Decimal("0.1"))
Ivan.deposit(Decimal("0.2"))
print(Ivan)
