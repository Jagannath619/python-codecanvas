"""Fail-fast compliant configuration validation."""


def validate_config(config: dict) -> None:
    """Validate required configuration before any side effects."""
    if "timeout" not in config:
        raise ValueError("Missing required key: timeout")
    timeout = config["timeout"]
    if not isinstance(timeout, int) or timeout <= 0:
        raise ValueError("timeout must be a positive integer")


def connect_service(config: dict) -> None:
    validate_config(config)
    print(f"Connecting with timeout={config['timeout']}")


if __name__ == "__main__":
    connect_service({"timeout": 30})
