import pygame
import time
from player import Player
from Enemy import Enemy
from input import input
from bullet import Bullet
from scoreboard import scoreboard
from constant import constant
class game:

     def __init__(self):
        pygame.init()
        self.display_width = 1000
        self.display_height = 1000
        self.gameDisplay = pygame.display.set_mode((self.display_width,self.display_height))

        self.time =time
        pygame.display.set_caption("my game")
        self.fpsClock = pygame.time.Clock()

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.dark_grey = (169, 169, 169)
        self.car_width = 100

        self.carImg = pygame.image.load('racecar.png')
        self.carImg = pygame.transform.rotate(self.carImg, 90)
        self.carImg = pygame.transform.scale(self.carImg, (self.car_width, self.car_width))

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
        self.num_bullets = 20

     def text_object(self,text, font,color):
        textSurface = font.render(text,True, color)
        return textSurface, textSurface.get_rect()

     def message_display(self,str,x,y,font_size,color):
        pygame.font.init()
        largeText = pygame.font.Font('freesansbold.ttf',font_size)
        TextSurf, TextRect = self.text_object(str, largeText,color)
        TextRect.center = (x,y)
        self.gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()




     def crash(self):
        self.message_display('you crashed',self.display_width/2,self.display_height/2,115,self.black)
        scoreboard.final_score = self.score.score
        #
        # self.message_display('score: {}'.format(self.score.score),self.display_width/2,self.display_height/2+100,115,self.black)
        for i in self.enemies:
            self.enemies.remove(i)
            i.kill()
        for i in self.all_sprites:
            self.all_sprites.remove(i)
            i.kill()
        self.score.score= 0
        self.num_bullets = 20
        self.all_sprites.add(self.player)
        self.player.rect = self.player.surf.get_rect(center=self.player.surf_center)
        pygame.display.flip()
        time.sleep(1)


        # reset everything


        #ask the user if they way to restart

        # self.gameloop()



    # def car(x,y):
    #     gameDisplay.blit(carImg, (x,y))
    #
    # def thing(x,y,w,h, color,blocks):
    #     pygame.draw.rect(gameDisplay,color, [x,y,w,h])
     def fire_bullet(self):
         if self.num_bullets > 0:
             new_bullet = Bullet(self)
             self.bullets.add(new_bullet)
             self.all_sprites.add (new_bullet)
             self.num_bullets -= 1

     def display_numbullets(self):
         self.message_display("bullets: {}".format(self.num_bullets), self.display_width-100, 20, 20,self.black)
     def get_player(self):
         return self.player



     def gameloop(self):

        pygame.init()

        numbullet = 4
        gameExit = False
        # bullet = Bullet((display_width/2,
        # (display_height)))
        car_speed = 5
        # enemies = pygame.sprite.Group()

        # # all_sprites.add(bullet)
        ADDENEMY = pygame.USEREVENT + 0
        pygame.time.set_timer(ADDENEMY,300)
        #
        # ADDBULLETT = pygame.USEREVENT + 1
        # pygame.time.set_timer(ADDBULLETT, 200)

        while not gameExit:
            self.gameDisplay.fill(self.white)
            # car(x, y)
            #
            # thing(thing_startx, thing_starty, thing_width, thing_height, (black), numblock)
            # thing_starty += thing_speed

            # self.player.blitme()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    constant.game_score = 4

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gameExit = True
                        constant.game_score = 4
                    if event.key == pygame.K_SPACE:
                         self.fire_bullet()
                elif event.type == ADDENEMY:
                    new_enemy = Enemy(self)
                    self.enemies.add(new_enemy)
                    self.all_sprites.add(new_enemy)

                # elif event.type == ADDBULLETT and numbullet < 10:
                #     new_bullet = Bullet(player.center)
                #     all_sprites.add(new_bullet)


                # if event.type == pygame.KEYUP:
                #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                #         x_change = 0
                #         y_change = 0
            pressed_keys = pygame.key.get_pressed()
            # if pressed_keys[K_SPACE]:
            #     if numbullet > 0:
            #         bullet = Bullet(player.center)
            #         bullet.update()
            #         all_sprites.add(bullet)
            #         numbullet -= 1
            #         if pygame.sprite.spritecollideany(bullet, enemies):
            #             bullet.kill()
            # Update the player sprite based on user keypresses
            self.input.update(pressed_keys)
            self.bullets.update()

            for entity in self.all_sprites:
                self.gameDisplay.blit(entity.surf, entity.rect)
            for b in self.bullets:
                self.gameDisplay.blit(b.surf,b.rect)
                b.update()
            #
            if pygame.sprite.spritecollideany(self.player,self.enemies):
                 # Update gamestate variable
                 self.player.kill()
                 self.crash()
                 constant.game_score = 3



                 gameExit = True


            collision = pygame.sprite.groupcollide(self.bullets,self.enemies,True,True)
            if collision != {}:
                self.score.update_score(2)


            self.score.display_score()
            self.display_numbullets()
            pygame.display.flip()
            self.fpsClock.tick(60)

if __name__ == '__main__':
    game = game()
    game.gameloop()
