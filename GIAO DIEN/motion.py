
import pygame , sys
from pygame.locals import *

pygame.init()

chieurongx = 500
chieucaoy = 700
imgheight = 50
imgwidth = 50

#fps
fpsclock = pygame.time.Clock()
FPS=30

DISPLAYSURF = pygame.display.set_mode((chieurongx, chieucaoy))
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


#image
img = pygame.image.load('wizard.png').convert_alpha()
img = pygame.transform.scale(img,(imgwidth,imgheight))

#background
background=pygame.image.load('background.jpg').convert_alpha()

class Background():
    def __init__(self,x,y):
        self.background=pygame.transform.scale(background,(1200,chieucaoy))
        self.x=x
        self.y=y
    def draw(self):
        DISPLAYSURF.blit(self.background,(self.x,self.y))
    def move(self,player):
        if player.img_rect.right > chieurongx - self.x:
            self.x -=player.speed
        if player.img_rect.left < -self.x:
            self.x += player.speed

class Player():
    def __init__(self,x,y,width,height):
        self.img = pygame.transform.scale(img,(width,height))
        self.img_rect = self.img.get_rect(topleft=(x,y))
        self.x=x
        self.y=y
        self.speed=10
    def draw(self,bg):
        DISPLAYSURF.blit(self.img,(self.img_rect.left + bg.x,self.img_rect.top+bg.y) )
    def move(self,bg,left,right):
        if left:
            self.img_rect.centerx -=self.speed
        if right:
            self.img_rect.centerx +=self.speed
        if self.img_rect.right > bg.background.get_width():
            self.img_rect.right = bg.background.get_width()
        if self.img_rect.left < 0:
            self.img_rect.left = 0
bg=Background(0,0)
player = Player(0,int(chieucaoy-imgheight),imgwidth,imgheight)

#get_react tao khung quanh ảnh
img_rect=img.get_rect()

def move(up,down,left,right):
    speed = 10
    if up:
        img_rect.centery -= speed
        if img_rect.top <=0:
            img_rect.top = 0
    if down:
        img_rect.centery += speed
        if img_rect.bottom >= chieucaoy:
            img_rect.bottom = chieucaoy
    if left:
        img_rect.centerx -= speed
        if img_rect.left <=0:
            img_rect.left = 0
    if right:
        img_rect.centerx += speed
        if img_rect.right >= chieurongx:
            img_rect.right = chieurongx
up,down,left,right = False,False,False,False

while True:
    # DISPLAYSURF.blit(img,(50,50))
    
    DISPLAYSURF.fill(White)
    
    for event in pygame.event.get(): #tra ve chuoi su kien
        if event.type == QUIT: 
            
            pygame.quit()
            sys.exit()
    
        if event.type == KEYDOWN:
            if event.key == K_UP:
                up = True
            if event.key == K_DOWN:
                down = True
            if event.key == K_LEFT:
                left = True
            if event.key == K_RIGHT:
                right = True
        if event.type == KEYUP:
            if event.key == K_UP:
                up = False
            if event.key == K_DOWN:
                down = False
            if event.key == K_LEFT:
                left = False
            if event.key == K_RIGHT:
                right = False 
    move(up,down,left,right)  
    DISPLAYSURF.blit(img,img_rect)
    
    bg.draw()
    player.draw(bg)
    player.move(bg,left,right)
    bg.move(player)
    pygame.display.update() #hien ra man hinh
    fpsclock.tick(FPS)
    
    