import time
import throttle
import GameManager
import pygame
from BulletTracker import BulletTracker
from Enemy import Enemy
from Screen import Screen
from bullet import Bullet
from input import input
from player import Player
from scoreboard import scoreboard
import End_Screen
# from util import util
from constant import constant
import util
class game(Screen):
    delay = 0.1
    limit = 1
    def __init__(self, game_manager):
        Screen.__init__(self, game_manager)
        pygame.init()
        self.cons = constant()

        self.gameDisplay = pygame.display.set_mode((constant.display_width, constant.display_height))


        self.time = time
        pygame.display.set_caption("my game")
        self.fpsClock = pygame.time.Clock()

        self.car_width = 80

        self.road_img = pygame.image.load("IIMAGE/road.jpg")
        self.road_img = pygame.transform.rotate(self.road_img, 90)

        self.road_img = pygame.transform.scale(self.road_img, (constant.display_width, constant.display_height))

        self.player = Player(self)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        self.enemy = Enemy(self)
        self.enemy.update()
        self.all_sprites.add(self.enemy)

        self.enemies = pygame.sprite.Group()
        self.enemies.add(self.enemy)
        self.input = input(self)

        self.bullets = pygame.sprite.Group()
        self.score = scoreboard(self)
        self.num_bullets = BulletTracker(self)

        self.delay = 0.7
        self.limit = 3
        self.level = 0

        self.crashes = False
    def text_object(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def message_display(self, str, x, y, font_size, color):
        pygame.font.init()
        largeText = pygame.font.SysFont('sitkasmallsitkatextitalicsitkasubheadingitalicsitkaheadingitalicsitkadisplayitalicsitkabanneritalic', font_size)
        TextSurf, TextRect = self.text_object(str, largeText, color)
        TextRect.center = (x, y)
        self.gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()


    def crash(self):
       # scoreboard.final_score = self.score.score
       self.message_display('you crashed',constant.display_width/2,constant.display_height/2,115,(255,0,38))
       # print("ran")
       time.sleep(1)
       # util.message_display('score: {}'.format(self.score.score),self.display_width/2,self.display_height/2+100,115,self.black)
       for i in self.enemies:
           self.enemies.remove(i)
           i.kill()
       for i in self.all_sprites:
           self.all_sprites.remove(i)
           i.kill()
       constant.score = self.score.score
       # self.score.score= 0
       # self.num_bullets = 20
       # self.all_sprites.add(self.player)
       # self.player.rect = self.player.surf.get_rect(center=self.player.surf_center)
       # pygame.display.flip()
       # time.sleep(1)

    # reset everything

    # ask the user if they way to restart

    # self.gameloop()

    # def car(x,y):
    #     gameDisplay.blit(carImg, (x,y))
    #
    # def thing(x,y,w,h, color,blocks):
    #     pygame.draw.rect(gameDisplay,color, [x,y,w,h])
    @throttle.wrap(1,1)
    def update_score(self):
        self.score.score = self.score.score +1

    @throttle.wrap(3,1)
    def update_level(self):
        self.level +=1
        if self.level % 2 == 0:
            self.delay -= 0.05
        else:
            self.limit += 1
    #note add throttle method
    @throttle.wrap(delay , limit)
    def add_enememy(self):
        new_enemy = Enemy(self)
        self.enemies.add(new_enemy)
        self.all_sprites.add(new_enemy)


    def fire_bullet(self):
        if self.num_bullets.numbullet > 0:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.all_sprites.add(new_bullet)
            self.num_bullets.update_bullet()

    def get_player(self):
        return self.player


    def update(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.manager.playing = False
                self.manager.running = False


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.manager.playing = False
                    self.manager.running = False
                if event.key == pygame.K_SPACE:
                    self.fire_bullet()


        self.add_enememy()
        pressed_keys = pygame.key.get_pressed()

        #update  movement of players
        self.input.update(pressed_keys)
        self.bullets.update()

        if pygame.sprite.spritecollideany(self.player, self.enemies):
            # Update gamestate variable
            self.player.kill()
            # self.crashes = True
            self.crash()

            self.manager.current_state = End_Screen.EndScreen(self.manager)


        collision = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
        if collision != {}:
            self.score.score += 0.5



    def render(self,display):
        display.blit(self.road_img, (0,0))
        for entity in self.all_sprites:
            display.blit(entity.surf, entity.rect)
        # for b in self.bullets:
        #     display.blit(b.surf, b.rect.topleft)
        #     b.update()
        #

        self.num_bullets.display_numbullets(display)
        self.score.display_score(display)

        # self.fpsClock.tick(60)

if __name__ == '__main__':
    game = game()
    game.gameloop()
