# -*- coding: utf-8 -*-
#!usr/bin/python
"""
Created on Wed Dec 19 23:44:21 2018

@author: fanzh
"""
import numpy as np

cubepoint = [0, 0, 0]
editvalue = 0.1

##待修改的矩阵
#mattlp70 = [
#        [ 6.98215883e-01, -6.88709938e-18, -2.20310837e-01, -1.43354567e+01],
#        [-1.17752353e-01,  1.24308655e+00, -3.73184381e-01, -1.93774098e+01],
#        [-3.17237026e-01, -3.31878735e-01, -1.00539735e+00,  3.51354354e+01],
#        [-2.87023976e-01, -3.00271237e-01, -9.09645217e-01,  3.36939654e+01]
#        ]
#
#mattlp71 = [
#        [-4.53165166e-01, -3.94847549e-17,  5.75050969e-01, -4.46914612e-01],
#        [ 3.52745069e-01,  1.22339498e+00,  2.77978451e-01, -1.41388043e+01],
#        [ 8.14928816e-01, -3.80890642e-01,  6.42199339e-01,  4.22042768e+01],
#        [ 7.37316548e-01, -3.44615343e-01,  5.81037497e-01,  4.00895837e+01]
#        ]
#with open("mat70.txt",'w+') as f1:
#      for i in range(len(mattlp70)):
#            for j in range(len(mattlp70[0])):
#                  f1.write(str(mattlp70[i][j])+' ')
#            f1.write('\n')
#with open("mat71.txt",'w+') as f2:
#      for i in range(len(mattlp71)):
#            for j in range(len(mattlp71[0])):
#                  f2.write(str(mattlp71[i][j])+' ')
#            f2.write('\n')


def readFile(path):               
      with open(path,'r') as f1:
            first_ele = True
            for data in f1.readlines():
                  data = data.strip(' \n')
                  nums = data.split(' ')
                  if first_ele:   
                        ### 将字符串转化为整型数据
                        nums = [float(num) for num in nums]
                        ### 加入到 matrix 中 。
                        matrix = np.array(nums)
                        first_ele = False
                  else:
                        nums = [float(num) for num in nums]
                        matrix = np.c_[matrix,nums]
            return matrix
def writeFile(mat,path):
    with open(path,'w+') as f1:
      for i in range(len(mat)):
            for j in range(len(mat[0])):
                  f1.write(str(mat[i][j])+' ')
            f1.write('\n')
                  
mattlp70 = readFile("mat70.txt")
mattlp71 = readFile("mat71.txt")
mattlp70[3][2] = mattlp70[3][2] + editvalue
writeFile(mattlp70,"mat70.txt")
writeFile(mattlp71,"mat71.txt")

            
#print(mattlp70edit)
##针对70的矩阵
#for i in range(4):
#      for j in range(4):
#            if j == 3:
#                  mattlp70edit[i][j] = mattlp70[i][j] + 1e-4
#            elif (j == 2 & i ==2)|(j == 1 & i == 1):
#                  mattlp70edit[i][j] = mattlp70[i][j] + random.uniform(-10e+0,10e+0)
#            elif i == 0 & j == 1:
#                  mattlp70edit[i][j] = mattlp70[i][j] + random.uniform(-10e-17,10e-17)
#            else:
#                  mattlp70edit[i][j] = mattlp70[i][j] + random.uniform(-10e-1,10e-1)
#      #      mattlp71edit[i][j] = mattlp71[i][j] + random.uniform(-10e-1,10e-1)

