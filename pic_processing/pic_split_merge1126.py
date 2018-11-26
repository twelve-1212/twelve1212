# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 22:19:54 2018

@author: 施腾芮
"""

import cv2


def Split_Img(img):
      img_rows,img_cols = img.shape[:2]
      img_split1 = img[0:int(img_rows/2), 0:int(img_cols)]
      img_split2 = img[int(img_rows/2):int(img_rows), 0:int(img_cols)]
      for img in img_split1,img_split2:
            


cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)
img = cv2.imread('D:\\twelve1212\\Tube_pic\\camera71_tube01_roi01.jpg')
img_rows,img_cols = img.shape[:2]
print(img_rows)
print(img_cols)
img_split1 = img[0:int(img_rows/2), 0:int(img_cols)]   #对像素取整 可能会丢失一些像素
img_split2 = img[int(img_rows/2):int(img_rows), 0:int(img_cols)]
imgcopy = img_split1.copy()
gray = cv2.cvtColor(imgcopy, cv2.COLOR_BGR2GRAY)
grayImage = cv2.medianBlur(gray, 5)

ret, binary = cv2.threshold(grayImage, 100, 255, cv2.THRESH_BINARY)
cv2.imshow('threshold',binary)
binary = cv2.Canny(binary, 100, 255)

image, contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

print(len(contours))
cv2.drawContours(img_split1, contours, -1, (255, 0, 0), 2)

cnt = contours[0]
rows,cols = img_split1.shape[:2]
[vx,vy,x,y]=cv2.fitLine(cnt,cv2.DIST_L2,0,0.01,0.01)
print(vx,vy,x,y)

xa = x - (vx/vy) * y
ya = 0
xb = x + (vx/vy) * (rows - y)
yb = rows
img_split1 = cv2.line(img_split1,(xa,ya),(xb,yb),(0,255,0),2)

cv2.imshow("img", img_split1)
cv2.waitKey(0)
cv2.destroyAllWindows()