import pygame
import random
import time
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

pygame.init()
display_width= 800
display_height = 800
gameDisplay = pygame.display.set_mode((display_width,display_height))


pygame.display.set_caption("random game")
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
dark_grey = (169,169,169)
car_width = 50

carImg = pygame.image.load('racecar.png')
carImg = pygame.transform.rotate(carImg, 90)
carImg = pygame.transform.scale(carImg, (car_width, car_width))


block_width = 100
class Bullet(pygame.sprite.Sprite):
    num_bullet = 0
    def __init__(self,position):
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

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((40, 20))
        self.surf.fill(black)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0,display_width),
                0,
            )
        )
        self.speed = random.randint(5, 20)
    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > display_height:
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf = pygame.image.load('racecar.png').convert()

        self.surf = pygame.transform.scale(self.surf, (car_width, car_width))
        self.surf = pygame.transform.rotate(self.surf, 90)
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.surf_center = (
    (display_width-self.surf.get_width())/2,
    (display_height)
)
        self.rect = self.surf.get_rect(center = self.surf_center)
        self.center = self.surf_center


    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            self.center = (self.center[0], self.center[1]-5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            self.center = (self.center[0], self.center[1]+5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
            self.center = (self.center[0]-5, self.center[1])
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
            self.center = (self.center[0]+5 , self.center[1])
        if pressed_keys[K_SPACE]:
            bullet = Bullet(self.center)
            bullet.update(pressed_keys)
            # fire a bullet


        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > display_width:
            self.rect.right = display_width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= display_height:
            self.rect.bottom = display_height


    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen






self.gameloop()
pygame.quit()
quit()

