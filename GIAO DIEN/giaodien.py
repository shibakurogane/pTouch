import pygame , sys
from pygame.locals import *

pygame.init()

#fps
fpsclock = pygame.time.Clock()
FPS=30

DISPLAYSURF = pygame.display.set_mode((1000, 700))
pygame.display.set_caption('tPython')

#color
Black	= (0,0,0)
White	=	(255,255,255)
Red	=	(255,0,0)
Lime	=	(0,255,0)
Blue	=	(0,0,255)
Yellow	=	(255,255,0)
Aqua	=	(0,255,255)
Magenta =	(255,0,255)
Silver	=	(192,192,192)
Gray	=	(128,128,128)
Maroon	=	(128,0,0)
Olive	=	(128,128,0)
Green	=	(0,128,0)
Purple	=	(128,0,128)
Teal	=	(0,128,128)
Navy	=	(0,0,128)

#Rect object

Myrect = pygame.Rect(50,50,100,100)
print(Myrect)

#test
font1 = pygame.font.Font('freesansbold.ttf',30)
text1 = font1.render('Minh',True,Navy,Teal)

#load image
img = pygame.image.load('hexagont.png').convert_alpha()
img1 = pygame.transform.scale(img,(25,25))

imgx=10
imgy=10
direction = 'right'

while True:
    # DISPLAYSURF.fill(White)
    # pygame.draw.rect(DISPLAYSURF,Red,(50,50,100,100))
    # pygame.draw.circle(DISPLAYSURF,Green,(150,150),100)
    
    if direction == 'right':
        imgx+=5
        if imgx == 300:
            direction = 'down'
    elif direction == 'down':
        imgy += 10
        if imgy == 400:
            direction = 'left'
    elif direction == 'left':
        imgx -=5
        if imgx==10:
            direction = 'up'
    elif direction == 'up':
        imgy-=10
        if imgy==10:
            direction = 'right'
    
    DISPLAYSURF.blit(img1,(imgx,imgy))
    # DISPLAYSURF.blit(text1,(200,200))
    for event in pygame.event.get(): #tra ve chuoi su kien
        if event.type == QUIT: 
            pygame.quit()
            sys.exit()
    pygame.display.update() #hien ra man hinh
    #
    fpsclock.tick(FPS)