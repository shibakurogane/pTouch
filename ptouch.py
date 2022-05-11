from cProfile import run
from pickle import GLOBAL
from turtle import up, update
from cv2 import line
import pygame, sys

from pygame.locals import *
import random, time

from pyparsing import White
from GraphHandler import generator,imagePredict
import numpy as np
import matplotlib.pyplot as plt
import cv2



# from main import RANK

#option

#Initializing 
pygame.init()
 
# FPS 
FPS = 60
fpsclock = pygame.time.Clock()
 
# colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
 
#
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SPEED=5
LIFE = 11
GOLD=0


line=[]

objheight=100
objwidth=100
 
nv_height=50
nv_width=50



#Setting up Fonts
font = pygame.font.Font('8-BIT WONDER.TTF', 20)
font_small = pygame.font.SysFont("Verdana", 20)
# game_over = font.render("GAME OVER", True, BLACK)
# main_font = pygame.font.SysFont("comicsans", 50)
# lost_font = pygame.font.SysFont("comicsans", 60)
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
# DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("ptouch")

# obj=pygame.image.load('gach.webp').convert_alpha()
# obj=pygame.transform.scale(obj,(objwidth ,objheight))

RANK=1
W,yDraw=generator.CreateGraph(RANK,'dothi.png')
dothi=pygame.image.load('dothi.png').convert_alpha()
hinhdothi=pygame.transform.scale(dothi,(100 ,100)).convert_alpha()

obj=pygame.image.load('ppenemy.webp').convert_alpha()
obj=pygame.transform.scale(obj,(objwidth ,objheight)).convert_alpha()

nv = pygame.image.load('wizard.png').convert_alpha()
nv = pygame.transform.scale(nv,(nv_width,nv_height))
 
BG=pygame.image.load('gray3.png').convert_alpha()
BG=pygame.transform.scale(BG,(SCREEN_WIDTH,1000))

BG1=pygame.image.load('BlacknWhite.webp').convert_alpha()
BG1=pygame.transform.scale(BG1,(SCREEN_WIDTH,1000))

BG2=pygame.image.load('BlacknWhite2.png').convert_alpha()
BG2=pygame.transform.scale(BG2,(SCREEN_WIDTH,1000))

GRASS=pygame.image.load('grass.jpg').convert_alpha()
GRASS=pygame.transform.scale(GRASS,(500,150))

COIN=pygame.image.load('coin.png').convert_alpha()
COIN=pygame.transform.scale(COIN,(40,40))


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = obj
        self.surf = pygame.Surface((objwidth ,objheight))
        self.rect = self.surf.get_rect(center = (random.randint(objwidth,SCREEN_WIDTH-objwidth), 0))
        

    def move(self,W,yDraw,RANK,line,playerDraw):
            global LIFE
            self.rect.move_ip(0,SPEED)
            if (self.rect.bottom >= (SCREEN_HEIGHT-80)):
                LIFE -= 10
                self.rect.top = 0
                self.rect.center = (random.randint(objwidth,SCREEN_WIDTH-objwidth), 0)
            if playerDraw:
                if imagePredict.Proccess(W,yDraw,RANK,line):
                    LIFE+=1
                
            
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = nv
        self.surf = pygame.Surface((nv_width,nv_height))
        self.rect = self.surf.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT-100))
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT] or pressed_keys[K_a]:
                  self.rect.move_ip(-10, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
                  self.rect.move_ip(10, 0)
                   
class Background():
      def __init__(self):
            self.bgimage = BG
            self.rectBGimg = self.bgimage.get_rect()
            
 
            self.bgY1 = 0
            self.bgX1 = 0
 
            self.bgY2 = self.rectBGimg.height
            self.bgX2 = 0
 
            self.movingUpSpeed = 5
         
      def update(self):
        self.bgY1 -= self.movingUpSpeed
        self.bgY2 -= self.movingUpSpeed
        if self.bgY1 <= -self.rectBGimg.height:
            self.bgY1 = self.rectBGimg.height
        if self.bgY2 <= -self.rectBGimg.height:
            self.bgY2 = self.rectBGimg.height
             
      def draw(self):
        DISPLAYSURF.blit(self.bgimage, (self.bgX1, self.bgY1))
        DISPLAYSURF.blit(self.bgimage, (self.bgX2, self.bgY2))
        DISPLAYSURF.blit(GRASS,(0,SCREEN_HEIGHT-150))
        # DISPLAYSURF.blit(GRASS,(0,SCREEN_HEIGHT-(150*2)))
        DISPLAYSURF.blit(GRASS,(SCREEN_WIDTH-500,SCREEN_HEIGHT-150))
        # DISPLAYSURF.blit(GRASS,(SCREEN_WIDTH-500,SCREEN_HEIGHT-(150*2)))
        
         

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
 
bg = Background()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
Char = pygame.sprite.Group()
Char.add(P1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)




# obj_group=pygame.sprite.Group()


#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
    
def gameover():
    # DISPLAYSURF.fill(WHITE)
    Game_over_label=font.render("GOODLUCK NEXT TIME",1,BLACK)
    Restart_label=font.render("PRESS SPACE TO RESTART",1,BLACK)
    DISPLAYSURF.blit(Game_over_label,(SCREEN_WIDTH/2 - Game_over_label.get_width()/2, 400))
    DISPLAYSURF.blit(Restart_label,(SCREEN_WIDTH/2 - Restart_label.get_width()/2, 500))
    pygame.display.update()

def getHighestScore():
    with open("highest score.txt","r") as f:
        return f.read()

playerDraw=False
def gameloop():
    run=True
    global hinhdothi
    global LIFE 
    global line
    global playerDraw
    global SPEED
    global W,yDraw
    global RANK

    try:
        highestScore = int(getHighestScore())
    except:
        highestScore = 0

    while run:
            # entity.move()
        #Cycles through all occurring events   
        for event in pygame.event.get():
            if event.type == INC_SPEED:
                SPEED += 0.5      
            if event.type == QUIT:
                run=False
                pygame.display.quit()
                pygame.quit()
                quit()
            # elif event.type == pygame.KEYUP:
            #     if event.key == pygame.K_SPACE:
            #             GameStage()
            if pygame.mouse.get_pressed()[0]:
                    positionX,positionY=pygame.mouse.get_pos()
                    line.append((pygame.mouse.get_pos()))
                    playerDraw=True
            else:
                    if playerDraw==True:
                        playerDraw=False
                        # pxarray = imagePredict.get_pixel_data(screen,[701,401],[1000,700])
                        # print(pxarray.shape)
                        # plt.imsave('image.png',pxarray)
                        # pygame.image.save(pxarray,'input.png')
                        PredictResult=imagePredict.Proccess(W,yDraw,RANK,line)
                        
                        line=[]
                        if PredictResult:
                            RANK+=1
                            W,yDraw=generator.CreateGraph(RANK,'dothi.png')
                            dothi=pygame.image.load('dothi.png').convert_alpha()
                            # obj=pygame.transform.scale(dothi,(objwidth ,objheight)).convert_alpha()
                            hinhdothi=pygame.transform.scale(dothi,(100 ,100)).convert_alpha()               
            if event.type ==pygame.KEYDOWN:
                    if event.key==pygame.K_p:
                        line=[]
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_SPACE and gameover:
            #         for entity in all_sprites:
            #             DISPLAYSURF.blit(entity.image, entity.rect)
            #             entity.move()
        bg.update()
        bg.draw()
        DISPLAYSURF.blit(hinhdothi,(SCREEN_WIDTH/3,0)) 
        #DISPLAYSURF.blit(background, (0,0))

        if(highestScore < LIFE):
            highestScore = LIFE
        with open("highest score.txt","w") as f:
            f.write(str(highestScore))

        LIFES = font_small.render(f"LIFE: {LIFE}", True, BLACK)
        DISPLAYSURF.blit(LIFES, (10,10))

        HIGHSCORE = font_small.render(f"HIGHEST SCORE: {highestScore}", True, BLACK)
        DISPLAYSURF.blit(HIGHSCORE, (10,30))
    
        #Moves and Re-draws all Sprites
        for entity in Char:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()
        for entity in enemies:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move(W,yDraw,RANK,line,playerDraw)
        for i in range(len(line)):
                pygame.draw.circle(DISPLAYSURF,BLACK,(line[i][0],line[i][1]),2)
        #To be run if collision occurs between Player and Enemy
        if pygame.sprite.spritecollideany(P1,enemies):
            #   pygame.mixer.Sound('crash.wav').play()
            #   time.sleep(0.8)
                        
            # DISPLAYSURF.fill(RED)
            # DISPLAYSURF.blit(game_over, (30,250))
            
            
            for entity in enemies:
                    # entity.kill()
                    LIFE=0
        if LIFE<=0:
                # GameOver()
                # time.sleep(1.5)
                # pygame.quit()
                # sys.exit()  
            run=False
            break
        # if run==False:
        #     LIFE=11
        #     gameover()
        #     time.sleep(2)
        #     GameStage()
            
        # for event in pygame.event.get():
            
            # pygame.display.update()
            # time.sleep(1.5)
            # pygame.quit()
            # sys.exit()
        pygame.display.update()
        fpsclock.tick(FPS)
    pygame.quit()
    
    


def GameStage():
    # title_font = pygame.font.SysFont("comicsans", 70)
    run = True
    while run:
        # DISPLAYSURF.blit(BG, (0,0))
        DISPLAYSURF.fill(WHITE)
        title_label = font.render("Press T to begin", 1, BLACK)
        DISPLAYSURF.blit(title_label, (SCREEN_WIDTH/2 - title_label.get_width()/2, 400))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     gameloop()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_t:
                    gameloop()
    pygame.quit()

# GameStage()


