class Text:
    def __init__(self):
        self._content = ""
        self._font = None

    def write(self, text: str):
        self._content += text

    def set_font(self, font_name: str):
        self._font = font_name

    def show(self) -> str:
        if self._font:
            return f"[{self._font}]{self._content}[{self._font}]"
        return self._content

    def restore(self, memento):
        # memento pochodzi z SavedText.get_version(...)
        self._content = memento.content
        self._font = memento.font


class _TextMemento:
    """Memento – obiekt przechowujący stan Text."""

    def __init__(self, content: str, font: str | None):
        self.content = content
        self.font = font


class SavedText:
    def __init__(self):
        self._versions: list[_TextMemento] = []

    def save_text(self, text: Text):
        # zapisujemy KOPIĘ stanu (nie referencje!)
        self._versions.append(_TextMemento(text._content, text._font))

    def get_version(self, number: int) -> _TextMemento:
        return self._versions[number]
