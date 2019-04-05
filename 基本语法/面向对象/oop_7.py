class Game:
    top_score = 0

    def __init__(self,play_name):
        self.play_name = play_name

    @staticmethod
    def show_help():
        print("help")

    @classmethod
    def show_top_score(cls):
        print(cls.top_score)

    def start_game(self):
        print("%s start game,boom...."%(self.play_name))


game = Game("xm")
Game.show_help()
print(Game.top_score)
game.start_game()
