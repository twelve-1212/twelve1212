# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 20:48:42 2018

@author: 施腾芮
"""

import cv2
 
img = cv2.imread('tube01_roi.jpg')
imgcopy = img.copy()
gray = cv2.cvtColor(imgcopy, cv2.COLOR_BGR2GRAY)
#ret, binary = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
 
#image, contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(image,contours,-1,(0,0,255),3)

grayImage = cv2.medianBlur(gray, 5)
#grayImage = cv2.blur(gray, (5, 5))
#grayImage = cv2.GaussianBlur(gray, (5,5), 1)
ret, binary = cv2.threshold(grayImage, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('threshold',binary)
binary = cv2.Canny(binary, 100, 255)
cv2.imshow('canny', grayImage)
image, contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.imshow("image", image)
print(len(contours))
cv2.drawContours(img, contours, 18, (255, 0, 0), 2) 
cv2.drawContours(img, contours, 22, (255, 0, 0), 2) 

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()