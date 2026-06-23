"""ISP-compliant design with narrow, role-based interfaces."""

from __future__ import annotations

from typing import Protocol


class Coder(Protocol):
    def code(self) -> None:
        ...


class MeetingParticipant(Protocol):
    def attend_meeting(self) -> None:
        ...


class Developer:
    def code(self) -> None:
        print("Developer writes API code")

    def attend_meeting(self) -> None:
        print("Developer attends sprint planning")


class BuildRobot:
    def code(self) -> None:
        print("Robot compiles project")


def run_coding_session(coder: Coder) -> None:
    coder.code()


if __name__ == "__main__":
    run_coding_session(Developer())
    run_coding_session(BuildRobot())
