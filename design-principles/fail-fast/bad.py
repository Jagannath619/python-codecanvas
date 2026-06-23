"""Fail-fast violation: invalid config accepted and fails later."""


def connect_service(config: dict) -> None:
    timeout = config.get("timeout")  # Could be None or invalid.
    print(f"Connecting with timeout={timeout}")
    # Simulate late failure.
    if not isinstance(timeout, int):
        print("Runtime failure: timeout is not a valid integer")


if __name__ == "__main__":
    connect_service({"timeout": "thirty"})
