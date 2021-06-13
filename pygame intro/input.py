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
from bullet import Bullet
class input:

    def __init__(self, game):
        self.game = game

    def update(self, keypressed):
        self.game.player.update(keypressed)
        self.game.enemies.update()
        # if keypressed[K_SPACE]:
        #     bullet = Bullet(self.game)
        #     self.game.all_sprites.add(bullet)
        #     self.game.bullets.add(bullet)
        #     print(self.game.all_sprites)
        #     bullet.update()
