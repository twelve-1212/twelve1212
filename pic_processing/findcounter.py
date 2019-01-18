# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 20:48:42 2018

@author: 施腾芮
"""

import cv2
import numpy as np

maxcnt = []
maxcnt2 = []
#cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)
img = cv2.imread('D:\\twelve1212\\Tube_pic\\camera70_tube01.jpg')
imgcopy = img.copy()
gray = cv2.cvtColor(imgcopy, cv2.COLOR_BGR2GRAY)
mask = np.zeros(gray.shape, dtype=np.uint8)
grayImage = cv2.medianBlur(gray, 5) #中值滤波
ret, binary = cv2.threshold(grayImage, 70, 200, cv2.THRESH_BINARY) #二值化 修改这个来改变轮廓条数
binary = cv2.Canny(binary, 100, 255)
image, contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
#寻找最大的两个轮廓 确定合适的阈值保证maxcnt里面是两条最大的轮廓
print(len(contours))
for i in range(len(contours)):
    perimeter = cv2.arcLength(contours[i], True)
    if perimeter > 1500:
        maxcnt.append(i)

#for i in range(len(maxcnt)):
#    cv2.drawContours(img, contours, maxcnt[i], (255, 0, 0), 2)
cnt0 = contours[maxcnt[0]]    
cnt1 = contours[maxcnt[1]] 
cnt2 = np.concatenate((cnt0, cnt1),axis = 0)  #将两个轮廓数据拼接
hull = cv2.convexHull(cnt2)
cv2.polylines(gray, [hull], True, (255, 255, 255), 3)
cv2.fillPoly(mask, [hull], (255, 255, 255)) #外黑里白
mask = cv2.bitwise_not(mask) #外白里黑
#cv2.imshow("mask", mask)
kernel = np.ones((9,9), np.uint8)
dilation = cv2.dilate(mask, kernel)
#masked_image = cv2.bitwise_and(gray, erosion)
masked_image = cv2.bitwise_or(gray, dilation)

ret, maskbinary = cv2.threshold(masked_image, 42, 255, cv2.THRESH_BINARY)
cv2.imshow("maskbinary", maskbinary)
image2, contours2, hierarchy2 = cv2.findContours(maskbinary, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) 
#print(len(contours2))
for i in range(len(contours2)):
    conlength = cv2.arcLength(contours2[i], True)
    if conlength < 2000 and conlength > 1000: #最外围的轮廓大于2000 中间管线轮廓为1000-2000中间 需要测算
        maxcnt2.append(i)
print(len(maxcnt2))
cv2.drawContours(img, contours2, maxcnt2[0], (255, 0, 0), 1)
#cv2.drawContours(img, contours2, -1, (255, 0, 0), 1)


#cnt = contours2[maxcnt2[0]] 
#rows,cols = img.shape[:2]
#[vx,vy,x,y]=cv2.fitLine(cnt,cv2.DIST_L2,0,0.01,0.01)
#xa = x - (vx/vy) * y
#ya = 0
#xb = x + (vx/vy) * (rows - y)
#yb = rows
#img = cv2.line(img,(xa,ya),(xb,yb),(0,255,0),2)

#cv2.imshow("img", gray)
#cv2.imshow("mask", mask)
#cv2.imshow("erosion", erosion)
#cv2.imshow("maskgray", masked_image)

cv2.imshow("finalimage", img)
cv2.waitKey(0)
cv2.destroyAllWindows()