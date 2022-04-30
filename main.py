import pygame
from GraphHandler import generator,imagePredict
import numpy as np
import matplotlib.pyplot as plt
import cv2
pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)

FPS = 1000

WIDTH, HEIGHT = 1000, 700
screen=pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("game")
ROWS = COLS = 100

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = WHITE

DRAW_GRID_LINES = True


def get_font(size):
    return pygame.font.SysFont("comicsans", size)
def get_pixel_data(surf, top_left, bottom_right):
    w = bottom_right[0] - top_left[0]
    h = bottom_right[1] - top_left[1]
    sub_surface = surf.subsurface(pygame.Rect(*top_left, w, h))
    return sub_surface

clock = pygame.time.Clock()

RANK=5
W,Ycenter,yDraw=generator.Q3(RANK)
minY=min(yDraw)
maxY=max(yDraw)
# pointsX=np.linspace(0,100,1000)
# for i in range(len(yDraw)):
#     yDraw[i]=yDraw[i]-minY
print(yDraw)
run=True
line=[]
graphD=pygame.image.load('foo.png').convert()

while run:
    clock.tick(FPS)
    screen.fill(BG_COLOR)
    pygame.draw.line(screen,BLACK,(700,0),(700,700))
    pygame.draw.line(screen,BLACK,(700,400),(1000,400))
    screen.blit(graphD,(0,0))
    for i in range(len(line)):
        pygame.draw.circle(screen,BLACK,(line[i][0],line[i][1]),2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pygame.mouse.get_pressed()[0]:
            positionX,positionY=pygame.mouse.get_pos()
            line.append((pygame.mouse.get_pos()))
        if event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_k:
                pxarray = get_pixel_data(screen,[701,401],[1000,700])
                # print(pxarray.shape)
                # plt.imsave('image.png',pxarray)
                pygame.image.save(pxarray,'input.png')
            if event.key==pygame.K_p:
                imagePredict.Proccess(W,Ycenter,yDraw,RANK)
    # for i in range(len(yDraw)):
    #     pygame.draw.circle(screen,BLACK,(pointsX[i],yDraw[i]*10),2)
    pygame.display.update()
pygame.quit(1)
