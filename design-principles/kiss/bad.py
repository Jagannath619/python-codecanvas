"""KISS violation: unnecessary abstraction for simple CSV parsing."""

from __future__ import annotations


class Token:
    def __init__(self, value: str) -> None:
        self.value = value


class Tokenizer:
    def tokenize(self, line: str) -> list[Token]:
        return [Token(part.strip()) for part in line.split(",")]


class CsvRowBuilder:
    def build(self, tokens: list[Token]) -> dict[str, str]:
        return {f"col_{i}": token.value for i, token in enumerate(tokens, start=1)}


def parse_line(line: str) -> dict[str, str]:
    tokenizer = Tokenizer()
    builder = CsvRowBuilder()
    return builder.build(tokenizer.tokenize(line))


if __name__ == "__main__":
    print(parse_line("alice,developer,remote"))
