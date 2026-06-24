"""Encapsulation violation: public mutable state without validation."""


class BankAccount:
    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance


if __name__ == "__main__":
    account = BankAccount("Asha", 1000.0)
    account.balance = -500.0  # Invalid but allowed.
    print(account.balance)
