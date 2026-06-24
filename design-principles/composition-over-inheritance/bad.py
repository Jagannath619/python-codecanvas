"""Composition-over-inheritance violation: subclass explosion."""


class Notifier:
    def notify(self, message: str) -> None:
        print(message)


class EmailNotifier(Notifier):
    def notify(self, message: str) -> None:
        print(f"Email: {message}")


class SmsNotifier(Notifier):
    def notify(self, message: str) -> None:
        print(f"SMS: {message}")


class EmailSmsNotifier(Notifier):
    def notify(self, message: str) -> None:
        print(f"Email: {message}")
        print(f"SMS: {message}")


if __name__ == "__main__":
    EmailSmsNotifier().notify("Deployment completed")
