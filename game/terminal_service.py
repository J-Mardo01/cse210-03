from game.jumper import Jumper
from game.choose_word import Call_word

class TerminalService:
    def __init__(self) -> None:
        pass

    def user_guess(self):
        guess = input("Please guess a letter (a-z): ").lower()

        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a letter.")
        else:
            return guess

    def _print_update(self):
        Jumper.print_jumper()
        Call_word._create_word_thing # Print the word with as many letters as they have guessed. 