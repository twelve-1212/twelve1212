# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 19:39:34 2018

@author: 施腾芮
"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
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
      mat = [[0 for i in range(4)] for i in range(4)]
      forward = point(centerx - eyex, centery - eyey, centerz - eyez)
      up = point(upx, upy, upz)
      cross = CrossFunc(forward, up)
      forward = NomFunc(forward)
      cross = NomFunc(cross)
      up = CrossFunc(cross, forward)
      mat[0][0] = cross.x
      mat[1][0] = cross.y
      mat[2][0] = cross.z
      mat[0][1] = up.x
      mat[1][1] = up.y
      mat[2][1] = up.z
      mat[0][2] = -forward.x
      mat[1][2] = -forward.y
      mat[2][2] = -forward.z
      mat[3][3] = 1
      glLoadMatrixd(mat)
      glTranslated(-eyex, -eyey, -eyez)

def MyPerspective(fovy, aspect, zNear, zFar):
      pmat = [[0 for i in range(4)] for i in range(4)]
      pmat[0][0] = 1/(tan(fovy*pi/360)*aspect)
      pmat[1][1] = 1/tan(fovy*pi/360)
      pmat[2][2] = -(zFar + zNear)/(zFar - zNear)
      pmat[2][3] = -2*zFar*zNear/(zFar - zNear)
      pmat[3][2] = -1 
      glLoadMatrixd(pmat)

def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #gluPerspective(60.0, 1.0, 1.0, 20.0)
    MyPerspective(60.0, 1.0, 1.0, 20.0)
    
    glMatrixMode(GL_MODELVIEW) 
    glLoadIdentity() 
    #gluLookAt(2.0, 2.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    MyLoookAt(5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    
    glColor3f(1.0, 1.0, 1.0)
    glutWireCube(1)
    glFlush()


# 初始化
glutInit()
glutInitDisplayMode(GLUT_RGB)
# 窗口
glutInitWindowPosition(200, 200)
glutInitWindowSize(500, 500)
glutCreateWindow("Cube Projection")
#绘制图像
glutDisplayFunc(drawFunc)
glutMainLoop()