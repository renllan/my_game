import random
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE
)
class Bullet(pygame.sprite.Sprite):
    num_bullet = 0
    def __init__(self,game ):
        super(Bullet, self).__init__()
        self.surf = pygame.Surface((10,30))
        self.dark_grey = (169, 169, 169)
        self.surf .fill(self.dark_grey)
        self.rect = self.surf.get_rect()
        self.num_bullet += 1
        self.rect.midtop = game.player.rect.midtop
        self.y = float(self.rect.y)


    def update(self):
         self.rect.move_ip(0, -5)
         if self.rect.top < 0:
             self.kill()

