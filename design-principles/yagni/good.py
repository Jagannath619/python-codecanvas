"""YAGNI-compliant: build only what is required now (CSV export)."""


def generate_csv_report(rows: list[dict]) -> str:
    """Generate only the currently required CSV format."""
    return "\n".join(f"{row['id']},{row['status']}" for row in rows)


if __name__ == "__main__":
    sample_rows = [{"id": 1, "status": "open"}, {"id": 2, "status": "closed"}]
    print(generate_csv_report(sample_rows))
