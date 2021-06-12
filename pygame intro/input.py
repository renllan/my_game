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
class input:

    def __init__(self, game):
        self.game = game

    def update(self, keypressed):
        self.game.player.update(keypressed)
        self.game.enemies.update()
