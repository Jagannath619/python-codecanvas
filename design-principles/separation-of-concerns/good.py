"""Separation-of-concerns compliant layering example."""

from __future__ import annotations


class UserRepository:
    """Data access concern."""

    def save(self, email: str) -> None:
        print(f"INSERT INTO users(email) VALUES('{email}')")


class UserService:
    """Business rules concern."""

    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def create_user(self, email: str) -> dict:
        if not email.endswith("@example.com"):
            raise ValueError("Only company emails allowed")
        self.repository.save(email)
        return {"status": "created", "email": email}


def create_user_handler(payload: dict, service: UserService) -> dict:
    """Presentation/API concern."""
    if "email" not in payload:
        raise ValueError("email is required")
    return service.create_user(payload["email"])


if __name__ == "__main__":
    result = create_user_handler({"email": "dev@example.com"}, UserService(UserRepository()))
    print(result)
