from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE,
    K_r
)
import BulletTracker
from constant import constant
class input:

    def __init__(self, game):
        self.game = game

    def update(self, keypressed):
        # self.game.player.update(keypressed)
        player1 = self.game.get_player()
        if keypressed[K_LEFT]:
            player1.move(-8, 0)
        if keypressed[K_DOWN]:
            player1.move(0, 8)
        if keypressed[K_UP]:
            player1.move(0, -8)

        if keypressed[K_RIGHT]:
            player1.move(8, 0)

        if player1.rect.left < 0:
            player1.rect.left = 0
        if player1.rect.right > constant.display_width:
            player1.rect.right = constant.display_width
        if player1.rect.top <= 0:
            player1.rect.top = 0
        if player1.rect.bottom >=constant.display_height:
            player1.rect.bottom = constant.display_height
        self.game.enemies.update()
        # if keypressed[K_SPACE]:
        #     self.game.fire_bullet()
        if keypressed[K_r]:
            self.game.num_bullets.numbullet = 20
        # if keypressed[K_SPACE]:
        #     bullet = Bullet(self.game)
        #     self.game.all_sprites.add(bullet)
        #     self.game.bullets.add(bullet)
        #     print(self.game.all_sprites)
        #     bullet.update()
