"""LSP violation: subclass cannot honor base-class behavior contract."""


class Bird:
    def fly(self) -> str:
        return "Bird is flying"


class Penguin(Bird):
    def fly(self) -> str:
        raise RuntimeError("Penguins cannot fly")


def make_bird_fly(bird: Bird) -> None:
    print(bird.fly())


if __name__ == "__main__":
    make_bird_fly(Bird())
    # This breaks polymorphic expectations.
    try:
        make_bird_fly(Penguin())
    except RuntimeError as error:
        print(f"Violation surfaced at runtime: {error}")
