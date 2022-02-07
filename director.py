from choose_word import Call_word
from jumper import Jumper
from terminal_service import TerminalService


class Director: 

    def __init__(self):
        self._jumper = Jumper()
        self._choose_word = Call_word()
        self._terminal_service = TerminalService()
        self._is_playing = True

    def start_game(self):
        while self._is_playing:
            self._get_input()
            self._do_output()
        pass

    def _get_input(self):
        guess = self._terminal_service.user_guess()
    
        

    def _do_output(self):
        pass