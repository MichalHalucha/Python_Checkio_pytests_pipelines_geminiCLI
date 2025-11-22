VOWELS = "aeiouAEIOU"


class HackerLanguage:
    def __init__(self):
        self.text = ""

    def write(self, text):
        self.text += text

    def delete(self, N):
        self.text = self.text[:-N]

    def send(self):
        result = ""
        for ch in self.text:
            if ch == " ":
                result += "1000000"
            elif ch.isalpha():
                b = format(ord(ch), "b").rjust(7, "0")
                result += b
            else:
                result += ch
        return result

    def read(self, text):
        result = ""
        buffer = ""

        for ch in text:
            if ch in "01":
                buffer += ch
                if len(buffer) == 7:
                    if buffer == "1000000":
                        result += " "
                    else:
                        result += chr(int(buffer, 2))
                    buffer = ""
            else:
                result += ch
        return result
