# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 16:05:52 2018

@author: 施腾芮
"""
import numpy as np
import cv2

img_i = cv2.imread('aa.jpg')
cv2.imshow('init_image',img_i)
img_gray = cv2.cvtColor(img_i,cv2.COLOR_BGR2GRAY)
img_32i = np.float32(img_gray)
img_cor = cv2.cornerHarris(img_32i,2,3,0.04)
img_cor = cv2.dilate(img_cor,None)  #扩大标记
img_i[img_cor>0.01*img_cor.max()]=[0,0,255]
cv2.imshow('dst',img_i)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()