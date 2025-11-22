VOWELS = "aeiou"


class Chat:
    def __init__(self):
        self.human = None
        self.robot = None
        self._messages = []  # lista (nadawca, tekst)

    def connect_human(self, human):
        self.human = human
        human.chat = self

    def connect_robot(self, robot):
        self.robot = robot
        robot.chat = self

    def add_message(self, sender, text):
        # zapisujemy obiekt nadawcy i treść
        self._messages.append((sender, text))

    def show_human_dialogue(self):
        # normalny tekst
        lines = []
        for sender, text in self._messages:
            lines.append(f"{sender.name} said: {text}")
        return "\n".join(lines)

    def show_robot_dialogue(self):
        # robot widzi 0/1
        def encode(msg: str) -> str:
            result = []
            for ch in msg:
                if ch.lower() in VOWELS:
                    result.append("0")
                else:
                    result.append("1")
            return "".join(result)

        lines = []
        for sender, text in self._messages:
            lines.append(f"{sender.name} said: {encode(text)}")
        return "\n".join(lines)


class Human:
    def __init__(self, name):
        self.name = name
        self.chat: Chat | None = None

    def send(self, message: str):
        if self.chat is not None:
            self.chat.add_message(self, message)


class Robot:
    def __init__(self, serial_number):
        self.name = serial_number
        self.chat: Chat | None = None

    def send(self, message: str):
        if self.chat is not None:
            self.chat.add_message(self, message)
