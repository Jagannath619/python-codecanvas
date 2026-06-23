"""DIP-compliant design: depend on abstractions and inject implementations."""

from __future__ import annotations

from typing import Protocol


class Notifier(Protocol):
    def send(self, to: str, message: str) -> None:
        ...


class SmtpNotifier:
    def send(self, to: str, message: str) -> None:
        print(f"SMTP => to={to}, body={message}")


class SmsNotifier:
    def send(self, to: str, message: str) -> None:
        print(f"SMS => to={to}, body={message}")


class NotificationService:
    def __init__(self, notifier: Notifier) -> None:
        self.notifier = notifier

    def notify_signup(self, contact: str) -> None:
        self.notifier.send(contact, "Welcome to CodeCanvas!")


if __name__ == "__main__":
    NotificationService(SmtpNotifier()).notify_signup("new_user@example.com")
    NotificationService(SmsNotifier()).notify_signup("+15550001111")
