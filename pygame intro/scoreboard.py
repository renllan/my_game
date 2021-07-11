import pygame
import util
class scoreboard:
    final_score = 0
    def __init__(self,game):
        pygame.init()
        self.game = game
        self.score = 0

    def update_score(self,points):
        self.score += points


    def display_score(self):
        util.message_display(str="score: {}".format(self.score),center = (100,20),font_size=30,color = (0,0,0),gameDisplay = self.game.manager.game_canvas)

