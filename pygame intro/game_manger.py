from Game_Screen import  game
from Start_Screen import Start_screen
from End_Screen import End_screen
from constant import constant
import pygame
class game_manager:
    def __init__(self):
        self.start_screen = Start_screen()
        self.game_screen = game()
        self.end_screen = End_screen()
        self.cons = constant()


    def manage(self):
        while True:
            print(constant.game_score)
            if constant.game_score == 1:
                self.start_screen.start_loop()
            if constant.game_score == 2:
                self.game_screen.gameloop()
            if constant.game_score == 3:
                self.end_screen.end_loop()
            if constant.game_score == 4:
                pygame.quit()
                break

if __name__ == '__main__':
    game = game_manager()
    game.manage()

