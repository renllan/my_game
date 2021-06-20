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
        self.display_width = 800
        self.display_height = 800
        self.gameDisplay = pygame.display.set_mode((self.display_width,self.display_height))

        self.time =time
        pygame.display.set_caption("random game")
        self.fpsClock = pygame.time.Clock()

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.dark_grey = (169, 169, 169)
        self.car_width = 50

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

     def text_object(self,text, font):
        textSurface = font.render(text,True, self.black)
        return textSurface, textSurface.get_rect()

     def message_display(self,str,x,y,font_size):
        largeText = pygame.font.Font('freesansbold.ttf',font_size)
        TextSurf, TextRect = self.text_object(str, largeText)
        TextRect.center = (x,y)
        self.gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()




     def crash(self):
        self.message_display('you crashed',self.display_width/2,self.display_height/2,115)

        self.message_display('score: {}'.format(self.score.score),self.display_width/2,self.display_height/2+100,115)
        for i in self.enemies:
            self.enemies.remove(i)
            i.kill()
        for i in self.all_sprites:
            self.all_sprites.remove(i)
            i.kill()
        self.score.score= 0
        self.num_bullets = 20
        self.all_sprites.add(self.player)

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
         self.message_display("bullets: {}".format(self.num_bullets), self.display_width-100, 20, 20)
     def get_player(self):
         return self.player



     def gameloop(self):
        # i = 1
        # numblock = 1
        # x =  (0.5* display_width-150)
        # y = (display_height-car_width)
        # thing_startx = random.randrange(0, display_width)
        #
        # thing_starty = -800
        #
        # thing_speed = 13
        # thing_width = block_width
        # thing_height = 100
        #
        # x_change = 0
        # y_change = 0


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

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gameExit = True
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
                 self.player.kill()
                 self.crash()

                 pygame.quit()
                 # gameExit = True

            collision = pygame.sprite.groupcollide(self.bullets,self.enemies,True,True)
            if collision != {}:
                self.score.update_score(2)

            # if x > display_width - car_width or x < 0:
            #         gameExit = True
            #
            # x = x+x_change
            #
            #
            #
            #
            #
            #
            #
            #
            # if thing_starty >  display_height:
            #
            #     thing_starty = 0 - thing_height
            #     thing_startx = random.randrange(0, display_width - thing_width)
            #     pygame.display.update(thing(thing_startx, thing_starty, thing_width, thing_height, (black),numblock))
            #
            #
            #         # thing_starty += thing_speed
            #     thing_speed = thing_speed * 1.05
            #     car_speed = car_speed * 1.05
            #
            #
            # numblock +=1
            #
            #
            # if y < thing_starty + thing_height:
            #     if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
            #         crash()

            # self.message_display("bullets: {}".format(numbullet),0,50,50)
            self.score.display_score()
            self.display_numbullets()
            pygame.display.flip()
            self.fpsClock.tick(60)

if __name__ == '__main__':
    game = game()
    game.gameloop()
