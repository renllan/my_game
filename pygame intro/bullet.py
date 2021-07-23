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

    def __init__(self,game ):
        super(Bullet, self).__init__()
        self.surf = pygame.image.load('IIMAGE/bullet.png').convert()

        self.b_width = 30
        self.b_height = 60
        self.surf = pygame.transform.rotate(self.surf, 90)
        self.surf = pygame.transform.scale(self.surf, (self.b_width,self.b_height))
        self.surf.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        self.rect  = self.surf.get_rect()
        self.rect.midbottom = game.player.rect.midtop
        self.y = float(self.rect.y)
        self.num_bullets = 20


    def update(self):
         self.rect.move_ip(0, -10)
         if self.rect.top < 0:
             self.kill()

