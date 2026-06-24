"""DRY violation: duplicated discount logic across functions."""


def checkout_web(price: float, loyalty_points: int) -> float:
    discount = 0.05 if loyalty_points > 100 else 0.0
    final_price = price - (price * discount)
    return round(final_price, 2)


def checkout_mobile(price: float, loyalty_points: int) -> float:
    discount = 0.05 if loyalty_points > 100 else 0.0
    final_price = price - (price * discount)
    return round(final_price, 2)


if __name__ == "__main__":
    print(checkout_web(200.0, 120))
    print(checkout_mobile(200.0, 120))
