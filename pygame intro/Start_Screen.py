#initialize a display
# generate a start button in the middle of the screen
# if it click start
#   update the gamestate  variable
from Game_Screen import game
import pygame
from constant import constant
class Start_screen:
    def __init__(self):
#         display
#   button
        self.game_display = pygame.display.set_mode((800, 800))
        self.start_button = pygame.Rect(400,400,200,50)
        self.start_button.midtop = (400,375)
        self.constant = constant
        self.game = game()

    def start_loop(self):
        this_screen = True
        self.game_display.fill((255,255,255))
        pygame.draw.rect(self.game_display,(0,150,150),self.start_button)
        while this_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    this_screen = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.start_button.collidepoint(pygame.mouse.get_pos())
                    self.game.gameloop()
                    pygame.quit()
            pygame.display.update()

if __name__ == '__main__':
    game = Start_screen()
    game.start_loop()
