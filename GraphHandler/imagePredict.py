import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2
import pygame
from sklearn.preprocessing import StandardScaler
def leftBorderDetect(img):
  for x in range(img.shape[1]):
    border=False
    for y in range(img.shape[0]):
      if(img[y][x]!=255):
        border=True
    if(border==True):
      return x
def rightBorderDetect(img):
  for x in range(img.shape[1]):
    rightBorder=img.shape[1]-1-x
    border=False
    for y in range(img.shape[0]):
      if(img[y][rightBorder]!=255):
        border=True
    if(border==True):
      return rightBorder
def topBorderDetect(img):
  for y in range(img.shape[0]):
    border=False
    for x in range(img.shape[1]):
      if(img[y][x]!=255):
        border=True
    if(border==True):
      return y
def bottomBorderDetect(img):
  for y in range(img.shape[0]):
    bottomBorder=img.shape[0]-1-y
    border=False
    for x in range(img.shape[1]):
      if(img[bottomBorder][x]!=255):
        border=True
    if(border==True):
      return bottomBorder

def convertPoints(img):
  pX=[]
  pY=[]
  for x in range(img.shape[1]):
    exist=False
    for y in range(img.shape[0]):
      if(img[y][x]!=255 and exist==False):
        # print(x,y)
        pX.append(x/img.shape[1])
        pY.append((img.shape[0]-1-y)/img.shape[1])
        exist=True

  return pX,pY

def normalization(arr):
  minArr=min(arr)
  scler=max(arr)-min(arr)
  afr=[0]*len(arr)
  for i in range(len(arr)):
    afr[i]=(arr[i]-minArr)/scler
  return afr
def fitCenterY(pY,distance):
  cY=[0]*len(pY)
  for i in range(len(pY)):
    cY[i]=pY[i]+distance
  return cY

def fitScaleY(pY,TOP,BOTTOM):
  cY=[0]*len(pY)
  scaleRange=TOP-BOTTOM
  yRange=max(pY)-min(pY)
  for i in range(len(pY)):
    cY[i]=pY[i]*(scaleRange/yRange)
  return cY
def loss(pX,pY,yBottom,yTop,RANK,W):
  expY=[0]*len(pY)
  LOSS=0
  for j in range(len(pY)):
    for i in range(RANK+1):
      expY[j] += W[i][0] * pX[j]**i
    
    LOSS+=(( pY[j] - expY[j] )**2)/(yTop-yBottom)**2
  # plt.plot(pX,expY)
  # plt.show()
  return LOSS/len(pX)
def get_pixel_data(surf, top_left, bottom_right):
    w = bottom_right[0] - top_left[0]
    h = bottom_right[1] - top_left[1]
    sub_surface = surf.subsurface(pygame.Rect(*top_left, w, h))
    return sub_surface

def Proccess(W,yDraw,RANK,line):
    npAr=np.array(line)
    print('shape:',npAr.shape)
    afx=normalization(npAr[:,0])
    afy=normalization(npAr[:,1])

    # scaler = StandardScaler()
    # scaler.fit(npAr)
    # print(scaler.transform(npAr))



    Ycenter=yDraw[500]
    pointsX=np.linspace(0,1,1000)
    # img=cv2.imread('input.png',0)
    # # cv2.imshow('input',img)
    # print('Input drawing',img)
    # left=leftBorderDetect(img)
    # right=rightBorderDetect(img)
    # top=topBorderDetect(img)
    # bottom=bottomBorderDetect(img)
    # cropped_image = img[ top:bottom,left:right]
    # # cv2.imshow('cropped',cropped_image)
    # plt.imsave('cropped.png',cropped_image)
    # poiX,poiY=convertPoints(cropped_image)
    poiX=afx
    poiY=np.array([y*-1 for y in afy])
    # plt.plot(poiX,poiY)
    # plt.show()
    # print('Get egde')

    # print(cropped_image)
    # plt.plot(poiX,poiY)
    # plt.plot(pointsX,yDraw,'blue')
    # plt.show()
    print('loss before scale',loss(poiX,poiY,min(yDraw),max(yDraw),RANK,W))


    poiY=fitScaleY(poiY,max(yDraw),min(yDraw))
    # plt.plot(poiX,poiY)
    # plt.plot(pointsX,yDraw,'blue')
    # plt.show()
    print('loss after scale',loss(poiX,poiY,min(yDraw),max(yDraw),RANK,W))


    centerDistanceY=Ycenter-poiY[len(poiY)//2]
    print('distance before fit center',centerDistanceY)
    poiY=fitCenterY(poiY,centerDistanceY) #fit center
    centerDistanceY=Ycenter-poiY[len(poiY)//2]
    # plt.plot(poiX,poiY,'red')
    # plt.plot(pointsX,yDraw,'blue')
    # plt.show()
    print('distance after fit center',centerDistanceY)
    print('loss after fit center',loss(poiX,poiY,min(yDraw),max(yDraw),RANK,W))
    print('limit',min(yDraw),max(yDraw))
    if(loss(poiX,poiY,min(yDraw),max(yDraw),RANK,W)<0.1):
        print('Correct')
        return True
    else:
        print('wrong')
        return False



