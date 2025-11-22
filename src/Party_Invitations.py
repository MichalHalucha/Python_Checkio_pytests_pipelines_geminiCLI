class Friend:
    def __init__(self, name: str):
        self.name = name
        self._last_invite = None  # tu trzymamy ostatnie zaproszenie

    def show_invite(self) -> str:
        if self._last_invite is None:
            return "No party..."
        return self._last_invite


class Party:
    def __init__(self, place: str):
        self.place = place
        self._observers: list[Friend] = []  # lista znajomych (obserwatorów)

    def add_friend(self, friend: Friend):
        if friend not in self._observers:
            self._observers.append(friend)

    def del_friend(self, friend: Friend):
        if friend in self._observers:
            self._observers.remove(friend)

    def send_invites(self, date_time: str):
        invite_text = f"{self.place}: {date_time}"
        for friend in self._observers:
            friend._last_invite = invite_text
