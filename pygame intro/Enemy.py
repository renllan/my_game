import random
import pygame
import math
from constant import constant
class Enemy(pygame.sprite.Sprite):
    def __init__(self,game):
        super(Enemy, self).__init__()
        self.game = game
        self.surf = pygame.Surface((random.randint(40,100), random.randint(20,50)))
        self.surf.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        self.spinning = True
        self.spin = random.randint(0,1)
        if self.spin == 1:
            self.spinning = False
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0,constant.display_width),
                0,
            )
        )
        self.horz_speed = random.randint(-15, 15)
        self.vert_speed = random.randint(5,15)
        # self.screen = game.gameDisplay
        # self.display_height = game.display_height
    def update(self):

        self.rect.move_ip(self.horz_speed,
                              self.vert_speed)
        if self.rect.top > constant.display_height:
            self.kill()


