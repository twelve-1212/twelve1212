# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 22:09:53 2018

@author: 施腾芮
"""

import cv2

#cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)
img = cv2.imread('D:\\twelve1212\\Tube_pic\\camera71_tube01_roi01.jpg')
img_rows,img_cols = img.shape[:2]
print(img_rows)
print(img_cols)
img_split1 = img[0:int(img_rows/2), 0:int(img_cols)]   #对像素取整 可能会丢失一些像素
img_split2 = img[int(img_rows/2):int(img_rows), 0:int(img_cols)]
i = 97
for img in img_split1,img_split2:
      cv2.namedWindow('img'+chr(i), cv2.WINDOW_AUTOSIZE)
      cv2.imshow("img"+chr(i), img)
      i = i + 1
      
      

#cv2.imshow("img", img_split1)

cv2.waitKey(0)
cv2.destroyAllWindows()