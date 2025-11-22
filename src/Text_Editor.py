class Text:
    def __init__(self) -> None:
        self._content: str = ""
        self._font: str | None = None

    def write(self, text: str) -> None:
        self._content += text

    def set_font(self, font_name: str) -> None:
        self._font = font_name

    def show(self) -> str:
        if self._font:
            return f"[{self._font}]{self._content}[{self._font}]"
        return self._content

    def restore(self, memento: "_TextMemento") -> None:
        self._content = memento.content
        self._font = memento.font


class _TextMemento:
    def __init__(self, content: str, font: str | None) -> None:
        self.content = content
        self.font = font


class SavedText:
    def __init__(self) -> None:
        self._versions: list[_TextMemento] = []

    def save_text(self, text: Text) -> None:
        self._versions.append(_TextMemento(text._content, text._font))

    def get_version(self, number: int) -> _TextMemento:
        return self._versions[number]
