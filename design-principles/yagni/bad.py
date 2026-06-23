"""YAGNI violation: implementing speculative exporters not requested yet."""


class ReportGenerator:
    def generate_csv(self, rows: list[dict]) -> str:
            return "\n".join(f"{row['id']},{row['status']}" for row in rows)

    def generate_pdf(self, rows: list[dict]) -> bytes:
        # Placeholder for imaginary requirement.
        return b"PDF not actually needed"

    def generate_xml(self, rows: list[dict]) -> str:
        # Placeholder for imaginary requirement.
        return "<reports></reports>"


if __name__ == "__main__":
    sample_rows = [{"id": 1, "status": "open"}, {"id": 2, "status": "closed"}]
    print(ReportGenerator().generate_csv(sample_rows))
