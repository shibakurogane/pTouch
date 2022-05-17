from cProfile import run
from doctest import FAIL_FAST
from enum import Flag
from lzma import CHECK_CRC32
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

from button import Button
def addCoin(point=0):
    try:
        playerCoin = int(Coin())
    except:
        playerCoin = 0
    playerCoin+=point
    with open("coin.txt","w") as f:
            f.write(str(playerCoin))
    return playerCoin

# from main import RANK

#option

#Initializing 
pygame.init()
 
# FPS 
FPS = 144
fpsclock = pygame.time.Clock()
 
# colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLUE2  = (0, 212, 255)
PURPLE2 = (239, 0 ,255)
AQUA	=	(0,255,255)
MAGENTA =	(255,0,255)
SILVER	=	(192,192,192)
GRAY	=	(128,128,128)
MAROON	=	(128,0,0)
OLIVE	=	(128,128,0)
PURPLE	=	(128,0,128)
TEAL	=	(0,128,128)
LAVA    =   (252,176,69)
BLOOD   =   (253,29,29)
#
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_W=600
SCREEN_H=800
SPEED=3
LIFE = 0

playerCoin=0

line=[]

objheight=100
objwidth=100
 
nv_height=50
nv_width=50

nv_w=100
nv_h=100

#Setting up Fonts
font = pygame.font.Font('8-BIT WONDER.TTF', 20)
font_small = pygame.font.SysFont("Verdana", 20)
# game_over = font.render("GAME OVER", True, BLACK)
# main_font = pygame.font.SysFont("comicsans", 50)
# lost_font = pygame.font.SysFont("comicsans", 60)
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
SCREEN = pygame.display.set_mode((SCREEN_W, SCREEN_H))
# DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("ptouch")

# obj=pygame.image.load('gach.webp').convert_alpha()
# obj=pygame.transform.scale(obj,(objwidth ,objheight))

RANK=1
grap=generator.Graph('dothi.png')
grap.CreateGraph(RANK)
# W,yDraw=generator.CreateGraph(RANK,'dothi.png')
dothi=pygame.image.load('dothi.png').convert_alpha()
hinhdothi=pygame.transform.scale(dothi,(100 ,100)).convert_alpha()

obj=pygame.image.load('image/enemy/bigdrill_3.png').convert_alpha()
obj=pygame.transform.scale(obj,(objwidth ,objheight)).convert_alpha()

nv = pygame.image.load('image/ball/hexagont.png').convert_alpha()
nv = pygame.transform.scale(nv,(nv_width,nv_height))
 
BG=pygame.image.load('image/background/gray3.png').convert_alpha()
BG=pygame.transform.scale(BG,(SCREEN_WIDTH,1000))

METALFLOOR=pygame.image.load('image/background/metalfloor.jpg').convert_alpha()
METALFLOOR=pygame.transform.scale(METALFLOOR,(150,150))

nv1 = pygame.image.load('image/ball/hexagont.png').convert_alpha()
nv1 = pygame.transform.scale(nv1,(nv_w,nv_h))

nv2 = pygame.image.load('image/ball/cityball.png').convert_alpha()
nv2 = pygame.transform.scale(nv2,(nv_w,nv_h))

nv3 = pygame.image.load('image/ball/metal_ball.png').convert_alpha()
nv3 = pygame.transform.scale(nv3,(nv_w,nv_h))

nv4 = pygame.image.load('image/ball/earthball.png').convert_alpha()
nv4 = pygame.transform.scale(nv4,(nv_w,nv_h))

nv5 = pygame.image.load('image/ball/knifeball.png').convert_alpha()
nv5 = pygame.transform.scale(nv5,(nv_w,nv_h))

nv6 = pygame.image.load('image/ball/ppball.png').convert_alpha()
nv6 = pygame.transform.scale(nv6,(nv_w,nv_h))

coin=pygame.image.load('image/value/coin.png').convert_alpha()
coin=pygame.transform.scale(coin,(50,50))

pink=pygame.image.load('image/background/pink.jpg').convert_alpha()
menuimage=pygame.transform.scale(pink,(200,80))

buybutton=pygame.transform.scale(pink,(200,100))


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = obj
        self.surf = pygame.Surface((objwidth ,objheight))
        self.rect = self.surf.get_rect(center = (random.randint(objwidth,SCREEN_WIDTH-objwidth), 0))
        self.alive=True
        

    def move(self):
            global LIFE
            self.rect.move_ip(0,SPEED)
            if (self.rect.bottom >= (SCREEN_HEIGHT-75)):
                
                self.rect.top = 0
                self.rect.center = (random.randint(objwidth//2,SCREEN_WIDTH-objwidth//2), 0)
                return True
            return False            
                
            
 
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
                  self.rect.move_ip(-7, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
                  self.rect.move_ip(7, 0)
    
    def draw(self,screen):
        player_idle=pygame.sprite.Group()
        player_idle.add(self)
        player_idle.update(0.5)
        player_idle.draw(screen)
                   
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
        DISPLAYSURF.blit(METALFLOOR,(0,SCREEN_HEIGHT-150))
        DISPLAYSURF.blit(METALFLOOR,(150,SCREEN_HEIGHT-150))
        DISPLAYSURF.blit(METALFLOOR,(300,SCREEN_HEIGHT-150))
        # DISPLAYSURF.blit(GRASS,(0,SCREEN_HEIGHT-(150*2)))
        DISPLAYSURF.blit(METALFLOOR,(450,SCREEN_HEIGHT-150))
        
        # DISPLAYSURF.blit(GRASS,(SCREEN_WIDTH-300,SCREEN_HEIGHT-(150*2)))
        
         

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
Player1=Player()
 
bg = Background()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
Char = pygame.sprite.Group()
Char.add(P1)






# obj_group=pygame.sprite.Group()


#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
    
# def gameover():
#     # DISPLAYSURF.fill(WHITE)
#     Game_over_label=font.render("GOODLUCK NEXT TIME",1,BLACK)
#     Restart_label=font.render("PRESS SPACE TO RESTART",1,BLACK)
#     DISPLAYSURF.blit(Game_over_label,(SCREEN_WIDTH/2 - Game_over_label.get_width()/2, 400))
#     DISPLAYSURF.blit(Restart_label,(SCREEN_WIDTH/2 - Restart_label.get_width()/2, 500))
#     pygame.display.update()


def getHighestScore():
    with open("highest score.txt","r") as f:
        return f.read()

def Coin():
    with open("coin.txt","r") as f:
        return f.read()

def get_font(size): 
    return pygame.font.Font("8-BIT WONDER.TTF", size)

def ShopID():
    with open("ID.txt","r") as f:
        return f.read()

playerDraw=False
def play():
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
                SPEED += 0.1     
            if event.type == QUIT:
                run=False
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
                        # PredictResult=imagePredict.Proccess(W,yDraw,RANK,line)
                        PredictResult=grap.Proccess(line)
                        line=[]
                        if PredictResult:
                            LIFE+=1
                            RANK=(LIFE+4)//4
                            grap.CreateGraph(RANK)
                            # W,yDraw=generator.CreateGraph(RANK,'dothi.png')
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

        LIFES = font_small.render(f"SCORE: {LIFE}", True, BLACK)
        DISPLAYSURF.blit(LIFES, (10,10))

        HIGHSCORE = font_small.render(f"HIGHEST SCORE: {highestScore}", True, BLACK)
        DISPLAYSURF.blit(HIGHSCORE, (10,30))
    
        #Moves and Re-draws all Sprites
        Player1.move()
        # for entity in Char:
        #     DISPLAYSURF.blit(entity.image, entity.rect)
        #     entity.move()
        # conclide=False
        for entity in enemies:
            DISPLAYSURF.blit(entity.image, entity.rect)
            echk=entity.move()
            # if echk:
            #     conclide=True
        # if conclide:
        #     LIFE -= 2
        with open('ID.txt', 'r') as file:
            data = file.readlines()
        SELECTED1=data[10][9:]
        SELECTED1=list(SELECTED1.split())

        SELECTED2=data[12][9:]
        SELECTED2=list(SELECTED2.split())
        if len(line)>1:
            for i in range(1,len(line)):
                if SELECTED1[0]=='LAVA':
                    pygame.draw.line(DISPLAYSURF,BLOOD,(line[i-1][0],line[i-1][1]),(line[i][0],line[i][1]),9)
                    pygame.draw.line(DISPLAYSURF,LAVA,(line[i-1][0],line[i-1][1]),(line[i][0],line[i][1]),5)
                else:
                    pygame.draw.line(DISPLAYSURF,SELECTED1[0],(line[i-1][0],line[i-1][1]),(line[i][0],line[i][1]),9)
                    pygame.draw.line(DISPLAYSURF,SELECTED2[0],(line[i-1][0],line[i-1][1]),(line[i][0],line[i][1]),5)
                # pygame.draw.line(DISPLAYSURF,WHITE,(line[i-1][0],line[i-1][1]),(line[i][0],line[i][1]),3)
        #To be run if collision occurs between Player and Enemy
        # print(Player1.rect,'',E1.rect)
        if pygame.sprite.collide_rect(Player1,E1):
        #     #   pygame.mixer.Sound('crash.wav').play()
        #     #   time.sleep(0.8)
            
            print('collide')
            run=False
            E1.rect.top = 0
            Player1.rect.center=(300, 700)
            line=[]
            GameOver(LIFE)
        #     # DISPLAYSURF.fill(RED)
        #     # DISPLAYSURF.blit(game_over, (30,250))
            
            
        #     # for entity in enemies:
        #     #         # entity.kill()
        #     #         LIFE=LIFE - 1 
        # if LIFE<=0:
        #         # GameOver()
        #         # time.sleep(1.5)
        #         # pygame.quit()
        #         # sys.exit()  
        #     GameOver()
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
        Player1.draw(DISPLAYSURF)
        pygame.display.update()
        fpsclock.tick(FPS)
    pygame.quit()
    



def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 
# GameStage()
def items(screen,nv,ImgPosition,textPosition,text,bColor="Black",hColor="Green"):
    SCREEN.blit(nv,ImgPosition)
    STORE_BUY= Button(image=None, pos=textPosition, text_input= text, font=get_font(30), base_color=bColor, hovering_color=hColor)
    return STORE_BUY

def Buyitems(screen,textPosition,text,bColor="Gray",hColor="Green"):
    STORE_BUY= Button(image=None, pos=textPosition, text_input= text, font=get_font(30), base_color=bColor, hovering_color=hColor)
    return STORE_BUY




def shop():
    while True:
        SCREEN.fill(WHITE)
        #SCREEN.blit(the, (40, -140))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        SHOP_TEXT = get_font(30).render("shop", True,BLACK)
        SHOP_RECT = SHOP_TEXT.get_rect(center=(SCREEN_W/2, 100))

        SHOP_BALL_BUTTON = Button(menuimage, pos=(SCREEN_W/2, 350), 
                            text_input="BALL", font=get_font(30), base_color="#CCFFFF", hovering_color="White")
        SHOP_LINE_BUTTON = Button(menuimage, pos=(SCREEN_W/2, 470), 
                            text_input="LINE", font=get_font(30), base_color="#CCFFFF", hovering_color="White")
        SHOP_BACK_BUTTON = Button(menuimage, pos=(SCREEN_W/2, SCREEN_H-100), 
                            text_input="BACK", font=get_font(30), base_color="#CCFFFF", hovering_color="White")

        SCREEN.blit(SHOP_TEXT, SHOP_RECT)

        for button in [SHOP_BALL_BUTTON, SHOP_LINE_BUTTON,SHOP_BACK_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if CREDIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                #    lan()
                if SHOP_BALL_BUTTON.checkForInput(MENU_MOUSE_POS):
                    store_1()
                if SHOP_LINE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    store_line_1()
                if SHOP_BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()   

        pygame.display.update()
def store_line_1():
    playerCoi=addCoin()
    ITEMS=['GREEN','BLACK','YELLOW']
    while True:
        
        with open('ID.txt', 'r') as file:
            data = file.readlines()
        SELECTED=data[6][9:]
        SELECTED=list(map(int,SELECTED.split()))
        # SELECTEDLINE=data[10][9:]
        # SELECTEDLINE=list(SELECTEDLINE.split())
        BOUGHT=data[35:38]
        # print(SELECTED)
        STORE_MOUSE_POS = pygame.mouse.get_pos()
     
        SCREEN.fill(WHITE)
        for i in BOUGHT:
            XC=int(i.split()[1])
            YC=int(i.split()[2])
            if(i.split()[3]=='OWNED'):
                OPTEXT = get_font(20).render("OWNED", True,'Gray')
                SCREEN.blit(OPTEXT,(XC,YC))
            else: 
                OPTEXT = get_font(20).render("1000", True,'Gray')
                SCREEN.blit(OPTEXT,(XC+20,YC))
        
        pygame.draw.rect(SCREEN,'Gray', pygame.Rect(SELECTED[0],SELECTED[1],SELECTED[2],SELECTED[3]))
    
        OPTIONS_TEXT = get_font(20).render("LINE COLOR", True, BLACK)
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(SCREEN_W/2,100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK_MENU = Button(menuimage, pos=(100, SCREEN_H-100), 
                            text_input="BACK", font=get_font(30), base_color="Black", hovering_color="Green")

        OPTIONS_MENU = Button(menuimage, pos=(300, SCREEN_H-100), 
                            text_input="MENU", font=get_font(30), base_color="Black", hovering_color="Green")

        OPTIONS_NEXT = Button(menuimage, pos=(500, SCREEN_H-100), 
                            text_input="NEXT", font=get_font(30), base_color="Black", hovering_color="Green")

        
        #make character store                    
        STORE_BUY_line1=items(SCREEN,nv1,(50,200),(300,250),ITEMS[0])
        # STORE_BUY_BUTTON_nv1=Buyitems(SCREEN,(520,250),'100')
        
        STORE_BUY_line2= items(SCREEN,nv2,(50,350),(300,400),ITEMS[1])
        
        # STORE_BUY_BUTTON_nv2=Buyitems(SCREEN,(520,400),'100')

        STORE_BUY_line3= items(SCREEN,nv3,(50,500),(300,550),ITEMS[2])
        # STORE_BUY_BUTTON_nv3=Buyitems(SCREEN,(520,550),'100')

        for button in [OPTIONS_BACK_MENU,OPTIONS_MENU,OPTIONS_NEXT,STORE_BUY_line1,STORE_BUY_line2,STORE_BUY_line3]:
            button.changeColor(STORE_MOUSE_POS)
            button.update(SCREEN)

        COINS = font.render(f"{playerCoi}", True, BLACK)
        SCREEN.blit(COINS, (70,91))
        SCREEN.blit(coin,(5,80))

        with open("coin.txt","w") as f:
            f.write(str(playerCoi))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK_MENU.checkForInput(STORE_MOUSE_POS):
                    main_menu()
                if OPTIONS_MENU.checkForInput(STORE_MOUSE_POS):
                    main_menu()
                if OPTIONS_NEXT.checkForInput(STORE_MOUSE_POS):
                    store_line_2()
                if STORE_BUY_line1.checkForInput(STORE_MOUSE_POS):
                    CHECK=data[35]
                    CHECK=CHECK.split()
                    if playerCoi>=1000 and CHECK[3]=='BUYNT':
                        playerCoi+=-1000
                        temp=data[35]
                        temp=temp.split()
                        temp[3]='OWNED\n'
                        st=" ".join(temp)
                        data[35]=st
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                        # SELECTED=data[2][9:]
                        # SELECTED=list(map(int,SELECTED.split(',')))
                        BOUGHT=data[35:38]
                   
                    if CHECK[3]=='OWNED' and STORE_BUY_line1.checkForInput(STORE_MOUSE_POS):
                        #thay doi mau net ve lon
                        templine=data[10].split()
                        templine[1]='GREEN'
                        templine[2]='7\n'
                        stline=" ".join(templine)
                        data[10]=stline
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                        #thay doi mau net ve nho
                        templinesmall=data[12].split()
                        templinesmall[1]='WHITE'
                        templinesmall[2]='7\n'
                        stlinesmall=" ".join(templinesmall)
                        data[12]=stlinesmall
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                        #thay doi o select
                        temp=data[6].split()
                        temp[2]='200'
                        temp[4]='100\n'
                        st=" ".join(temp)
                        data[6]=st
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))

                if STORE_BUY_line2.checkForInput(STORE_MOUSE_POS):
                    CHECK=data[36]
                    CHECK=CHECK.split()
                    if playerCoi>=1000 and CHECK[3]=='BUYNT':
                        playerCoi+=-1000
                        temp=data[36]
                        temp=temp.split()
                        temp[3]='OWNED\n'
                        st=" ".join(temp)
                        data[36]=st
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                        # SELECTED=data[2][9:]
                        # SELECTED=list(map(int,SELECTED.split(',')))
                        BOUGHT=data[35:38]
                   
                    if CHECK[3]=='OWNED' and STORE_BUY_line2.checkForInput(STORE_MOUSE_POS):
                        #thay doi mau net ve
                        templine=data[10].split()
                        templine[1]='BLACK'
                        templine[2]='7\n'
                        stline=" ".join(templine)
                        data[10]=stline
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                        #thay doi mau net ve nho
                        templinesmall=data[12].split()
                        templinesmall[1]='WHITE'
                        templinesmall[2]='7\n'
                        stlinesmall=" ".join(templinesmall)
                        data[12]=stlinesmall
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                        #thay doi o select
                        temp=data[6].split()
                        temp[2]='350'
                        temp[4]='100\n'
                        st=" ".join(temp)
                        data[6]=st
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))

                if STORE_BUY_line3.checkForInput(STORE_MOUSE_POS):
                    CHECK=data[37]
                    CHECK=CHECK.split()
                    if playerCoi>=1000 and CHECK[3]=='BUYNT':
                        playerCoi+=-1000
                        temp=data[37]
                        temp=temp.split()
                        temp[3]='OWNED\n'
                        st=" ".join(temp)
                        data[37]=st
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                        # SELECTED=data[2][9:]
                        # SELECTED=list(map(int,SELECTED.split(',')))
                        BOUGHT=data[35:38]
                   
                    if CHECK[3]=='OWNED' and STORE_BUY_line3.checkForInput(STORE_MOUSE_POS):
                        #thay doi mau net ve
                        templine=data[10].split()
                        templine[1]='YELLOW'
                        templine[2]='7\n'
                        stline=" ".join(templine)
                        data[10]=stline
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                        #thay doi mau net ve nho
                        templinesmall=data[12].split()
                        templinesmall[1]='WHITE'
                        templinesmall[2]='7\n'
                        stlinesmall=" ".join(templinesmall)
                        data[12]=stlinesmall
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                        #thay doi o select
                        temp=data[6].split()
                        temp[2]='500'
                        temp[4]='100\n'
                        st=" ".join(temp)
                        data[6]=st
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
        pygame.display.update()
        
def store_line_2():
    playerCoi=addCoin()
    ITEMS=['AQUA','TEAL','LAVA']
    while True:
        
        with open('ID.txt', 'r') as file:
            data = file.readlines()
        SELECTED=data[8][9:]
        SELECTED=list(map(int,SELECTED.split()))
        # SELECTEDLINE=data[10][9:]
        # SELECTEDLINE=list(SELECTEDLINE.split())
        BOUGHT=data[40:43]
        # print(SELECTED)
        STORE_MOUSE_POS = pygame.mouse.get_pos()
     
        SCREEN.fill(WHITE)
        for i in BOUGHT:
            XC=int(i.split()[1])
            YC=int(i.split()[2])
            if(i.split()[3]=='OWNED'):
                OPTEXT = get_font(20).render("OWNED", True,'Gray')
                SCREEN.blit(OPTEXT,(XC,YC))
            else: 
                OPTEXT = get_font(20).render("1000", True,'Gray')
                SCREEN.blit(OPTEXT,(XC+20,YC))
        
        pygame.draw.rect(SCREEN,'Gray', pygame.Rect(SELECTED[0],SELECTED[1],SELECTED[2],SELECTED[3]))
    
        OPTIONS_TEXT = get_font(20).render("LINE COLOR", True, BLACK)
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(SCREEN_W/2,100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK_MENU = Button(menuimage, pos=(100, SCREEN_H-100), 
                            text_input="BACK", font=get_font(30), base_color="Black", hovering_color="Green")

        OPTIONS_MENU = Button(menuimage, pos=(300, SCREEN_H-100), 
                            text_input="MENU", font=get_font(30), base_color="Black", hovering_color="Green")

        OPTIONS_NEXT = Button(menuimage, pos=(500, SCREEN_H-100), 
                            text_input="NEXT", font=get_font(30), base_color="Black", hovering_color="Green")

        
        #make character store                    
        STORE_BUY_line4=items(SCREEN,nv1,(50,200),(300,250),ITEMS[0])
        # STORE_BUY_BUTTON_nv1=Buyitems(SCREEN,(520,250),'100')
        
        STORE_BUY_line5= items(SCREEN,nv2,(50,350),(300,400),ITEMS[1])
        
        # STORE_BUY_BUTTON_nv2=Buyitems(SCREEN,(520,400),'100')

        STORE_BUY_line6= items(SCREEN,nv3,(50,500),(300,550),ITEMS[2])
        # STORE_BUY_BUTTON_nv3=Buyitems(SCREEN,(520,550),'100')

        for button in [OPTIONS_BACK_MENU,OPTIONS_MENU,OPTIONS_NEXT,STORE_BUY_line4,STORE_BUY_line5,STORE_BUY_line6]:
            button.changeColor(STORE_MOUSE_POS)
            button.update(SCREEN)

        COINS = font.render(f"{playerCoi}", True, BLACK)
        SCREEN.blit(COINS, (70,91))
        SCREEN.blit(coin,(5,80))

        with open("coin.txt","w") as f:
            f.write(str(playerCoi))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK_MENU.checkForInput(STORE_MOUSE_POS):
                    store_line_1()
                if OPTIONS_MENU.checkForInput(STORE_MOUSE_POS):
                    main_menu()
                # if OPTIONS_NEXT.checkForInput(STORE_MOUSE_POS):
                #     store_2()
                if STORE_BUY_line4.checkForInput(STORE_MOUSE_POS):
                    CHECK=data[40]
                    CHECK=CHECK.split()
                    if playerCoi>=1000 and CHECK[3]=='BUYNT':
                        playerCoi+=-1000
                        temp=data[40]
                        temp=temp.split()
                        temp[3]='OWNED\n'
                        st=" ".join(temp)
                        data[40]=st
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                        # SELECTED=data[2][9:]
                        # SELECTED=list(map(int,SELECTED.split(',')))
                        BOUGHT=data[40:43]
                   
                    if CHECK[3]=='OWNED' and STORE_BUY_line4.checkForInput(STORE_MOUSE_POS):
                        #thay doi mau net ve
                        templine=data[10].split()
                        templine[1]='AQUA'
                        templine[2]='7\n'
                        stline=" ".join(templine)
                        data[10]=stline
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                        #thay doi mau net ve nho
                        templinesmall=data[12].split()
                        templinesmall[1]='WHITE'
                        templinesmall[2]='7\n'
                        stlinesmall=" ".join(templinesmall)
                        data[12]=stlinesmall
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                        #thay doi o select
                        temp=data[8].split()
                        temp[2]='200'
                        temp[4]='100\n'
                        st=" ".join(temp)
                        data[8]=st
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))

                if STORE_BUY_line5.checkForInput(STORE_MOUSE_POS):
                    CHECK=data[41]
                    CHECK=CHECK.split()
                    if playerCoi>=1000 and CHECK[3]=='BUYNT':
                        playerCoi+=-1000
                        temp=data[41]
                        temp=temp.split()
                        temp[3]='OWNED\n'
                        st=" ".join(temp)
                        data[41]=st
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                        # SELECTED=data[2][9:]
                        # SELECTED=list(map(int,SELECTED.split(',')))
                        BOUGHT=data[40:43]
                   
                    if CHECK[3]=='OWNED' and STORE_BUY_line5.checkForInput(STORE_MOUSE_POS):
                        #thay doi mau net ve
                        templine=data[10].split()
                        templine[1]='TEAL'
                        templine[2]='7\n'
                        stline=" ".join(templine)
                        data[10]=stline
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                        #thay doi mau net ve nho
                        templinesmall=data[12].split()
                        templinesmall[1]='WHITE'
                        templinesmall[2]='7\n'
                        stlinesmall=" ".join(templinesmall)
                        data[12]=stlinesmall
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                        #thay doi o select
                        temp=data[8].split()
                        temp[2]='350'
                        temp[4]='100\n'
                        st=" ".join(temp)
                        data[8]=st
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))

                if STORE_BUY_line6.checkForInput(STORE_MOUSE_POS):
                    CHECK=data[42]
                    CHECK=CHECK.split()
                    if playerCoi>=1000 and CHECK[3]=='BUYNT':
                        playerCoi+=-1000
                        temp=data[42]
                        temp=temp.split()
                        temp[3]='OWNED\n'
                        st=" ".join(temp)
                        data[42]=st
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                        # SELECTED=data[2][9:]
                        # SELECTED=list(map(int,SELECTED.split(',')))
                        BOUGHT=data[40:43]
                   
                    if CHECK[3]=='OWNED' and STORE_BUY_line6.checkForInput(STORE_MOUSE_POS):
                        #thay doi mau net ve
                        templine=data[10].split()
                        templine[1]='LAVA'
                        templine[2]='7\n'
                        stline=" ".join(templine)
                        data[10]=stline
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                        #thay doi mau net ve nho
                        templinesmall=data[12].split()
                        templinesmall[1]='BLOOD'
                        templinesmall[2]='7\n'
                        stlinesmall=" ".join(templinesmall)
                        data[12]=stlinesmall
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                        #thay doi o select
                        temp=data[8].split()
                        temp[2]='500'
                        temp[4]='100\n'
                        st=" ".join(temp)
                        data[8]=st
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                
        pygame.display.update()
        

def store_1():
    playerCoi=addCoin()
    ITEMS=['HEXAGON','CITYBALL','METALBALL']
    while True:
        
        with open('ID.txt', 'r') as file:
            data = file.readlines()
        SELECTED=data[2][9:]
        SELECTED=list(map(int,SELECTED.split()))
        BOUGHT=data[20:23]
        # print(SELECTED)
        STORE_MOUSE_POS = pygame.mouse.get_pos()
     
        SCREEN.fill(WHITE)
        for i in BOUGHT:
            XC=int(i.split()[1])
            YC=int(i.split()[2])
            if(i.split()[3]=='OWNED'):
                OPTEXT = get_font(20).render("OWNED", True,'Gray')
                SCREEN.blit(OPTEXT,(XC,YC))
            else: 
                OPTEXT = get_font(20).render("1000", True,'Gray')
                SCREEN.blit(OPTEXT,(XC+20,YC))
        
        pygame.draw.rect(SCREEN,'Gray', pygame.Rect(SELECTED[0],SELECTED[1],SELECTED[2],SELECTED[3]))
    
        OPTIONS_TEXT = get_font(20).render("STORE", True, BLACK)
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(SCREEN_W/2,100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK_MENU = Button(menuimage, pos=(100, SCREEN_H-100), 
                            text_input="BACK", font=get_font(30), base_color="Black", hovering_color="Green")

        OPTIONS_MENU = Button(menuimage, pos=(300, SCREEN_H-100), 
                            text_input="MENU", font=get_font(30), base_color="Black", hovering_color="Green")

        OPTIONS_NEXT = Button(menuimage, pos=(500, SCREEN_H-100), 
                            text_input="NEXT", font=get_font(30), base_color="Black", hovering_color="Green")

        
        #make character store                    
        STORE_BUY_nv1=items(SCREEN,nv1,(50,200),(300,250),ITEMS[0])
        # STORE_BUY_BUTTON_nv1=Buyitems(SCREEN,(520,250),'100')
        
        STORE_BUY_nv2= items(SCREEN,nv2,(50,350),(300,400),ITEMS[1])
        
        # STORE_BUY_BUTTON_nv2=Buyitems(SCREEN,(520,400),'100')

        STORE_BUY_nv3= items(SCREEN,nv3,(50,500),(300,550),ITEMS[2])
        # STORE_BUY_BUTTON_nv3=Buyitems(SCREEN,(520,550),'100')

        for button in [OPTIONS_BACK_MENU,OPTIONS_MENU,OPTIONS_NEXT,STORE_BUY_nv1,STORE_BUY_nv2,STORE_BUY_nv3]:
            button.changeColor(STORE_MOUSE_POS)
            button.update(SCREEN)

        COINS = font.render(f"{playerCoi}", True, BLACK)
        SCREEN.blit(COINS, (70,91))
        SCREEN.blit(coin,(5,80))

        with open("coin.txt","w") as f:
            f.write(str(playerCoi))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK_MENU.checkForInput(STORE_MOUSE_POS):
                    shop()
                if OPTIONS_MENU.checkForInput(STORE_MOUSE_POS):
                    main_menu()
                if OPTIONS_NEXT.checkForInput(STORE_MOUSE_POS):
                    temp=data[2].split()
                    temp[2]='-200'
                    temp[4]='0\n'
                    st=" ".join(temp)
                    data[2]=st
                    with open("ID.txt","w") as f:
                        f.write(listToString(data))
                    store_2()
                if STORE_BUY_nv1.checkForInput(STORE_MOUSE_POS):
                    CHECK=data[20]
                    CHECK=CHECK.split()
                    if CHECK[3]=='OWNED' and STORE_BUY_nv1.checkForInput(STORE_MOUSE_POS):
                        print(1111)                  
                        Player1.image= pygame.transform.scale(pygame.image.load('image/ball/hexagont.png'),(nv_width,nv_height)).convert_alpha()
                        temp=data[2].split()
                        temp[2]='200'
                        temp[4]='100\n'
                        st=" ".join(temp)
                        data[2]=st
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                        
                if STORE_BUY_nv2.checkForInput(STORE_MOUSE_POS):
                    CHECK=data[21]
                    CHECK=CHECK.split()
                    if playerCoi>=1000 and CHECK[3]=='BUYNT':
                        playerCoi+=-1000
                        temp=data[21]
                        temp=temp.split()
                        temp[3]='OWNED\n'
                        st=" ".join(temp)
                        data[21]=st
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                        # SELECTED=data[2][9:]
                        # SELECTED=list(map(int,SELECTED.split(',')))
                        BOUGHT=data[20:23]
                   
                    if CHECK[3]=='OWNED' and STORE_BUY_nv2.checkForInput(STORE_MOUSE_POS):
                        print(2222)                  
                        Player1.image= pygame.transform.scale(pygame.image.load('image/ball/cityball.png'),(nv_width,nv_height)).convert_alpha()
                        temp=data[2].split()
                        temp[2]='350'
                        temp[4]='100\n'
                        st=" ".join(temp)
                        data[2]=st
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                       
                        

                if STORE_BUY_nv3.checkForInput(STORE_MOUSE_POS):
                    CHECK=data[22]
                    CHECK=CHECK.split()
                    if playerCoi>=1000 and CHECK[3]=='BUYNT':
                        playerCoi+=-1000
                        temp=data[22]
                        temp=temp.split()
                        temp[3]='OWNED\n'
                        st=" ".join(temp)
                        data[22]=st
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                        # SELECTED=data[2][9:]
                        # SELECTED=list(map(int,SELECTED.split(',')))
                        BOUGHT=data[20:23]
                    if CHECK[3]=='OWNED' and STORE_BUY_nv3.checkForInput(STORE_MOUSE_POS):
                        print(3333)
                        Player1.image= pygame.transform.scale(pygame.image.load('image/ball/metal_ball.png'),(nv_width,nv_height)).convert_alpha()
                        temp=data[2].split()
                        temp[2]='500'
                        temp[4]='100\n'
                        st=" ".join(temp)
                        data[2]=st
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                       
        pygame.display.update()

def store_2():
    playerCoi=addCoin()
    ITEMS=['EARTH BALL','KNIFE BALL','PUPLE BALL']
    # with open('ID.txt', 'r') as file:
    #     data = file.readlines()
    # SELECTED=data[2][9:]
    # SELECTED=list(map(int,SELECTED.split(',')))
    # BOUGHT=data[30:33]
    while True:

        with open('ID.txt', 'r') as file:
            data = file.readlines()
        SELECTED=data[4][9:]
        SELECTED=list(map(int,SELECTED.split()))
        BOUGHT=data[30:33]

        STORE_MOUSE_POS = pygame.mouse.get_pos()
     
        SCREEN.fill(WHITE)
        for i in BOUGHT:
            XC=int(i.split()[1])
            YC=int(i.split()[2])
            if(i.split()[3]=='OWNED'):
                OPTEXT = get_font(20).render("OWNED", True,'Gray')
                SCREEN.blit(OPTEXT,(XC,YC))
            else: 
                OPTEXT = get_font(20).render("1000", True,'Gray')
                SCREEN.blit(OPTEXT,(XC+20,YC))

        pygame.draw.rect(SCREEN,'Gray', pygame.Rect(SELECTED[0],SELECTED[1],SELECTED[2],SELECTED[3]))

        OPTIONS_TEXT = get_font(20).render("STORE", True, BLACK)
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(SCREEN_W/2,100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(menuimage, pos=(100, SCREEN_H-100), 
                            text_input="BACK", font=get_font(30), base_color="Black", hovering_color="Green")

        OPTIONS_MENU = Button(menuimage, pos=(300, SCREEN_H-100), 
                            text_input="MENU", font=get_font(30), base_color="Black", hovering_color="Green")

        OPTIONS_NEXT = Button(menuimage, pos=(500, SCREEN_H-100), 
                            text_input="NEXT", font=get_font(30), base_color="Black", hovering_color="Green")
        #make character store                    
    
        STORE_BUY_nv4= items(SCREEN,nv4,(50,200),(300,250),ITEMS[0])
        # STORE_BUY_BUTTON_nv4=Buyitems(SCREEN,(520,250),'BUY')

        STORE_BUY_nv5= items(SCREEN,nv5,(50,350),(300,400),ITEMS[1])
        # STORE_BUY_BUTTON_nv5=Buyitems(SCREEN,(520,400),'BUY')

        STORE_BUY_nv6= items(SCREEN,nv6,(50,500),(300,550),ITEMS[2])
        # STORE_BUY_BUTTON_nv6=Buyitems(SCREEN,(520,550),'BUY')

        for button in [OPTIONS_BACK,OPTIONS_MENU,OPTIONS_NEXT,STORE_BUY_nv4,STORE_BUY_nv5,STORE_BUY_nv6]:
            button.changeColor(STORE_MOUSE_POS)
            button.update(SCREEN)

        COINS = font.render(f"{playerCoi}", True, BLACK)
        DISPLAYSURF.blit(COINS, (70,92))
        SCREEN.blit(coin,(5,80))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(STORE_MOUSE_POS):
                    temp=data[4].split()
                    temp[2]='-200'
                    temp[4]='0\n'
                    st=" ".join(temp)
                    data[4]=st
                    with open("ID.txt","w") as f:
                        f.write(listToString(data))
                    store_1()
                    
                if OPTIONS_MENU.checkForInput(STORE_MOUSE_POS):
                    main_menu()

                if  STORE_BUY_nv4.checkForInput(STORE_MOUSE_POS):
                    CHECK=data[30]
                    CHECK=CHECK.split()
                    if playerCoi>=1000 and CHECK[3]=='BUYNT':
                        playerCoi+=-1000
                        temp=data[30]
                        temp=temp.split()
                        temp[3]='OWNED\n'
                        st=" ".join(temp)
                        data[30]=st
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                        # SELECTED=data[2][9:]
                        # SELECTED=list(map(int,SELECTED.split(',')))
                        BOUGHT=data[30:33]
                    if CHECK[3]=='OWNED' and STORE_BUY_nv4.checkForInput(STORE_MOUSE_POS):
                        print(4444)
                        Player1.image= pygame.transform.scale(pygame.image.load('image/ball/earthball.png'),(nv_width,nv_height)).convert_alpha()
                        temp=data[4].split()
                        temp[2]='200'
                        temp[4]='100\n'
                        st=" ".join(temp)
                        data[4]=st
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))

                if  STORE_BUY_nv5.checkForInput(STORE_MOUSE_POS):
                    CHECK=data[31]
                    CHECK=CHECK.split()
                    if playerCoi>=1000 and CHECK[3]=='BUYNT':
                        playerCoi+=-1000
                        temp=data[31]
                        temp=temp.split()
                        temp[3]='OWNED\n'
                        st=" ".join(temp)
                        data[31]=st
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                        # SELECTED=data[2][9:]
                        # SELECTED=list(map(int,SELECTED.split(',')))
                        BOUGHT=data[30:33]
                    if CHECK[3]=='OWNED' and STORE_BUY_nv5.checkForInput(STORE_MOUSE_POS):
                        print(5555)
                        Player1.image= pygame.transform.scale(pygame.image.load('image/ball/knifeball.png'),(nv_width,nv_height)).convert_alpha()
                        temp=data[4].split()
                        temp[2]='350'
                        temp[4]='100\n'
                        st=" ".join(temp)
                        data[4]=st
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))

                if  STORE_BUY_nv6.checkForInput(STORE_MOUSE_POS):
                    CHECK=data[32]
                    CHECK=CHECK.split()
                    if playerCoi>=1000 and CHECK[3]=='BUYNT':
                        playerCoi+=-1000
                        temp=data[32]
                        temp=temp.split()
                        temp[3]='OWNED\n'
                        st=" ".join(temp)
                        data[32]=st
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                        # SELECTED=data[2][9:]
                        # SELECTED=list(map(int,SELECTED.split(',')))
                        BOUGHT=data[30:33]
                    if CHECK[3]=='OWNED' and STORE_BUY_nv6.checkForInput(STORE_MOUSE_POS):
                        print(6666)
                        Player1.image= pygame.transform.scale(pygame.image.load('image/ball/ppball.png'),(nv_width,nv_height)).convert_alpha()
                        temp=data[4].split()
                        temp[2]='500'
                        temp[4]='100\n'
                        st=" ".join(temp)
                        data[4]=st
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))

                


        pygame.display.update()


def credit():
    while True:
           
        CREDITS_MOUSE_POS = pygame.mouse.get_pos()
     
        SCREEN.fill(WHITE)

        OPTIONS_TEXT = get_font(20).render("Credits", True, BLACK)
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(SCREEN_W/2, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(menuimage, pos=(SCREEN_W/2, SCREEN_H-100), 
                            text_input="BACK", font=get_font(30), base_color="Black", hovering_color="Green")

        CREATER_NHAN = Button(image=None, pos=(SCREEN_W/2, 250), 
                            text_input="MAKE BY NHAN", font=get_font(40), base_color="Black", hovering_color="Green")
        CREATER_MINH = Button(image=None, pos=(SCREEN_W/2, 350), 
                            text_input="MAKE BY MINH", font=get_font(40), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(CREDITS_MOUSE_POS)


        OPTIONS_BACK.update(SCREEN)
        for button in [OPTIONS_BACK,CREATER_NHAN,CREATER_MINH]:
            button.changeColor(CREDITS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(CREDITS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def GameOver(point):
    addCoin(point)
    
    while True:
        GAME_OVER_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill(WHITE)
        GAME_OVER_TEXT = get_font(20).render("GAME OVER", True, BLACK)
        GAME_OVER_RECT = GAME_OVER_TEXT.get_rect(center=(SCREEN_W/2, 100))
        SCREEN.blit(GAME_OVER_TEXT, GAME_OVER_RECT)

        GAME_OVER_BACK = Button(image=None, pos=(150, SCREEN_H-100), 
                            text_input="BACK", font=get_font(30), base_color="Black", hovering_color="Green")

        GAME_OVER_AGAIN = Button(image=None, pos=(450, SCREEN_H-100), 
                            text_input="PLAY AGAIN", font=get_font(30), base_color="Black", hovering_color="Green")

        GAME_OVER_BACK.update(SCREEN)

        for button in [GAME_OVER_BACK,GAME_OVER_AGAIN]:
            button.changeColor(GAME_OVER_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GAME_OVER_BACK.checkForInput(GAME_OVER_MOUSE_POS):
                    global LIFE
                    LIFE=0
                    global SPEED
                    SPEED=3
                    global RANK
                    RANK=1
                    line=[]
                    
                    global playerDraw
                    playerDraw=False
                    global W,yDraw
                    grap.CreateGraph(RANK)
                    global hinhdothi
                    dothi=pygame.image.load('dothi.png').convert_alpha()
                    hinhdothi=pygame.transform.scale(dothi,(100 ,100)).convert_alpha()
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GAME_OVER_AGAIN.checkForInput(GAME_OVER_MOUSE_POS):
                    # global LIFE
                    LIFE=0
                    # global SPEED
                    SPEED=3
                    # global RANK
                    RANK=1
                    # global line
                    
                    # global playerDraw
                    playerDraw=False
                    # global W,yDraw
                    grap.CreateGraph(RANK)
                    # global hinhdothi
                    dothi=pygame.image.load('dothi.png').convert_alpha()
                    hinhdothi=pygame.transform.scale(dothi,(100 ,100)).convert_alpha()

                    play()

        pygame.display.update()


def main_menu():
    
    while True:
        SCREEN.fill(WHITE)
        # SCREEN.blit(the, (40, -140))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(70).render("PTOUCH", True,BLACK)
        MENU_RECT = MENU_TEXT.get_rect(center=(SCREEN_W/2, 100))

        PLAY_BUTTON = Button(menuimage, pos=(SCREEN_W/2, 250), 
                            text_input="PLAY", font=get_font(30), base_color="#CCFFFF", hovering_color="White")
        STORE_BUTTON = Button(menuimage, pos=(SCREEN_W/2, 370), 
                            text_input="STORE", font=get_font(30), base_color="#CCFFFF", hovering_color="White")
        CREDITS_BUTTON = Button(menuimage, pos=(SCREEN_W/2, 490), 
                            text_input="CREDITS", font=get_font(30), base_color="#CCFFFF", hovering_color="White")
        QUIT_BUTTON = Button(menuimage, pos=(SCREEN_W/2, 610), 
                            text_input="QUIT", font=get_font(30), base_color="#CCFFFF", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [CREDITS_BUTTON,PLAY_BUTTON, STORE_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if CREDIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                #    lan()
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if STORE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    shop()
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credit()   
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()


