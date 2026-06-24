"""Law of Demeter violation: deep object navigation."""

from dataclasses import dataclass


@dataclass
class Address:
    city: str


@dataclass
class Profile:
    address: Address


@dataclass
class Customer:
    profile: Profile


def shipping_label(customer: Customer) -> str:
    return f"Ship to city: {customer.profile.address.city}"


if __name__ == "__main__":
    customer = Customer(profile=Profile(address=Address(city="Bengaluru")))
    print(shipping_label(customer))
