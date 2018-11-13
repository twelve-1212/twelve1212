# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 16:46:20 2018

@author: 施腾芮
"""

import cv2

def nothing(x):
    pass

img = cv2.imread('tube01_roi.jpg')
imgcopy = img.copy()
gray = cv2.cvtColor(imgcopy, cv2.COLOR_BGR2GRAY)
grayImage = cv2.medianBlur(gray, 5)
ret, binary = cv2.threshold(grayImage, 150, 255, cv2.THRESH_BINARY)

cv2.namedWindow('res')
cv2.createTrackbar('min','res',0,25,nothing)
cv2.createTrackbar('max','res',0,25,nothing)
while(1):
    if cv2.waitKey(1)&0xFF==27:
        break
    maxVal=cv2.getTrackbarPos('max','res')
    minVal=cv2.getTrackbarPos('min','res')
    canny=cv2.Canny(binary,10*minVal,10*maxVal)
    cv2.imshow('res',canny)

#cv2.imshow('canny', grayImage)
image, contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#cv2.imshow("image", image)
cv2.drawContours(imgcopy, contours, -1, (255, 0, 0), 2)

#cv2.imshow("res", imgcopy)
cv2.waitKey(0)
cv2.destroyAllWindows()