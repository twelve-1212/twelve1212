# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 22:09:53 2018

@author: 施腾芮
"""

import cv2

def Split_Pic(img):
      imgcopy = img.copy()
      gray = cv2.cvtColor(imgcopy, cv2.COLOR_BGR2GRAY)
      grayImage = cv2.medianBlur(gray, 5)
      ret, binary = cv2.threshold(grayImage, 100, 255, cv2.THRESH_BINARY)
      #cv2.imshow('threshold',binary)
      binary = cv2.Canny(binary, 100, 255)
      image, contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
      #print(len(contours))
      cv2.drawContours(img, contours, -1, (255, 0, 0), 2)
      cnt = contours[0] #在拟合右边的那条轮廓
      rows,cols = img.shape[:2]
      [vx,vy,x,y]=cv2.fitLine(cnt,cv2.DIST_L2,0,0.01,0.01)
      #print(vx,vy,x,y)
      xa = x - (vx/vy) * y
      ya = 0
      xb = x + (vx/vy) * (rows - y)
      yb = rows
      img = cv2.line(img,(xa,ya),(xb,yb),(0,255,0),2)
      return img

#cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)
img = cv2.imread('D:\\twelve1212\\Tube_pic\\camera71_tube01_roi01.jpg')
img_rows,img_cols = img.shape[:2]
print(img_rows)
print(img_cols)
img_split1 = img[0:int(img_rows/4), 0:int(img_cols)]   #对像素取整 可能会丢失一些像素
img_split2 = img[int(img_rows/4):int(img_rows/2), 0:int(img_cols)]
img_split3 = img[int(img_rows/2):int(3*img_rows/4), 0:int(img_cols)]
img_split4 = img[int(3*img_rows/4):int(img_rows), 0:int(img_cols)]
img_split = [img_split1,img_split2,img_split3,img_split4]
i = 97
for img in img_split:
      cv2.namedWindow('img'+chr(i), cv2.WINDOW_AUTOSIZE)
      pic = Split_Pic(img)
      cv2.imshow("img"+chr(i), pic)
      i = i + 1
      

      

#cv2.imshow("img", img_split1)

cv2.waitKey(0)
cv2.destroyAllWindows()