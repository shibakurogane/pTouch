import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2
pointsX=np.linspace(0,1,1000)
def sin_f(x):
  return np.sin(x)        

#CREATE LEAST SQUARES ANALYTICAL SOLUTION FUNCTION 

def Q3(rank,outputName):
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
  plt.plot(pointsX,pointsY,'blue')

  plt.axis('off')
  plt.savefig(outputName)
  plt.clf()
  return W,pointsY


