from utils import *

pygame.init()
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
# FPS 
fpsclock = pygame.time.Clock()
 
# colors

playerCoin=0

line=[] #STORE INPUT DRAWING


nv_w=100
nv_h=100

line_w=100
line_h=100

#Setting up Fonts
font = pygame.font.Font('8-BIT WONDER.TTF', 20)
font_small = pygame.font.SysFont("Verdana", 20)

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
SCREEN = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("ptouch")

RANK=1
grap=generator.Graph('dothi.png')
grap.CreateGraph(RANK)

dothi=pygame.image.load('dothi.png').convert_alpha()
hinhdothi=pygame.transform.scale(dothi,(100 ,100)).convert_alpha()

obj=pygame.image.load('image/enemy/bigdrill_3.png').convert_alpha()
obj=pygame.transform.scale(obj,(OBJWIDTH ,OBJHEIGHT)).convert_alpha()

nv = pygame.image.load('image/ball/hexagont.png').convert_alpha()
nv = pygame.transform.scale(nv,(NVWIDTH,NVHEIGHT))
 
BG=pygame.image.load('image/background/gray3.png').convert_alpha()
BG=pygame.transform.scale(BG,(SCREEN_WIDTH,1000))

FRAME=pygame.image.load('image/background/khungvuongmetal_1.png').convert_alpha()
FRAME=pygame.transform.scale(FRAME,(110,110))

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

green = pygame.image.load('image/line/greenline.png').convert_alpha()
green = pygame.transform.scale(green,(line_w,line_h))

black = pygame.image.load('image/line/blackline.png').convert_alpha()
black = pygame.transform.scale(black,(line_w,line_h))

yellow = pygame.image.load('image/line/yellowline.png').convert_alpha()
yellow = pygame.transform.scale(yellow,(line_w,line_h))

aqua = pygame.image.load('image/line/aqualine.png').convert_alpha()
aqua = pygame.transform.scale(aqua,(line_w,line_h))

teal = pygame.image.load('image/line/tealline.png').convert_alpha()
teal = pygame.transform.scale(teal,(line_w,line_h))

lava = pygame.image.load('image/line/lavaline.png').convert_alpha()
lava = pygame.transform.scale(lava,(line_w,line_h))

coin=pygame.image.load('image/value/coin.png').convert_alpha()
coin=pygame.transform.scale(coin,(50,50))

pink=pygame.image.load('image/background/pink.jpg').convert_alpha()
menuimage=pygame.transform.scale(pink,(200,80))

buybutton=pygame.transform.scale(pink,(200,100))

#background music
pygame.mixer.music.load('music/backgroundmusic.wav')
pygame.mixer.music.play(-1)


        
#Setting up Sprites        
P1 = Player(nv)
E1 = Enemy(obj)
Player1=Player(nv)
 
bg = Background(BG)
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
Char = pygame.sprite.Group()
Char.add(P1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
    




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
        highestScore = int(openTxt('highest score.txt'))
    except:
        highestScore = 0

    while run:
        
        #Cycles through all occurring events   
        for event in pygame.event.get():
            if event.type == INC_SPEED:
                SPEED += 0.1     
            if event.type == QUIT:
                run=False
            if pygame.mouse.get_pressed()[0]:
                    positionX,positionY=pygame.mouse.get_pos()
                    line.append((pygame.mouse.get_pos()))
                    playerDraw=True
            else:
                    if playerDraw==True:
                        playerDraw=False
                        PredictResult=grap.Proccess(line)
                        line=[]
                        if PredictResult:
                            LIFE+=1
                            RANK=(LIFE+4)//4
                            grap.CreateGraph(RANK)
                            # W,yDraw=generator.CreateGraph(RANK,'dothi.png')
                            dothi=pygame.image.load('dothi.png').convert_alpha()
                            hinhdothi=pygame.transform.scale(dothi,(100 ,100)).convert_alpha()               
            if event.type ==pygame.KEYDOWN:
                    if event.key==pygame.K_p:
                        line=[]
        bg.update()
        bg.draw(DISPLAYSURF,METALFLOOR,FRAME)
        DISPLAYSURF.blit(hinhdothi,(250,5)) 

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
        for entity in enemies:
            DISPLAYSURF.blit(entity.image, entity.rect)
            echk=entity.move()

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
                
        #To be run if collision occurs between Player and Enemy
        # print(Player1.rect,'',E1.rect)
        if pygame.sprite.collide_rect(Player1,E1): 
            print('collide')
            run=False
            E1.rect.top = 0
            Player1.rect.center=(300, 700)
            line=[]
            GameOver(LIFE)
        
        Player1.draw(DISPLAYSURF)
        pygame.display.update()
        fpsclock.tick(FPS)
    pygame.quit()
    




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
                if SHOP_BALL_BUTTON.checkForInput(MENU_MOUSE_POS):
                    store_1()
                if SHOP_LINE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    store_line_1()
                if SHOP_BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()   

        pygame.display.update()
def store_line_1():
    playerCoi=addCoin('coin.txt')
    ITEMS=['GREEN','BLACK','YELLOW']
    while True:
        
        with open('ID.txt', 'r') as file:
            data = file.readlines()
        SELECTED=data[6][9:]
        SELECTED=list(map(int,SELECTED.split()))
        BOUGHT=data[35:38]
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
        STORE_BUY_line1=items(SCREEN,green,(50,200),(300,250),ITEMS[0])
    
        STORE_BUY_line2= items(SCREEN,black,(50,350),(300,400),ITEMS[1])
        
        STORE_BUY_line3= items(SCREEN,yellow,(50,500),(300,550),ITEMS[2])
    
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
    playerCoi=addCoin('coin.txt')
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
        STORE_BUY_line4=items(SCREEN,aqua,(50,200),(300,250),ITEMS[0])
        
        STORE_BUY_line5= items(SCREEN,teal,(50,350),(300,400),ITEMS[1])

        STORE_BUY_line6= items(SCREEN,lava,(50,500),(300,550),ITEMS[2])

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
    playerCoi=addCoin('coin.txt')
    ITEMS=['HEXAGON','CITYBALL','METALBALL']
    while True:
        
        with open('ID.txt', 'r') as file:
            data = file.readlines()
        SELECTED=data[2][9:]
        SELECTED=list(map(int,SELECTED.split()))
        BOUGHT=data[20:23]
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
    
        OPTIONS_TEXT = get_font(20).render("BALL", True, BLACK)
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
        
        STORE_BUY_nv2= items(SCREEN,nv2,(50,350),(300,400),ITEMS[1])

        STORE_BUY_nv3= items(SCREEN,nv3,(50,500),(300,550),ITEMS[2])

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
                        Player1.image= pygame.transform.scale(pygame.image.load('image/ball/hexagont.png'),(NVWIDTH,NVHEIGHT)).convert_alpha()
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
                        BOUGHT=data[20:23]
                   
                    if CHECK[3]=='OWNED' and STORE_BUY_nv2.checkForInput(STORE_MOUSE_POS):
                        print(2222)                  
                        Player1.image= pygame.transform.scale(pygame.image.load('image/ball/cityball.png'),(NVWIDTH,NVHEIGHT)).convert_alpha()
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
                        BOUGHT=data[20:23]
                    if CHECK[3]=='OWNED' and STORE_BUY_nv3.checkForInput(STORE_MOUSE_POS):
                        print(3333)
                        Player1.image= pygame.transform.scale(pygame.image.load('image/ball/metal_ball.png'),(NVWIDTH,NVHEIGHT)).convert_alpha()
                        temp=data[2].split()
                        temp[2]='500'
                        temp[4]='100\n'
                        st=" ".join(temp)
                        data[2]=st
                        with open("ID.txt","w") as f:
                            f.write(listToString(data))
                       
        pygame.display.update()

def store_2():
    playerCoi=addCoin('coin.txt')
    ITEMS=['EARTH BALL','KNIFE BALL','PUPLE BALL']
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

        OPTIONS_TEXT = get_font(20).render("BALL", True, BLACK)
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

        STORE_BUY_nv5= items(SCREEN,nv5,(50,350),(300,400),ITEMS[1])

        STORE_BUY_nv6= items(SCREEN,nv6,(50,500),(300,550),ITEMS[2])

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
                        BOUGHT=data[30:33]
                    if CHECK[3]=='OWNED' and STORE_BUY_nv4.checkForInput(STORE_MOUSE_POS):
                        print(4444)
                        Player1.image= pygame.transform.scale(pygame.image.load('image/ball/earthball.png'),(NVWIDTH,NVHEIGHT)).convert_alpha()
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
                        BOUGHT=data[30:33]
                    if CHECK[3]=='OWNED' and STORE_BUY_nv5.checkForInput(STORE_MOUSE_POS):
                        print(5555)
                        Player1.image= pygame.transform.scale(pygame.image.load('image/ball/knifeball.png'),(NVWIDTH,NVHEIGHT)).convert_alpha()
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
                        BOUGHT=data[30:33]
                    if CHECK[3]=='OWNED' and STORE_BUY_nv6.checkForInput(STORE_MOUSE_POS):
                        print(6666)
                        Player1.image= pygame.transform.scale(pygame.image.load('image/ball/ppball.png'),(NVWIDTH,NVHEIGHT)).convert_alpha()
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
    addCoin('coin.txt',point)
    
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
                    LIFE=0               
                    SPEED=3                    
                    RANK=1                   
                    playerDraw=False
                    grap.CreateGraph(RANK)   
                    dothi=pygame.image.load('dothi.png').convert_alpha()
                    hinhdothi=pygame.transform.scale(dothi,(100 ,100)).convert_alpha()
                    play()

        pygame.display.update()


def main_menu():
    
    while True:
        SCREEN.fill(WHITE)

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


