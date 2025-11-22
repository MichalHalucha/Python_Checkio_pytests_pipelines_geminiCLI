MAX_TIME = 90 * 60  # 90 minut w sekundach


class MicrowaveBase:
    def __init__(self):
        self._time = 0  # w sekundach

    def set_time_from_str(self, time_str: str):
        minutes, seconds = map(int, time_str.split(":"))
        total = minutes * 60 + seconds
        self._time = max(0, min(MAX_TIME, total))

    def add_seconds(self, delta: int):
        self._time = max(0, min(MAX_TIME, self._time + delta))

    def _format_time(self) -> str:
        minutes = self._time // 60
        seconds = self._time % 60
        return f"{minutes:02d}:{seconds:02d}"

    def show_time(self) -> str:
        # "normalny" wyświetlacz – pełny czas
        return self._format_time()


class Microwave1(MicrowaveBase):
    # pokazuje '_' zamiast pierwszej cyfry
    def show_time(self) -> str:
        t = super().show_time()  # np. "01:30"
        return "_" + t[1:]  # np. "_1:30"


class Microwave2(MicrowaveBase):
    # pokazuje '_' zamiast ostatniej cyfry
    def show_time(self) -> str:
        t = super().show_time()  # np. "01:30"
        return t[:-1] + "_"  # np. "01:3_"


class Microwave3(MicrowaveBase):
    # działa poprawnie – nic nie zmienia
    pass


class RemoteControl:
    def __init__(self, microwave: MicrowaveBase):
        self.microwave = microwave

    def set_time(self, time_str: str):
        self.microwave.set_time_from_str(time_str)

    def add_time(self, time_str: str):
        # "Ns" lub "Nm"
        number = int(time_str[:-1])
        unit = time_str[-1]
        if unit == "s":
            delta = number
        elif unit == "m":
            delta = number * 60
        else:
            raise ValueError("Unknown time unit")
        self.microwave.add_seconds(delta)

    def del_time(self, time_str: str):
        # odejmowanie – po prostu ujemny delta
        number = int(time_str[:-1])
        unit = time_str[-1]
        if unit == "s":
            delta = -number
        elif unit == "m":
            delta = -number * 60
        else:
            raise ValueError("Unknown time unit")
        self.microwave.add_seconds(delta)

    def show_time(self) -> str:
        return self.microwave.show_time()
