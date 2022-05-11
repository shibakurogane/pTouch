from ast import Break, Global
from matplotlib import image
import pygame, sys
from button import Button
from pygame import Surface, mixer
from ptouch import *
 
# Setup pygame/window ---------------------------------------- #
FPS=60
fpsclock = pygame.time.Clock()
from pygame.locals import *

pygame.init()

pygame.display.set_caption('game menu')

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)

Player1=Player()

SCREEN_W=600
SCREEN_H=800

nv_w=100
nv_h=100

LIFE=12

SCREEN = pygame.display.set_mode((SCREEN_W, SCREEN_H))

nv1 = pygame.image.load('wizard.png').convert_alpha()
nv1 = pygame.transform.scale(nv1,(nv_w,nv_h))

nv2 = pygame.image.load('lanternguy.png').convert_alpha()
nv2 = pygame.transform.scale(nv2,(nv_w,nv_h))

pink=pygame.image.load('pink.jpg').convert_alpha()
menuimage=pygame.transform.scale(pink,(200,80))

buybutton=pygame.transform.scale(pink,(200,100))


 
font = pygame.font.Font('8-BIT WONDER.TTF', 20)
 


def get_font(size): 
    return pygame.font.Font("8-BIT WONDER.TTF", size)
 
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
    
    # LIFE=12
    
    while run:
        #Cycles through all occurring events   
        for event in pygame.event.get():
            if event.type == INC_SPEED:
                SPEED += 0.5      
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
        SCREEN.blit(LIFES, (10,10))

        HIGHSCORE = font_small.render(f"HIGHEST SCORE: {highestScore}", True, BLACK)
        DISPLAYSURF.blit(HIGHSCORE, (10,30))

        Player1.move()
        # #Moves and Re-draws all Sprites
        # for entity in Char:
        #     DISPLAYSURF.blit(entity.image, entity.rect)
        #     entity.move()
        for entity in enemies:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move(W,yDraw,RANK,line,playerDraw)
        for i in range(len(line)):
                pygame.draw.circle(DISPLAYSURF,BLACK,(line[i][0],line[i][1]),2)
        
        
        #To be run if collision occurs between Player and Enemy
        if pygame.sprite.spritecollideany(Player1,enemies):
            #   pygame.mixer.Sound('crash.wav').play()
            #   time.sleep(0.8)
                        
            # DISPLAYSURF.fill(RED)
            # DISPLAYSURF.blit(game_over, (30,250))
            for entity in enemies:
                    # entity.kill()
                    LIFE=LIFE-1
                  
        if LIFE<=0:
            #run=False
            GameOver()
        
        
        
        Player1.draw(DISPLAYSURF)
        pygame.display.update()
        fpsclock.tick(FPS)
    pygame.quit()
    
 
def store():
    while True:
           
        STORE_MOUSE_POS = pygame.mouse.get_pos()
     
        SCREEN.fill(WHITE)

        OPTIONS_TEXT = get_font(20).render("STORE", True, BLACK)
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(SCREEN_W/2,100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(menuimage, pos=(SCREEN_W/2, SCREEN_H-100), 
                            text_input="BACK", font=get_font(30), base_color="Black", hovering_color="Green")
        #make character store                    
        SCREEN.blit(nv1,(50,200))
        STORE_BUY_nv1= Button(image=None, pos=(300,250), 
                            text_input= "WIZAD", font=get_font(30), base_color="Black", hovering_color="Green")

        SCREEN.blit(nv2,(50,350))
        STORE_BUY_nv2= Button(image=None, pos=(300,400), 
                            text_input="LANTERN GUY", font=get_font(30), base_color="Black", hovering_color="Green")

        for button in [OPTIONS_BACK,STORE_BUY_nv1,STORE_BUY_nv2]:
            button.changeColor(STORE_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(STORE_MOUSE_POS):
                    main_menu()
                elif STORE_BUY_nv2.checkForInput(STORE_MOUSE_POS):
                    Player1.image= pygame.transform.scale(pygame.image.load('lanternguy.png'),(nv_width,nv_height)).convert_alpha()
                elif STORE_BUY_nv1.checkForInput(STORE_MOUSE_POS):
                    Player1.image= pygame.transform.scale(pygame.image.load('wizard.png'),(nv_width,nv_height)).convert_alpha()

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

def GameOver():
    while True:
        GAME_OVER_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(WHITE)

        GAME_OVER_TEXT = get_font(20).render("GAME OVER", True, BLACK)
        GAME_OVER_RECT = GAME_OVER_TEXT.get_rect(center=(SCREEN_W/2, 100))
        SCREEN.blit(GAME_OVER_TEXT, GAME_OVER_RECT)

        GAME_OVER_BACK = Button(menuimage, pos=(SCREEN_W/2, SCREEN_H-100), 
                            text_input="BACK", font=get_font(30), base_color="Black", hovering_color="Green")

        GAME_OVER_BACK.update(SCREEN)

        for button in [ GAME_OVER_BACK]:
            button.changeColor(GAME_OVER_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GAME_OVER_BACK.checkForInput(GAME_OVER_MOUSE_POS):
                    # global LIFE
                    # LIFE=13
                    main_menu()

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
                    store()
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credit()   
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()

