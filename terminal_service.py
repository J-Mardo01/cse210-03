from jumper import Jumper
from choose_word import Call_word

class TerminalService:
    def __init__(self) -> None:
        pass

    def user_guess(self):
        return input("Please guess a letter (a-z): ")

    def _print_update(self):
        Jumper.print_jumper()
        Call_word._create_word_thing # Print the word with as many letters as they have guessed. 