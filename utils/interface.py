import pygame
from .tools import *
class Enemy(pygame.sprite.Sprite):
    '''
    class tượng trưng cho kẻ thù 
    Kẻ thù sẽ rơi từ trên xuống với tốc độ tăng dần và ngẫu nhiên
    Nếu chạm trúng người chơi, trò chơi sẽ kết thúc
    '''
    def __init__(self,obj):
        super().__init__() 
        self.image = obj
        self.surf = pygame.Surface((OBJWIDTH ,OBJHEIGHT))
        self.rect = self.surf.get_rect(center = (random.randint(OBJWIDTH,SCREEN_WIDTH-OBJWIDTH), 0))
        self.alive=True
        

    def move(self):
            global LIFE
            self.rect.move_ip(0,SPEED)
            if (self.rect.bottom >= (SCREEN_HEIGHT-75)):
                
                self.rect.top = 0
                self.rect.center = (random.randint(OBJWIDTH//2,SCREEN_WIDTH-OBJWIDTH//2), 0)
                return True
            return False            
                
            
 
class Player(pygame.sprite.Sprite):
    '''
    Class người chơi
    Người chơi được phép di chuyển trái phải cới tốc độ dược đặt trước
    '''
    def __init__(self,nv):
        super().__init__() 
        self.image = nv
        self.surf = pygame.Surface((NVWIDTH,NVHEIGHT))
        self.rect = self.surf.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT-100))
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
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
    '''
    Class background
    Vẽ nền 
    Tạo background chạy dọc
    '''
    def __init__(self,BG):
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
             
    def draw(self,DISPLAYSURF,METALFLOOR,FRAME):
        DISPLAYSURF.blit(self.bgimage, (self.bgX1, self.bgY1))
        DISPLAYSURF.blit(self.bgimage, (self.bgX2, self.bgY2))
        DISPLAYSURF.blit(METALFLOOR,(0,SCREEN_HEIGHT-150))
        DISPLAYSURF.blit(METALFLOOR,(150,SCREEN_HEIGHT-150))
        DISPLAYSURF.blit(METALFLOOR,(300,SCREEN_HEIGHT-150)) 
        DISPLAYSURF.blit(METALFLOOR,(450,SCREEN_HEIGHT-150))
        DISPLAYSURF.blit(FRAME,(245,0))