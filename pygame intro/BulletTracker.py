import util

class BulletTracker():

    def __init__(self,game ):
        self.numbullet = 20
        self.game = game
    def update_bullet(self):
        self.numbullet -=1

    def display_numbullets(self):
        util.message_display(str = "bullets: {}".format(self.numbullet), center = (900,20), font_size=30, gameDisplay = self.game.manager.game_canvas, color = (0,0,0))