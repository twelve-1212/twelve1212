# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 10:30:15 2018

@author: 施腾芮
"""

import cv2


img = cv2.imread('tube01_roi.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret1,th1 = cv2.threshold(gray,152,255,cv2.THRESH_BINARY)
ret2,th2 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("img1", th1)
cv2.imshow("img2", th2)
cv2.waitKey(0)
cv2.destroyAllWindows()