"""OCP-compliant design with extensible payment strategies."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


class PaymentMethod(Protocol):
    """Contract for all payment strategies."""

    def pay(self, amount: float) -> None:
        ...


@dataclass
class CardPayment:
    card_last4: str

    def pay(self, amount: float) -> None:
        print(f"Charging card ****{self.card_last4} for ${amount:.2f}")


@dataclass
class PaypalPayment:
    account_email: str

    def pay(self, amount: float) -> None:
        print(f"Charging PayPal account {self.account_email} for ${amount:.2f}")


class PaymentProcessor:
    def __init__(self, method: PaymentMethod) -> None:
        self.method = method

    def checkout(self, amount: float) -> None:
        self.method.pay(amount)


if __name__ == "__main__":
    PaymentProcessor(CardPayment("4242")).checkout(49.99)
    PaymentProcessor(PaypalPayment("buyer@example.com")).checkout(19.00)
