class Letter:
    def __init__(self, letterFrom, letterTo):
        self._sender = letterFrom
        self._receiver = letterTo
        self._body = []

    def addLine(self, line):
        self._body.append(line)

    def getText(self):
        text = "Dear " + self._receiver + ":\n\n"

        for line in self._body:
            text = text + line + "\n"

        text = text + "\nSincerely, \n\n"
        text = text + self._sender

        return text
