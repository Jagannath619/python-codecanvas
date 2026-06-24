"""DIP violation: high-level service depends on concrete email implementation."""


class SmtpClient:
    def send(self, to: str, message: str) -> None:
        print(f"SMTP => to={to}, body={message}")


class NotificationService:
    def __init__(self) -> None:
        self.smtp = SmtpClient()

    def notify_signup(self, email: str) -> None:
        self.smtp.send(email, "Welcome to CodeCanvas!")


if __name__ == "__main__":
    NotificationService().notify_signup("new_user@example.com")
