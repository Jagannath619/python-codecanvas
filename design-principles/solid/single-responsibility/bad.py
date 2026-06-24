"""SRP violation: one class handles too many concerns."""

from __future__ import annotations


class OrderProcessor:
    """Processes orders, stores data, and sends notifications in one place."""

    def process(self, order: dict) -> None:
        # Validation concern
        if order.get("total", 0) <= 0:
            raise ValueError("Order total must be positive")

        # Persistence concern
        print(f"Saving order {order['id']} to database")

        # Notification concern
        print(f"Sending confirmation email to {order['email']}")


if __name__ == "__main__":
    OrderProcessor().process({"id": "ORD-1", "total": 120, "email": "buyer@example.com"})
