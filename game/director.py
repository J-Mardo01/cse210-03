from game.choose_word import Call_word
from game.jumper import Jumper
from game.terminal_service import TerminalService


class Director: 

    def __init__(self):
        self._jumper = Jumper()
        self._choose_word = Call_word()
        self._terminal_service = TerminalService()
        self._is_playing = True
        self._score = 0

    def start_game(self):
        while self._is_playing:
            self._get_input()
            self._do_output()
        pass

    def _get_input(self):
       # Print word
        self._choose_word.print_current_word()
        # Print jumper
        self._jumper._print_jumper()

        guess = self._terminal_service.user_guess()
        return guess

    def score(self):
        if not self._choose_word.check_guess():
            self._score += 1
        if self._score > 3:
            self._is_playing == False

    def return_score(self):
        return self._score

    def _do_output(self):
        pass