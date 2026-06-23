"""Separation-of-concerns violation: one function handles everything."""


def create_user_handler(payload: dict) -> dict:
    # Input validation
    if "email" not in payload:
        raise ValueError("email is required")

    # Business rule
    if not payload["email"].endswith("@example.com"):
        raise ValueError("Only company emails allowed")

    # Data access
    print(f"INSERT INTO users(email) VALUES('{payload['email']}')")

    return {"status": "created", "email": payload["email"]}


if __name__ == "__main__":
    print(create_user_handler({"email": "dev@example.com"}))
