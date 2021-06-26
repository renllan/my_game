# display 2 buttons asking the user to restart or quit the game
# update the screen
# close game if the user choose quit
# change gamesate to gamescreen if user choose restart
import pygame
import util
from constant import constant
from scoreboard import scoreboard
from Game_Screen import game
class End_screen:

    def __init__(self):
        pygame.init()
#         display
#   button
        self.game_display = pygame.display.set_mode((1000, 1000))
        self.restart_button = pygame.Rect(200,600,200,50)
        self.restart_button.midtop = (250,800)

        self.quit_button = pygame.Rect(600,600,200,50)
        self.quit_button.midtop = (750,800)
        self.game = game()



    def end_loop(self):
        this_screen = True
        self.game_display.fill((255,255,255))
        pygame.draw.rect(self.game_display,(0,150,150),self.restart_button)
        pygame.draw.rect(self.game_display, (150, 0, 30), self.quit_button)
        util.message_display(str = 'you crashed', center = (self.game.display_width / 2, self.game.display_height / 2), font_size=115, color=self.game.black, gameDisplay = self.game_display )

        util.message_display(str = 'score: {}'.format(scoreboard.final_score), center = (self.game.display_width / 2,
                             self.game.display_height / 2 + 100), font_size= 115, color=self.game.black, gameDisplay = self.game_display)
        util.message_display(str = "restart", center = self.restart_button.center,font_size=30,color = (255,255,255),gameDisplay=self.game_display)
        util.message_display(str="quit", center=self.quit_button.center, font_size=30, color=(255, 255, 255),
                             gameDisplay=self.game_display)
        while this_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    this_screen = False
                    constant.game_score = 4
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.restart_button.collidepoint(pygame.mouse.get_pos()):
                        constant.game_score = 2
                        this_screen = False

                    if self.quit_button.collidepoint(pygame.mouse.get_pos()):
                        constant.game_score = 4
                        this_screen = False
            if this_screen == True:
                pygame.display.update()

if __name__ == '__main__':
    game = End_screen()
    game.end_loop()
