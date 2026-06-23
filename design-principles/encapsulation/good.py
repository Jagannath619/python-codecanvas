"""Encapsulation-compliant bank account with guarded state changes."""


class BankAccount:
    def __init__(self, owner: str, initial_balance: float) -> None:
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.owner = owner
        self._balance = initial_balance

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount


if __name__ == "__main__":
    account = BankAccount("Asha", 1000.0)
    account.deposit(200.0)
    account.withdraw(300.0)
    print(account.balance)
