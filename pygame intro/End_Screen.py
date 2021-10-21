# display 2 buttons asking the user to restart or quit the game
# update the screen
# close game if the user choose quit
# change gamesate to gamescreen if user choose restart
import pygame
import Game_Screen
import util
from constant import constant
from scoreboard import scoreboard
import GameManager
from Screen import Screen
from constant import constant


class EndScreen(Screen):

    def __init__(self,Gamemanger):
        Screen.__init__(self,Gamemanger)

#         display
#   button
#         self.game_display = pygame.display.set_mode((1000, 1000))
        self.restart_button = pygame.Rect(600,600,200,50)
        self.restart_button.midtop = (constant.display_width/4,constant.display_height/2+200)
        self.constant = constant()
        self.quit_button = pygame.Rect(600,600,200,50)
        self.quit_button.midtop = (3*constant.display_width/4,constant.display_height/2+200)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.manager.playing = False
                self.manager.running = False


            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.restart_button.collidepoint(pygame.mouse.get_pos()):
                    self.manager.current_state = Game_Screen.game(self.manager)
                if self.quit_button.collidepoint(pygame.mouse.get_pos()):
                    self.manager.running = False



    def render(self,display):
        display.fill((255, 255, 255))
        pygame.draw.rect(display, (0, 150, 150), self.restart_button)
        pygame.draw.rect(display, (150, 0, 30), self.quit_button)

        util.message_display(str='you crashed', center=(constant.display_width / 2, constant.display_height / 2),
                             font_size=115, color=constant.black, gameDisplay=display)

        util.message_display(str='score: {}'.format(constant.score), center=(constant.display_width / 2,
                                                                                     constant.display_height / 2 + 100),
                             font_size=115, color=constant.black, gameDisplay=display)
        util.message_display(str="restart", center=self.restart_button.center, font_size=30, color=(255, 255, 255),
                             gameDisplay=display)
        util.message_display(str="quit", center=self.quit_button.center, font_size=30, color=(255, 255, 255),
                             gameDisplay=display)


    # def initialize(self):
    #     self.game_display.fill((255, 255, 255))
    #     pygame.draw.rect(self.game_display, (0, 150, 150), self.restart_button)
    #     pygame.draw.rect(self.game_display, (150, 0, 30), self.quit_button)
    #     util.message_display(str='you crashed', center=(self.game.display_width / 2, self.game.display_height / 2),
    #                          font_size=115, color=self.game.black, gameDisplay=self.game_display)
    #
    #     util.message_display(str='score: {}'.format(scoreboard.final_score), center=(self.game.display_width / 2,
    #                                                                                  self.game.display_height / 2 + 100),
    #                          font_size=115, color=self.game.black, gameDisplay=self.game_display)
    #     util.message_display(str="restart", center=self.restart_button.center, font_size=30, color=(255, 255, 255),
    #                          gameDisplay=self.game_display)
    #     util.message_display(str="quit", center=self.quit_button.center, font_size=30, color=(255, 255, 255),
    #                          gameDisplay=self.game_display)
    #     self.end_loop()
    # def end_loop(self):
    #     this_screen = True
    #     self.game_display.fill((255, 255, 255))
    #     pygame.draw.rect(self.game_display, (0, 150, 150), self.restart_button)
    #     pygame.draw.rect(self.game_display, (150, 0, 30), self.quit_button)
    #     util.message_display(str='you crashed', center=(self.game.display_width / 2, self.game.display_height / 2),
    #                          font_size=115, color=self.game.black, gameDisplay=self.game_display)
    #
    #     util.message_display(str='score: {}'.format(scoreboard.final_score), center=(self.game.display_width / 2,
    #                                                                                  self.game.display_height / 2 + 100),
    #                          font_size=115, color=self.game.black, gameDisplay=self.game_display)
    #     util.message_display(str="restart", center=self.restart_button.center, font_size=30, color=(255, 255, 255),
    #                          gameDisplay=self.game_display)
    #     util.message_display(str="quit", center=self.quit_button.center, font_size=30, color=(255, 255, 255),
    #                          gameDisplay=self.game_display)
    #     while this_screen:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 this_screen = False
    #                 GameManager.GameManager.changeState(constant.END_GAME)
    #
    #             if event.type == pygame.MOUSEBUTTONDOWN:
    #                 if self.restart_button.collidepoint(pygame.mouse.get_pos()):
    #                     GameManager.GameManager.change_state(constant.IN_GAME)
    #
    #                     this_screen = False
    #
    #                 if self.quit_button.collidepoint(pygame.mouse.get_pos()):
    #                     GameManager.GameManager.change_state(gamestate=constant.QUIT)
    #
    #                     this_screen = False
    #         if this_screen == True:
    #             pygame.display.update()

# if __name__ == '__main__':
#     game = EndScreen()
#     game.end_loop()
