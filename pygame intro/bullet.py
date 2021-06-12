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
    def __init__(self):
        super(Bullet, self).__init__()
        self.surf = pygame.Surface((10,30))
        self.surf .fill(dark_grey)
        self.rect = self.surf.get_rect(
            center = (position))
        self.num_bullet += 1

    def update(self,key):
         if key[K_SPACE]:
             self.rect.move_ip(0, -20)
         if key[K_LEFT]:
             self.rect.move_ip(-5, 0)
         if key[K_RIGHT]:
            self.rect.move_ip(5, 0)
         if self.rect.top < 0:
             self.kill()
