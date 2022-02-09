import random as ram
from game.director import Director

class Call_word:

    def __init__(self):
        self._words = ['cool' , 'jump']
        self._split_word = []
        self._current_word = []
        pass

    def print_current_word(self):
        print(self._current_word)

    def _random_choice(self):
        self._x = self._words[ram.randint(0,len(self._words))]
        self._split_word = list(self._x)
        return self._split_word
        
    def _create_word_thing(self):
        self._current_word = ["_" for i in range(len(self._split_word))]

    def check_guess(self):
        guess = Director._get_input()
        if guess in self._split_word:
            for i in self._split_word:
                if i == guess:
                    self._current_word = guess
            return True
        return False
       
        