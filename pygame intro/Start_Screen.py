#initialize a display
# generate a start button in the middle of the screen
# if it click start
#   update the gamestate  variable
import pygame
from constant import constant
import util
from constant import constant
import GameManager
import Game_Screen
from Screen import Screen

class StartScreen(Screen):
    def __init__(self,Gamemanger):
        Screen.__init__(self,Gamemanger)
        self.start_button = pygame.Rect(4000, 400, 200, 50)
        self.start_button.midtop = (500, 475)

#         display
#   button




    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.manger.playing = False
                self.manager.running = False


            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button.collidepoint(pygame.mouse.get_pos()):
                    self.manager.current_state = Game_Screen.game(self.manager)


    def render(self,display):
        display.fill((255, 255, 255))
        pygame.draw.rect(display, (0, 150, 150), self.start_button)
        util.message_display(str="start", center=self.start_button.center, font_size=30, color=(255, 255, 255),
                             gameDisplay=display)



if __name__ == '__main__':
    game = Start_screen()
    game.start_loop()
