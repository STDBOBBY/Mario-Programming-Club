import pygame as pg         
import sys
from pygame.locals import *  #it help us to use "KEYUP" and "KEYDOWN" line 68,78
from random import randint
pg.init()           # create a game

#this function draw the floor 
def draw_floor():
        screen.blit(floor,(0,612))
        screen.blit(floor,(625,612))

#this function move mario when we press the buttons
def move(left, right,jump):
    speed_mario =10
    if left:            
        mario_rect.centerx-=speed_mario
    if right:
        mario_rect.centerx+=speed_mario
    if jump:
         mario_rect.centery-=30 
         is_jumping = True
         

#screen setting
size = width, height = 1280,720
groundPosition= height*0.8
screen = pg.display.set_mode(size)

#create mario
mario = pg.image.load('mario.png').convert_alpha()
mario = pg.transform.scale(mario,(50,63))

mario_rect=mario.get_rect()         
mario_rect.width= 50
mario_rect.height=50
mario_rect.center=(width*0.2,groundPosition) #

#Score
score = 0 
game_font = pg.font.SysFont('Comic Sans MS', 24)
text = game_font.render("Score: " + str(score), False, (0,255,0))
#endText = font.render("", False, (0,0,0))

#coin 
class Coin:
    def __init__(self):
        self.coin = pg.image.load("coin.png")
        self.coin = pg.transform.scale(self.coin, (50,50))
        self.coin_rect = self.coin.get_rect()
        self.coin_rect.height = 50
        self.coin_rect.width = 50
    def pos(self, x, y):
        self.coin_rect.center = (x, y)
        pass
y = randint(0, 500)
x = randint(0,500)
c = Coin()
c.coin_rect.center = (width*0.7,groundPosition)
#floor
floor=pg.image.load('floor.png').convert_alpha()
floor= pg.transform.scale2x(floor)

#FPS setting
fpsClock = pg.time.Clock()
FPS = 60

left, right,jump= False,False, False
gravity = 2
speed=0
count=0
gameOver = False
# is_jumping=True
countDown = 10
clock = pg.time.Clock()
startTick = pg.time.get_ticks()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    secondsPassed = (pg.time.get_ticks() - startTick)/1000
    timeLeft = max(0, countDown - int(secondsPassed))
    timerText = game_font.render(f"Time Left: {timeLeft}", True, (0,255,0))
    
    if timeLeft <= 0:
        gameOver = True
    if not gameOver:
        # if pg.key.get_pressed()[pg.K_RIGHT]:
        #     right=True
        # if pg.key.get_pressed()[pg.K_LEFT]:
        #     left=True
        speed+=gravity                       # add gravity to mario
        mario_rect.centery+=speed            #
        if mario_rect.centery>=groundPosition:  # this code keep mario always stand on the ground
            mario_rect.centery=groundPosition
            speed=0
            is_jumping=True

        if event.type==KEYDOWN:   #when we press the key
            if event.key ==K_LEFT:  #press left
                left = True         # when we press left keyborad, left become true and mario go to the left 
                right = False       # mario can not go left and right in the same time
            if event.key ==K_RIGHT:
                right= True         # when we press right keyborad, left become true and mario go to the right 
                left = False
            if event.key ==K_UP and mario_rect.centery==groundPosition:    # when we press up keyborad, up become true and mario jump
                jump = True
                
                # is_jumping = False
        if event.type==KEYUP:       # when we release they key set left, right, jump back to False
            if event.key ==K_LEFT:  
                left = False        
            if event.key ==K_RIGHT:
                right = False
            if event.key == K_UP:
                jump = False
    move(left,right,jump)       # call funciton an mario will move when we press keyboard
    # is_jumping = False
    if c.coin_rect.colliderect(mario_rect):
        y = randint(350, 575)
        x = randint(0,1200)
        c.coin_rect.center = (x,y)
        startTick = startTick + 1000
        score += 1
        text = game_font.render("Score: " + str(score), False, (0,255,0))

    fpsClock.tick(FPS)              # FSF setting, change FPS value will change the game speed
    screen.fill('white')            # back ground   
    screen.blit(mario,mario_rect)
    screen.blit(c.coin, c.coin_rect)# show mario on screen
    screen.blit(text, (50,100))
    screen.blit(timerText, (50,125))
    draw_floor()                    # show floor on screen
    pg.display.flip()               # can not see anthing without this code =]]