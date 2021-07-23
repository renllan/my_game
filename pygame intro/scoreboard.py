import pygame
import util
from constant import constant
class scoreboard:
    final_score = 0
    def __init__(self,game):
        pygame.init()
        self.game = game
        self.score = 0

    def update_score(self,points):
        self.score += points


    def display_score(self,display):
        util.message_display(str="score: {}".format(self.score),center = (3*constant.display_width/4,20),font_size=30,color = (0,0,0),gameDisplay =display)

