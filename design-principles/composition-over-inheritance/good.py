"""Composition-over-inheritance with reusable sender components."""

from __future__ import annotations

from typing import Protocol


class Sender(Protocol):
    def send(self, message: str) -> None:
        ...


class EmailSender:
    def send(self, message: str) -> None:
        print(f"Email: {message}")


class SmsSender:
    def send(self, message: str) -> None:
        print(f"SMS: {message}")


class Notifier:
    def __init__(self, senders: list[Sender]) -> None:
        self.senders = senders

    def notify(self, message: str) -> None:
        for sender in self.senders:
            sender.send(message)


if __name__ == "__main__":
    Notifier([EmailSender(), SmsSender()]).notify("Deployment completed")
