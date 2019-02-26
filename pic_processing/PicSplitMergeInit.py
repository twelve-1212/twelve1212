# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 22:19:54 2018

@author: 施腾芮
"""
import cv2
import numpy as np

def Pic_Process(img):
      imgcopy = img.copy()
      gray = cv2.cvtColor(imgcopy, cv2.COLOR_BGR2GRAY)
      grayImage = cv2.medianBlur(gray, 5)
      ret, binary = cv2.threshold(grayImage, 80, 255, cv2.THRESH_BINARY)
      binary = cv2.Canny(binary, 100, 255)
      image, contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
      cv2.drawContours(img, contours, -1, (255, 0, 0), 2)
      #contours[0]为右边那条轮廓拟合右边的那条轮廓
      cnt = contours[0] 
      rows,cols = img.shape[:2]
      [vx,vy,x,y]=cv2.fitLine(cnt,cv2.DIST_L2,0,0.01,0.01)
      xa = x - (vx/vy) * y
      ya = 0
      xb = x + (vx/vy) * (rows - y)
      yb = rows
      img = cv2.line(img,(xa,ya),(xb,yb),(0,255,0),2)
      return img

def Split_Pic(img,n):
      names = locals()
      img_rows,img_cols = img.shape[:2]
      for i in range(n):
            names['img_split'+str(i)] = img[int(i*img_rows/n):int((i+1)*img_rows/n), 0:int(img_cols)]
            names['pic'+str(i)] = Pic_Process(names['img_split'+str(i)])
            cv2.imwrite('D:\\twelve1212\\Tube_pic\\merge'+'%d'%i+'.jpg', names['pic'+str(i)])
            cv2.imshow("img"+'%d'%i, names['pic'+str(i)])
            
def Merge_Pic(n):
      names = locals()
      imgfinal = cv2.imread('D:\\twelve1212\\Tube_pic\\merge0.jpg')
      for i in range(1,n):
            names['img_split'+str(i)] = cv2.imread('D:\\twelve1212\\Tube_pic\\merge'+'%d'%i+'.jpg')
            imgfinal = np.concatenate((imgfinal, names['img_split'+str(i)]))
      cv2.imshow("imgfinal", imgfinal)

if __name__ == '__main__':
      img = cv2.imread('D:\\twelve1212\\Tube_pic\\camera70_tube01_roi01.jpg')
      Split_Pic(img,8)      
      Merge_Pic(8)
      cv2.waitKey(0)
      cv2.destroyAllWindows()