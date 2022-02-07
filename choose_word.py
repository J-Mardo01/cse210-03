import random as ram
from director import Director

class Call_word:

    def __init__(self):
        self._words = ['cool' , 'jump']
        self._split_word = []
        self._current_word = []
        pass

    def _random_choice(self):
        self._x = self._words[ram.randint(0,len(self._words))]
        self._split_word = list(self._x)
        return self._split_word
        
    def _create_word_thing(self):
        y = len(self._split_word)
        start_list = ["_" for i in range(len(self._split_word))]

    def _create_index(self):
        if Director._get_input in self.split_word:
            self._current_word[self._split_word.index(Director._get_input)] = Director._get_input
        pass
       
        
word = Call_word()
word._random_choice()
word._create_word_thing()
    

# NEED TO BUILD A WHILE LOOP FOR INDEX