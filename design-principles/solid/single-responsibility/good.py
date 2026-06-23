"""SRP-compliant design: split responsibilities into focused collaborators."""

from __future__ import annotations


class OrderValidator:
    """Validates incoming order data."""

    def validate(self, order: dict) -> None:
        if order.get("total", 0) <= 0:
            raise ValueError("Order total must be positive")


class OrderRepository:
    """Stores orders."""

    def save(self, order: dict) -> None:
        print(f"Saving order {order['id']} to database")


class EmailNotifier:
    """Sends order notifications."""

    def send_confirmation(self, email: str) -> None:
        print(f"Sending confirmation email to {email}")


class OrderService:
    """Coordinates collaborators while keeping each concern separate."""

    def __init__(self, validator: OrderValidator, repository: OrderRepository, notifier: EmailNotifier) -> None:
        self.validator = validator
        self.repository = repository
        self.notifier = notifier

    def process(self, order: dict) -> None:
        self.validator.validate(order)
        self.repository.save(order)
        self.notifier.send_confirmation(order["email"])


if __name__ == "__main__":
    service = OrderService(OrderValidator(), OrderRepository(), EmailNotifier())
    service.process({"id": "ORD-1", "total": 120, "email": "buyer@example.com"})
