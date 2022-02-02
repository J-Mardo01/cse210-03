import random as ram

class Call_word:

    def __init__(self):
        self._words = ['cool', 'class' , 'fortnite' , 'jump' , 'coding']
        self._random_choice()
        pass

    def _random_choice(self , _words):
        self._x = ram.randint(0,len(self._words))
        print(_words[self._x])
