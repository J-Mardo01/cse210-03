from choose_word import Call_word
from jumper import Jumper
from terminal_service import TerminalService


class Director: 

    def __init__(self) -> None:
        self._jumper = Jumper()
        self._word = Call_word()
        self._terminal_service = TerminalService()
        self._is_playing = True
        self._score = 0

    def start_game(self):
        self._word._random_choice()
        self._word._create_word_thing()
        self._jumper._print_jumper(self._score)
        self._word.print_current_word()
        while self._is_playing == True:
            self._get_input()
            self._do_output()

    def _get_input(self):
        guess = self._terminal_service.read_text("Please enter a letter [a-z]: ").lower()
        
        if not self._word.check_guess(guess):
            self._score += 1
        if self._score > 3:
            print(f"Sorry, you lost. The word was {self._word._split_word}") 
            self._is_playing = False
        elif self._word._current_word == self._word._split_word:
            print("You won!")
            self._is_playing = False  

    def _do_output(self):
        self._word.print_current_word()
        self._jumper._print_jumper(self._score)