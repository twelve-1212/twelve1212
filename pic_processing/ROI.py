# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 20:31:13 2018

@author: 施腾芮
"""

import cv2

if __name__ == '__main__' :

    # Read image
    im = cv2.imread("D:\\twelve1212\\Tube_pic\\camera70_tube01.jpg",0)

    # Select ROI
    fromCenter = False
    r = cv2.selectROI("image", im, fromCenter)

    # Crop image 裁剪图片
    imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    
    #保存图片
    cv2.imwrite('D:\\twelve1212\\Tube_pic\\camera70_tube01_roi01.jpg', imCrop)
    # Display cropped image
    cv2.imshow("Image", imCrop)
    cv2.waitKey(0)
    cv2.destroyAllWindows()