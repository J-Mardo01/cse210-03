from game.director import Director

class Jumper:

    def __init__ (self):
        pass
    def _print_jumper(self):
        print_list = [
        [" ____"],
        ["\____/"],
        [" \  /"],
        ["  \/"],
        ["  O"],
        [" /|\\"],
        [" /\\"]]

        for i in print_list[Director.return_score():len(print_list)]:
            print(*i, sep="")


