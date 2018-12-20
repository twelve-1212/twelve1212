# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 16:45:19 2018

@author: fanzh
"""

import numpy as np
from math import *

class point():
      def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z
            
def MyViewport(sx,sy,ws,hs,zNear,zFar):
      viewmat = [[0 for i in range(4)] for i in range(4)]
      viewmat[0][0] = ws/2
      viewmat[0][3] = sx + (ws/2)
      viewmat[1][1] = hs/2
      viewmat[1][3] = sy + hs/2
      viewmat[2][2] = (zFar - zNear)/2
      viewmat[2][3] = (zNear + zFar)/2
      viewmat[3][3] = 1
      #print(viewmat)
      return viewmat
  
#世界坐标系的坐标
cubepoint = [0, 0, 0]

mattlp70 = [
        [ 6.98215883e-01, -6.88709938e-18, -2.20310837e-01, -1.43354567e+01],
        [-1.17752353e-01,  1.24308655e+00, -3.73184381e-01, -1.93774098e+01],
        [-3.17237026e-01, -3.31878735e-01, -1.00539735e+00,  3.51354354e+01],
        [-2.87023976e-01, -3.00271237e-01, -9.09645217e-01,  3.36939654e+01]
        ]

mattlp71 = [
        [-4.53165166e-01, -3.94847549e-17,  5.75050969e-01, -4.46914612e-01],
        [ 3.52745069e-01,  1.22339498e+00,  2.77978451e-01, -1.41388043e+01],
        [ 8.14928816e-01, -3.80890642e-01,  6.42199339e-01,  4.22042768e+01],
        [ 7.37316548e-01, -3.44615343e-01,  5.81037497e-01,  4.00895837e+01]
        ]
#camera70_eye:(27, 24.3, 20.5)
#camera71_eye:(-27,24,-20.5)

cubepoint = np.append(cubepoint,1) #最后加1 使得列向量为四维 可以和4*4矩阵相乘
for imat in mattlp70, mattlp71:
    aw = np.array([cubepoint]).T #列向量表示
    ap = np.dot(imat, aw)
#      mat1 = np.dot(MyLoookAt(eyex, eyey, eyez, centerx, centery, centerz, 0.0, 1.0, 0.0), MyTranslation(eyex,eyey,eyez))
#      mattlp = np.dot(MyPerspective(75.0, 1.78, 1.0, 20.0), mat1)
#      print(mattlp)
#      amattlp = np.dot(mattlp, aw)
#      print(ap)
#      print(amattlp)
    lap = ap.tolist()
    lan = [lap[0][0]/lap[3][0], lap[1][0]/lap[3][0], lap[2][0]/lap[3][0], 1]
    an = np.array([lan]).T
    apoint = np.dot(MyViewport(0, 0, 1280, 720, 1.0, 20.0), an)
    pointlist = apoint.tolist()
    print(pointlist[:2])