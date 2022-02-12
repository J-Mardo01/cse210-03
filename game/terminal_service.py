from matplotlib.pyplot import text
from jumper import Jumper
from choose_word import Call_word

class TerminalService:
    def read_text(self, prompt):
        return input(prompt)

    def read_number(self, prompt):
        return float(input(prompt))

    def write_text(self, prompt):
        print(text)