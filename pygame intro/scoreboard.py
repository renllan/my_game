class scoreboard:
    def __init__(self,game):
        self.game = game
        self.score = 0

    def update_score(self,points):
        self.score += points


    def display_score(self):
        self.game.message_display("score: {}".format(self.score),40,20,20)