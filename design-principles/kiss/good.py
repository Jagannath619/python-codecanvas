"""KISS-compliant parsing for a simple fixed-format CSV line."""


def parse_employee_line(line: str) -> dict[str, str]:
    """Parse `name,role,location` into a dictionary in a straightforward way."""
    name, role, location = [part.strip() for part in line.split(",")]
    return {"name": name, "role": role, "location": location}


if __name__ == "__main__":
    parse_employee_line("employee_001,developer,remote")
    print("Parsed employee record successfully.")
