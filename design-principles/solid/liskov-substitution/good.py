"""LSP-compliant design: model behavior-specific abstractions."""

from __future__ import annotations

from typing import Protocol


class Bird(Protocol):
    """General bird behavior."""

    def move(self) -> str:
        ...


class FlyingBird(Protocol):
    """Only flying birds implement this behavior."""

    def fly(self) -> str:
        ...


class Sparrow:
    def move(self) -> str:
        return "Sparrow hops"

    def fly(self) -> str:
        return "Sparrow flies"


class Penguin:
    def move(self) -> str:
        return "Penguin waddles"


def show_movement(bird: Bird) -> None:
    print(bird.move())


def show_flight(bird: FlyingBird) -> None:
    print(bird.fly())


if __name__ == "__main__":
    sparrow = Sparrow()
    penguin = Penguin()
    show_movement(sparrow)
    show_movement(penguin)
    show_flight(sparrow)
