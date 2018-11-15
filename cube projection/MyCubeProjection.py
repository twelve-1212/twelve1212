# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 19:59:52 2018

@author: 施腾芮
"""

import numpy as np
from math import *

class point():
      def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z
            
def NomFunc(p):
      tmp = sqrt(p.x * p.x + p.y * p.y + p.z * p.z)
      p.x = p.x / tmp
      p.y = p.y / tmp
      p.z = p.z / tmp
      return p
      
def CrossFunc(a, b):
      cross = point(a.y*b.z - a.z*b.y, a.z*b.x - a.x*b.z, a.x*b.y - a.y*b.x)
      return cross

def MyLoookAt(eyex, eyey, eyez, centerx, centery, centerz, upx, upy, upz):
      matwtoc = [[0 for i in range(4)] for i in range(4)]
      forward = point(centerx - eyex, centery - eyey, centerz - eyez)
      up = point(upx, upy, upz)
      cross = CrossFunc(forward, up)
      forward = NomFunc(forward)
      cross = NomFunc(cross)
      up = CrossFunc(cross, forward)
      matwtoc[0][0] = cross.x
      matwtoc[1][0] = cross.y
      matwtoc[2][0] = cross.z
      matwtoc[0][1] = up.x
      matwtoc[1][1] = up.y
      matwtoc[2][1] = up.z
      matwtoc[0][2] = -forward.x
      matwtoc[1][2] = -forward.y
      matwtoc[2][2] = -forward.z
      matwtoc[3][3] = 1
      matwtoc = np.mat(matwtoc) #该矩阵*最终坐标 = 当前坐标
      lmat = matwtoc.I #取逆矩阵*当前坐标 = 最终坐标
      #print(lmat)
      return lmat

#为保证translation在未变换过的xyz轴上进行，需在lookat函数前进行translation
def MyTranslation(eyex,eyey,eyez):
      transmat = [[0 for i in range(4)] for i in range(4)]
      transmat[0][0] = 1
      transmat[1][1] = 1
      transmat[2][2] = 1
      transmat[3][3] = 1  
      transmat[0][3] = -eyex
      transmat[1][3] = -eyey
      transmat[2][3] = -eyez
      print(transmat)
      return transmat

#透视投影
def MyPerspective(fovy, aspect, zNear, zFar):
      pmat = [[0 for i in range(4)] for i in range(4)]
      pmat[0][0] = 1/(tan(fovy*pi/360)*aspect)
      pmat[1][1] = 1/tan(fovy*pi/360)
      pmat[2][2] = -(zFar + zNear)/(zFar - zNear)
      pmat[2][3] = -2*zFar*zNear/(zFar - zNear)
      pmat[3][2] = -1 
      #print(pmat)
      return pmat

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

cubepoint_list = [
        [1, 1, 1], 
        [1, -1, 1], 
        [-1, -1, 1], 
        [-1, 1, 1], 
        [1, 1, -1], 
        [1, -1, -1], 
        [-1, -1, -1], 
        [-1, 1, -1]
        ]

eyex = 2.0
eyey = 2.0
eyez = 5.0
cube = np.zeros((8,4))
cubepoint = np.array(cubepoint_list)
f_point = [[0 for i in range(2)] for i in range(8)]
for i in range(len(cubepoint_list)):
      cube[i] = np.append(cubepoint[i],1)
      aw = np.array([cube[i]]).T #列向量表示
      
      at = np.dot(MyTranslation(eyex,eyey,eyez), aw)
      ac = np.dot(MyLoookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0), at)
      ap = np.dot(MyPerspective(60.0, 1.0, 1.0, 20.0), ac)
      lap = ap.tolist()
      lan = [lap[0][0]/lap[3][0], lap[1][0]/lap[3][0], lap[2][0]/lap[3][0], 1]
      an = np.array([lan]).T
      apoint = np.dot(MyViewport(0, 0, 500, 500, 1.0, 20.0), an)
      pointlist = apoint.tolist()
      #print(pointlist)
      finalpoint = []
      for j in range(len(pointlist) - 2):
            finalpoint.append(pointlist[j][0])
      f_point[i] = finalpoint
      #print(finalpoint)
print(f_point)