# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 19:25:39 2018

@author: 施腾芮
"""

import cv2
img=cv2.imread("D:\\twelve1212\\Test_pic\\img11.jpg") # 定片位置
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # 转化为灰度图
# 图片的缩放
#size=img.shape
#img=cv2.resize(img,(size[1]//2,size[0]//2),cv2.INTER_LINEAR)


def onmouse(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,y)


def main():
    cv2.namedWindow("img",cv2.WINDOW_NORMAL)  # 构建窗口
    cv2.setMouseCallback("img",onmouse,0) # 回调绑定窗口
    cv2.imshow("img",img) # 显示图像
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__=="__main__":
    main()
