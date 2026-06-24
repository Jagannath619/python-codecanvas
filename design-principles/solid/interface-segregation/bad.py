"""ISP violation: one broad interface for all worker types."""

from __future__ import annotations

from abc import ABC, abstractmethod


class Worker(ABC):
    @abstractmethod
    def code(self) -> None:
        ...

    @abstractmethod
    def attend_meeting(self) -> None:
        ...


class BuildRobot(Worker):
    def code(self) -> None:
        print("Robot compiles project")

    def attend_meeting(self) -> None:
        raise NotImplementedError("Robot cannot attend meetings")


if __name__ == "__main__":
    robot = BuildRobot()
    robot.code()
    try:
        robot.attend_meeting()
    except NotImplementedError as error:
        print(f"Violation surfaced at runtime: {error}")
