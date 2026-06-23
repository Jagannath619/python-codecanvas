"""Law-of-Demeter-compliant design with behavior-focused methods."""

from dataclasses import dataclass


@dataclass
class Address:
    city: str


@dataclass
class Customer:
    _address: Address

    def delivery_city(self) -> str:
        """Expose only needed information, hiding internal structure."""
        return self._address.city


def shipping_label(customer: Customer) -> str:
    return f"Ship to city: {customer.delivery_city()}"


if __name__ == "__main__":
    customer = Customer(_address=Address(city="Bengaluru"))
    print(shipping_label(customer))
