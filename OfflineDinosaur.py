
import pygame as pg
import sys

pg.init()

size = width, height = 1280, 720
groundPosition = height * 0.6
screen = pg.display.set_mode(size)

dino = pg.image.load("dinosaur.png")
dino = pg.transform.scale(dino, (100, 100))

cactus = pg.image.load("cactus.png")
cactus = pg.transform.scale(cactus, (100, 100))

dinoRect = dino.get_rect()
dinoRect.width = 60
dinoRect.height = 80
dinoRect.center = (width * 0.25, groundPosition)

cactusRect = cactus.get_rect()
cactusRect.width = 60
cactusRect.height = 80
cactusRect.center = (width + 150, groundPosition)

speed = [0,0]
jumping = False
gravity = 0.02

cactusSpeed = [-1, 0]

score = 0

font = pg.font.SysFont('Comic Sans MS', 24)
text = font.render("Score: " + str(score), False, (0,0,0))
endText = font.render("", False, (0,0,0))

gameOver = False

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
    
    if not gameOver:
        speed[1] += gravity
    
        if dinoRect.centery >= groundPosition:
            dinoRect.centery = groundPosition
            jumping = False
            speed[1] = 0
        
        if pg.key.get_pressed()[pg.K_SPACE]:
            if not jumping:
                jumping = True
                speed[1] = -3
    
        dinoRect = dinoRect.move(speed)
    
        cactusRect = cactusRect.move(cactusSpeed)
    
        if cactusRect.centerx < -150:
            cactusRect.centerx = width + 150
            score += 1
        
        if dinoRect.colliderect(cactusRect):
            endText = font.render("Game Over", False, (0,0,0), (255, 255, 255))
            gameOver = True
        

        text = font.render("Score: " + str(score), False, (0,0,0))

    screen.fill("white")
    screen.blit(text, (width * 0.8, height * 0.1))
    screen.blit(cactus, cactusRect)
    screen.blit(dino, dinoRect)
    screen.blit(endText, (width / 2, height / 2))
    
    pg.display.flip()