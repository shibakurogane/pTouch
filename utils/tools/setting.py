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

from GraphHandler import generator,imagePredict

from button import Button


FPS = 144
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


OBJHEIGHT=200
OBJWIDTH=150
 
NVHEIGHT=50
NVWIDTH=50

