# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 22:19:54 2018

@author: 施腾芮
"""
import cv2
import numpy as np


def FindHull(img):
    maxcnt = []
    imgcopy = img.copy()
    gray = cv2.cvtColor(imgcopy, cv2.COLOR_BGR2GRAY)
    grayImage = cv2.medianBlur(gray, 5) #中值滤波
    ret, binary = cv2.threshold(grayImage, 70, 200, cv2.THRESH_BINARY) #二值化 修改这个来改变轮廓条数
    binary = cv2.Canny(binary, 100, 255)
    image, contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
    #寻找最大的两个轮廓 确定合适的阈值保证maxcnt里面是两条最大的轮廓
    for i in range(len(contours)):
        perimeter = cv2.arcLength(contours[i], True)
        if perimeter > 1500:
            maxcnt.append(i)
    cnt0 = contours[maxcnt[0]]    
    cnt1 = contours[maxcnt[1]] 
    cnt2 = np.concatenate((cnt0, cnt1),axis = 0)  #将两个轮廓数据拼接
    hull = cv2.convexHull(cnt2)
    return hull

def FindContour(img,hull):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mask = np.zeros(gray.shape, dtype=np.uint8)
    cv2.polylines(gray, [hull], True, (255, 255, 255), 3)
    cv2.fillPoly(mask, [hull], (255, 255, 255)) #外黑里白
    mask = cv2.bitwise_not(mask) #外白里黑
    kernel = np.ones((9,9), np.uint8)
    dilation = cv2.dilate(mask, kernel)
    masked_image = cv2.bitwise_or(gray, dilation)
    ret, maskbinary = cv2.threshold(masked_image, 41, 255, cv2.THRESH_BINARY) #调整该阈值 确定弯管轮廓
    cv2.imshow("maskbinary", maskbinary)
    image2, contours2, hierarchy2 = cv2.findContours(maskbinary, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) 
    maxcnt2 = []
    for i in range(len(contours2)):
        conlength = cv2.arcLength(contours2[i], True)
        if conlength < 2000 and conlength > 1000: #最外围的轮廓大于2000 中间管线轮廓为1000-2000中间 需要测算
            maxcnt2.append(i)
            cv2.drawContours(img, contours2, maxcnt2[0], (255, 0, 0), 1)
    cv2.imshow("finalimage", img)
    return maxcnt2[0]

def Pic_Process(img, cnt):
      #contours[0]为右边那条轮廓拟合右边的那条轮廓
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
        names['pic'+str(i)] = Pic_Process(names['img_split'+str(i)], FindContour(img, FindHull(img)))
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
    img = cv2.imread('D:\\twelve1212\\Tube_pic\\camera70_tube01.jpg')
    Split_Pic(img,1)      
    Merge_Pic(1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()