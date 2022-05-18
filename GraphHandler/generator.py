import numpy as np
import matplotlib.pyplot as plt
import pygame

pointsX=np.linspace(0,1,1000)
#CREATE LEAST SQUARES ANALYTICAL SOLUTION FUNCTION 
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
    for i in range(RANK):
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
def CreateGraph(rank,outputName):
  #CREATE MATRIX WITH RANK-ORDER
  X=np.random.rand(100,1)
  Y=np.random.rand(100,1)
  ADup=np.zeros_like(X)
  RANK=rank+1
  A=np.zeros_like(X)
  for r in range(RANK):
    for i in range(len(X)):
      ADup[i]=X[i]**r
    A=np.concatenate((A,ADup),axis=1)
  A=np.delete(A,0,axis=1)
  # print(A)
  #CALCULATOR COEF WITH FORMULA
  Z1=np.matmul(A.T,A)             #A.T*A
  Z2=np.linalg.inv(Z1)            #(A.T*A)^-1
  Z3=np.matmul(A.T,Y)             #A.T*Y
  W=np.matmul(Z2,Z3)              #((A.T*A)^-1)*A.T*Y
  print(W)
  pointsY=0

  
  #Y init from 1000 equidistant X point using training coefficient      
  for i in range(RANK):
    pointsY+=W[i][0]*pointsX**i
  #DRAWING
  plt.plot(pointsX,pointsY,'black',linewidth=20)

  plt.axis('off')
  plt.savefig(outputName)
  plt.clf()
  return W,pointsY


class Graph():
  def __init__(self,outputName):
      self.outputName=outputName
      self.pointsX=np.linspace(0,1,1000)
  def CreateGraph(self,rank):
  #CREATE MATRIX WITH RANK-ORDER
    X=np.random.rand(100,1)
    Y=np.random.rand(100,1)
    ADup=np.zeros_like(X)
    RANK=rank+1
    self.RANK=RANK
    A=np.zeros_like(X)
    for r in range(RANK):
      for i in range(len(X)):
        ADup[i]=X[i]**r
      A=np.concatenate((A,ADup),axis=1)
    A=np.delete(A,0,axis=1)
  # print(A)
  #CALCULATOR COEF WITH FORMULA
    Z1=np.matmul(A.T,A)             #A.T*A
    Z2=np.linalg.inv(Z1)            #(A.T*A)^-1
    Z3=np.matmul(A.T,Y)             #A.T*Y
    W=np.matmul(Z2,Z3)              #((A.T*A)^-1)*A.T*Y
    print(W)
    pointsY=0

  
  #Y init from 1000 equidistant X point using training coefficient      
    for i in range(RANK):
      pointsY+=W[i][0]*pointsX**i
  #DRAWING
    plt.plot(pointsX,pointsY,'black',linewidth=20)

    plt.axis('off')
    plt.savefig(self.outputName)
    plt.clf()
    self.W=W
    self.pointsY=pointsY
    return W,pointsY

  def Proccess(self,line):
    npAr=np.array(line)
    print('shape:',npAr.shape)
    afx=normalization(npAr[:,0])
    afy=normalization(npAr[:,1])

    Ycenter=self.pointsY[500]
    pointsX=np.linspace(0,1,1000)

    poiX=afx
    poiY=np.array([y*-1 for y in afy])

    print('loss before scale',loss(poiX,poiY,min(self.pointsY),max(self.pointsY),self.RANK,self.W))


    poiY=fitScaleY(poiY,max(self.pointsY),min(self.pointsY))

    print('loss after scale',loss(poiX,poiY,min(self.pointsY),max(self.pointsY),self.RANK,self.W))


    centerDistanceY=Ycenter-poiY[len(poiY)//2]
    print('distance before fit center',centerDistanceY)
    poiY=fitCenterY(poiY,centerDistanceY) #fit center
    centerDistanceY=Ycenter-poiY[len(poiY)//2]
    print('distance after fit center',centerDistanceY)
    print('loss after fit center',loss(poiX,poiY,min(self.pointsY),max(self.pointsY),self.RANK,self.W))
    print('limit',min(self.pointsY),max(self.pointsY))
    if(loss(poiX,poiY,min(self.pointsY),max(self.pointsY),self.RANK,self.W)<0.1):
        print('Correct')
        return True
    else:
        print('wrong')
        return False


