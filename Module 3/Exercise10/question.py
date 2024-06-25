class Question:

    def __init__(self):
        self._text = ""
        self._answer = ""

    def setText(self, questionText):
        self._text = questionText

    def setAnswer(self, correctResponse):
        self._answer = correctResponse

    def checkAnswer(self, response):
        return response == self._answer

    def display(self):
        print(self._text)
