#initialize a display
# generate a start button in the middle of the screen
# if it click start
#   update the gamestate  variable
from Game_Screen import game
import pygame
from constant import constant
import util
from constant import constant
class Start_screen:
    def __init__(self):
#         display
#   button
        self.game_display = pygame.display.set_mode((1000, 1000))
        self.start_button = pygame.Rect(4000,400,200,50)
        self.start_button.midtop = (500,475)
        self.game = game()




    def start_loop(self):
            this_screen = True
            self.game_display.fill((255,255,255))
            pygame.draw.rect(self.game_display,(0,150,150),self.start_button)
            util.message_display(str = "start", center = self.start_button.center,font_size=30,color = (255,255,255),gameDisplay=self.game_display)
            while this_screen:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        this_screen = False
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.start_button.collidepoint(pygame.mouse.get_pos()):
                            constant.game_score = 2
                            this_screen = False

                if this_screen == True:
                    pygame.display.update()

if __name__ == '__main__':
    game = Start_screen()
    game.start_loop()
