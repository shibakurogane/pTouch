
import pygame , sys
from pygame.locals import *
import random,time

pygame.init()

#fps
fpsclock = pygame.time.Clock()
FPS=30

chieurongx = 700
chieucaoy = 700
imgheight = 50
imgwidth = 50
objheight = 50
objwidth = 50
SCORE=0

DISPLAYSURF = pygame.display.set_mode((chieurongx, chieucaoy))
pygame.display.set_caption('tPython')

#image
nv = pygame.image.load('wizard.png').convert_alpha()
nv = pygame.transform.scale(nv,(50,50))

#background
BG=pygame.image.load('black.png').convert_alpha()
BG=pygame.transform.scale(BG,(chieurongx,800))

#object
obj=pygame.image.load('gach.webp').convert_alpha()
obj=pygame.transform.scale(obj,(objheight ,objwidth))

class Background():
    def __init__(self,x,y,speed):
        # self.pink = pygame.transform.scale(BG,(600,500))
        self.x=x
        self.y=y
        self.speed=speed
        self.img=BG
        self.width=self.img.get_width()
        self.height=self.img.get_height()
    def draw(self):
        DISPLAYSURF.blit(self.img,(self.x,self.y))
        DISPLAYSURF.blit(self.img,(self.x,self.y-self.height))
    def update(self):
        # self.x -= self.speed
        # if self.x < -self.width:
        #     self.x += self.width
        self.y += self.speed
        if self.y > self.height:
            self.y -= self.height


# them các object            
class Object(pygame.sprite.Sprite): 
    def __init__(self,img,x,y,speed): 
        pygame.sprite.Sprite.__init__(self)
        self.x=x
        self.y=y
        self.speed=speed
        self.image=obj
        self.width=self.image.get_width()
        self.height=self.image.get_height()
        self.rect=self.image.get_rect(topleft=(self.x,self.y))
    
    def update(self,bg):
        # self.x -= self.speed
        # if self.x < -self.width:
        #     self.x += self.width
        self.rect.centery += self.speed
        if self.rect.centery >= bg.height:
            self.rect.centery -= bg.height

obj_group=pygame.sprite.Group()
Number_obj=[(300,int(chieucaoy-50),10),(0,600,10)]
for i in Number_obj:
    objs = Object(obj,*i)
    obj_group.add(objs)



#load animation
dir_='animation/'
animation_=[]

actor_w,actor_h=150,120
for i in range(1,12):
    actor = pygame.image.load(dir_ + str(i) + '.png')
    actor = pygame.transform.scale(actor,(actor_w,actor_h))
    animation_.append(actor)



class Player():
    def __init__(self,x,y,animation_list):
        self.x=x
        self.y=y
        self.animation_list=animation_list
        self.img = animation_list[0]
        self.frame=0
        self.time_init=pygame.time.get_ticks()
    def draw(self):
        self.update_animation()
        DISPLAYSURF.blit(self.img,(self.x,self.y))
    def update_animation(self):
        self.time_now=pygame.time.get_ticks()
        Cooldown=50
        if self.time_now-self.time_init > Cooldown:
            self.frame+=1
            if self.frame>=8:
                self.frame=0
            self.img=self.animation_list[self.frame]
            self.time_init=self.time_now

    
left,right = False,False  
         
bg=Background(0,0,10)
player = Player(0,int(chieucaoy-actor_h),animation_)

# player = Player(0,int(chieucaoy-imgheight),imgwidth,imgheight)

# up,down,left,right = False,False,False,False

while True:
    for event in pygame.event.get(): #tra ve chuoi su kien
        if event.type == QUIT: 
            pygame.quit()
            sys.exit()
        # if event.type == KEYDOWN:
        #     if event.key == K_UP:
        #         up = True
        #     if event.key == K_DOWN:
        #         down = True
        #     if event.key == K_LEFT:
        #         left = True
        #     if event.key == K_RIGHT:
        #         right = True

    bg.draw()     
    bg.update()
    obj_group.draw(DISPLAYSURF)
    obj_group.update(bg)
    player.draw()
    
    # objs.draw()
    # objs.update(bg)

    # player.draw(bg)
    # player.move(bg,left,right)
    # bg.move(player)
    pygame.display.update() #hien ra man hinh
    #
    fpsclock.tick(FPS)





    #chyen dong
    # def move(self,player):
    #     if player.nv_rect.right > chieurongx - self.x:
    #         self.x -=player.speed
    #     if player.nv_rect.left < -self.x:
    #         self.x += player.speed

# class Player():
#     def __init__(self,x,y,width,height):
#         self.nv = pygame.transform.scale(nv,(width,height))
#         self.nv_rect = self.nv.get_rect(topleft=(x,y))
#         self.x=x
#         self.y=y
#         self.speed=10
#     def draw(self,bg):
#         DISPLAYSURF.blit(self.nv,(self.nv_rect.left + bg.x,self.nv_rect.top+bg.y) )
#     def move(self,bg,left,right):
#         if left:
#             self.nv_rect.centerx -=self.speed
#         if right:
#             self.nv_rect.centerx +=self.speed
#         if self.nv_rect.right > bg.pink.get_width():
#             self.nv_rect.right = bg.pink.get_width()
#         if self.nv_rect.left < 0:
#             self.nv_rect.left = 0