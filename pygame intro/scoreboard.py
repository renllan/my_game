class scoreboard:
    def __init__(self,game):
        self.game = game
        self.score = 0

    def update_score(self):
        self.score += 1