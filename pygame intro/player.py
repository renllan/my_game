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
from constant import constant
class Player(pygame.sprite.Sprite):
    def __init__(self,game):
        super(Player,self).__init__()
        self.screen = game.gameDisplay
        self.surf = pygame.image.load('racecar.png').convert()
        self.car_width = 150
        self.surf = pygame.transform.scale(self.surf, (150,112))
        self.surf = pygame.transform.rotate(self.surf, 90)
        self.surf.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        self.surf_center = (
    (game.display_width-self.surf.get_width())/2,
    (game.display_height-self.car_width/2)

        )

        self.display_width = game.display_width
        self.display_height = game.display_height

        self.rect = self.surf.get_rect(center = self.surf_center)
        self.center = self.surf_center


    # def update(self, pressed_keys):
    #     if pressed_keys[K_UP]:
    #         self.rect.move_ip(0, -5)
    #         self.center = (self.center[0], self.center[1]-5)
    #     if pressed_keys[K_DOWN]:
    #         self.rect.move_ip(0, 5)
    #         self.center = (self.center[0], self.center[1]+5)
    #     if pressed_keys[K_LEFT]:
    #         self.rect.move_ip(-5, 0)
    #         self.center = (self.center[0]-5, self.center[1])
    #     if pressed_keys[K_RIGHT]:
    #         self.rect.move_ip(5, 0)
    #         self.center = (self.center[0]+5 , self.center[1])
    #     # if pressed_keys[K_SPACE]:
    #     #     bullet = Bullet(self.center)
    #     #     bullet.update(pressed_keys)
    #         # fire a bullet
    #
    #
    #     if self.rect.left < 0:
    #         self.rect.left = 0
    #     if self.rect.right > self.display_width:
    #         self.rect.right = self.display_width
    #     if self.rect.top <= 0:
    #         self.rect.top = 0
    #     if self.rect.bottom >= self.display_height:
    #         self.rect.bottom = self.display_height

    def move(self, deltax, deltay):
        self.rect.move_ip(deltax,deltay)
    def blitme(self):
        self.screen.blit(self.surf, self.rect)