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
        self.surf = pygame.image.load('bullet.png').convert()
        self.dark_grey = (169, 169, 169)
        self.surf = pygame.transform.rotate(self.surf, 90)
        self.surf = pygame.transform.scale(self.surf, (40,80))
        self.surf.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        self.rect  = self.surf.get_rect()
        self.num_bullet += 1
        self.rect.midtop = game.player.rect.midtop
        self.y = float(self.rect.y)


    def update(self):
         self.rect.move_ip(0, -15)
         if self.rect.top < 0:
             self.kill()
    def display_numbullets(self):
        self.game.message_display("bullets: {}".format(self.game.num_bullets),self.game.display_width,20,20)
