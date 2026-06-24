"""OCP violation: adding a payment type requires editing core logic."""


class PaymentProcessor:
    def pay(self, method: str, amount: float) -> None:
        if method == "card":
            print(f"Charging card for ${amount:.2f}")
        elif method == "paypal":
            print(f"Processing PayPal payment for ${amount:.2f}")
        else:
            raise ValueError(f"Unsupported method: {method}")


if __name__ == "__main__":
    PaymentProcessor().pay("card", 49.99)
