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
        self.start_button = pygame.Rect(200, 200, 300, 100)
        self.start_button.center = (constant.display_width/2, constant.display_height/2)

#         display
#   button




    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.manager.playing = False
                self.manager.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.manager.playing = False
                    self.manager.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button.collidepoint(pygame.mouse.get_pos()):
                    self.manager.current_state = Game_Screen.game(self.manager)


    def render(self,display):
        display.fill((255, 255, 255))
        pygame.draw.rect(display, (0, 150, 150), self.start_button)
        util.message_display(str="start", center=self.start_button.center, font_size=50, color=(255, 255, 255),
                             gameDisplay=display)



# if __name__ == '__main__':
#     game = Start_screen()
#     game.start_loop()
