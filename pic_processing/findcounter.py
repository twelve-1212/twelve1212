# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 20:48:42 2018

@author: 施腾芮
"""

import cv2

#cv2.namedWindow('tube', 0)
#cv2.namedWindow('threshold', cv2.WINDOW_NORMAL)
#cv2.namedWindow('canny', cv2.WINDOW_NORMAL)
#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)
img = cv2.imread('D:\\twelve1212\\Tube_pic\\camera71_tube01_roi01.jpg')
#cv2.imshow('tube',img)
imgcopy = img.copy()
gray = cv2.cvtColor(imgcopy, cv2.COLOR_BGR2GRAY)
#ret, binary = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
#image, contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(image,contours,-1,(0,0,255),3)
grayImage = cv2.medianBlur(gray, 5)
#grayImage = cv2.blur(gray, (5, 5))
#grayImage = cv2.GaussianBlur(gray, (5,5), 1)
ret, binary = cv2.threshold(grayImage, 100, 255, cv2.THRESH_BINARY)
cv2.imshow('threshold',binary)
binary = cv2.Canny(binary, 100, 255)
#cv2.imshow('canny', grayImage)
image, contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#cv2.imshow("image", image)
print(len(contours))
cv2.drawContours(img, contours, -1, (255, 0, 0), 2)

cnt = contours[0]
rows,cols = img.shape[:2]
[vx,vy,x,y]=cv2.fitLine(cnt,cv2.DIST_L2,0,0.01,0.01)
print(vx,vy,x,y)
#lefty=int((x*vy/vx)+y)
#righty=int(((cols-x)*vy/vx)+y)
#img = cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)
#img = cv2.line(img,(vx,x),(vy,y),(0,255,0),2)
xa = x - (vx/vy) * y
ya = 0
xb = x + (vx/vy) * (rows - y)
yb = rows
img = cv2.line(img,(xa,ya),(xb,yb),(0,255,0),2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()