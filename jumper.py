

class Jumper:

    def __init__ (self):
        self._score = 0
        
    def _print_jumper(self):
        print_list = [
        [" ____"],
        ["\____/"],
        [" \  /"],
        ["  \/"],
        ["  O"],
        [" /|\\"],
        [" /\\"]]

        for i in print_list[self._score:len(print_list)]:
            print(*i, sep="")

