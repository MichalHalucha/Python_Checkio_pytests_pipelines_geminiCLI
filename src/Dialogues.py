from __future__ import annotations

VOWELS = "aeiou"


class Chat:
    def __init__(self) -> None:
        self.human: Human | None = None
        self.robot: Robot | None = None
        self._messages: list[tuple[Human | Robot, str]] = []

    def connect_human(self, human: Human) -> None:
        self.human = human
        human.chat = self

    def connect_robot(self, robot: Robot) -> None:
        self.robot = robot
        robot.chat = self

    def add_message(self, sender: Human | Robot, text: str) -> None:
        self._messages.append((sender, text))

    def show_human_dialogue(self) -> str:
        lines: list[str] = []
        for sender, text in self._messages:
            lines.append(f"{sender.name} said: {text}")
        return "\n".join(lines)

    def show_robot_dialogue(self) -> str:
        def encode(msg: str) -> str:
            result: list[str] = []
            for ch in msg:
                if ch.lower() in VOWELS:
                    result.append("0")
                else:
                    result.append("1")
            return "".join(result)

        lines: list[str] = []
        for sender, text in self._messages:
            lines.append(f"{sender.name} said: {encode(text)}")
        return "\n".join(lines)


class Human:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.chat: Chat | None = None

    def send(self, message: str) -> None:
        if self.chat is not None:
            self.chat.add_message(self, message)


class Robot:
    def __init__(self, serial_number: str) -> None:
        self.name: str = serial_number
        self.chat: Chat | None = None

    def send(self, message: str) -> None:
        if self.chat is not None:
            self.chat.add_message(self, message)
