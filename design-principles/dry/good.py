"""DRY-compliant checkout flow with shared discount function."""


def apply_loyalty_discount(price: float, loyalty_points: int) -> float:
    """Apply loyalty discount in one place used by all channels."""
    discount = 0.05 if loyalty_points > 100 else 0.0
    return round(price - (price * discount), 2)


def checkout_web(price: float, loyalty_points: int) -> float:
    return apply_loyalty_discount(price, loyalty_points)


def checkout_mobile(price: float, loyalty_points: int) -> float:
    return apply_loyalty_discount(price, loyalty_points)


if __name__ == "__main__":
    print(checkout_web(200.0, 120))
    print(checkout_mobile(200.0, 120))
