# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:40:45 2018

@author: 施腾芮
"""

import numpy as np

point3D = np.array([[0,0,0,1]]).T
viewmat = [[0 for i in range(4)] for i in range(3)]
viewmat[0][0] = 1
viewmat[0][1] = 1
viewmat[0][2] = 1
viewmat[0][3] = 1
viewmat[1][0] = 1
viewmat[1][1] = 1
viewmat[1][2] = 1
viewmat[1][3] = 1
viewmat[2][0] = 1
viewmat[2][1] = 1
viewmat[2][2] = 1
viewmat[2][3] = 1
print(viewmat)
point2D = np.dot(viewmat,point3D)
print(point2D)