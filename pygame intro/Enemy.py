import random
import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self,game):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((40, 20))
        self.surf.fill(game.black)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0,game.display_width),
                0,
            )
        )
        self.speed = random.randint(5, 20)
        self.screen = game.gameDisplay
        self.display_height = game.display_height
    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > self.display_height:
            self.kill()
