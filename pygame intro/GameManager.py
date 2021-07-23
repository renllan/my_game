import pygame
import End_Screen
import Game_Screen
import Start_Screen
from constant import constant
import time


class GameManager:
    gamestate = 1
    def __init__(self):
        # self.start_screen = Start_Screen.StartScreen()
        # self.game_screen = Game_Screen.game()
        # self.end_screen = End_Screen.EndScreen()
        self.time = time
        self.fpsClock = pygame.time.Clock()



        self.cons = constant()
        self.state_number = 1
        pygame.init()
        self.GAME_W, self.GAME_H = self.cons.display_width, self.cons.display_height
        self.game_canvas = pygame.Surface((self.GAME_W, self.GAME_H))
        self.game_display = pygame.display.set_mode((self.GAME_W, self.GAME_H))


        self.current_state = Start_Screen.StartScreen(self)
        self.running, self.playing = True,True

        self.ADDENEMY = pygame.USEREVENT + 0
        self.interval = pygame.time.set_timer(self.ADDENEMY, 300)

    # @staticmethod
    # def change_state(gamestate):
    #
    #     if gamestate == constant.START_GAME:
    #         start_screen = Start_Screen.StartScreen()
    #         start_screen.startLoop()
    #     if gamestate == constant.IN_GAME:
    #         game_screen = Game_Screen.game()
    #         game_screen.gameloop()
    #     if gamestate == constant.END_GAME:
    #         end_screen = End_Screen.EndScreen()
    #         end_screen.end_loop()
    #     if gamestate == constant.QUIT:
    #         pygame.quit()

    # def manage(self):
    #     while True:
    #         print(constant.game_score)
    #         if GameManager.gamestate == 1:
    #             self.start_screen.start_loop()
    #         if GameManager.gamestate == 2:
    #             self.game_screen.gameloop()
    #         if GameManager.gamestate== 3:
    #             self.end_screen.end_loop()
    #         if GameManager.gamestate == 4:
    #             pygame.quit()
    #             break

    def update(self):
        self.current_state.update()
    def render(self):
        self.current_state.render(self.game_canvas)
        self.game_display.blit(self.game_canvas, (0,0))
        pygame.display.flip()

    def gameloop(self):
        self.update()
        self.render()
        self.fpsClock.tick(60)



if __name__ == '__main__':
    game = GameManager()
    # print(pygame.font.get_fonts())
    while game.running:
        game.gameloop()

    pygame.quit()
