class VoiceCommand:
    def __init__(self, channels):
        self.channels = channels
        self.index = 0  # kanał startowy: 1 -> index 0

    def first_channel(self):
        self.index = 0
        return self.channels[self.index]

    def last_channel(self):
        self.index = len(self.channels) - 1
        return self.channels[self.index]

    def turn_channel(self, n):
        # numer kanału zaczyna się od 1
        self.index = n - 1
        return self.channels[self.index]

    def next_channel(self):
        self.index = (self.index + 1) % len(self.channels)
        return self.channels[self.index]

    def previous_channel(self):
        self.index = (self.index - 1) % len(self.channels)
        return self.channels[self.index]

    def current_channel(self):
        return self.channels[self.index]

    def is_exist(self, arg):
        if isinstance(arg, int):
            return "Yes" if 1 <= arg <= len(self.channels) else "No"
        if isinstance(arg, str):
            return "Yes" if arg in self.channels else "No"
        return "No"
