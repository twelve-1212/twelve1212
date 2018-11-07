# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 16:36:20 2018

@author: 施腾芮
"""

import matplotlib.pyplot as plt

pointlist = [[-1482.0508075688774, 683.0127018922194], [-1482.0508075688774, -183.01270189221935], [1982.0508075688774, 683.0127018922194], [1982.0508075688774, -183.01270189221935], [-2348.076211353316, 683.0127018922194], [-2348.076211353316, -183.01270189221935], [2848.076211353316, 683.0127018922194], [2848.076211353316, -183.01270189221935]]
plt.plot([pointlist[0][0],pointlist[1][0]], [pointlist[0][1],pointlist[1][1]])
plt.plot([pointlist[0][0],pointlist[3][0]], [pointlist[0][1],pointlist[3][1]])
plt.plot([pointlist[0][0],pointlist[4][0]], [pointlist[0][1],pointlist[4][1]])
plt.plot([pointlist[1][0],pointlist[2][0]], [pointlist[1][1],pointlist[2][1]])
plt.plot([pointlist[1][0],pointlist[5][0]], [pointlist[1][1],pointlist[5][1]])
plt.plot([pointlist[2][0],pointlist[3][0]], [pointlist[2][1],pointlist[3][1]])
plt.plot([pointlist[2][0],pointlist[6][0]], [pointlist[2][1],pointlist[6][1]])
plt.plot([pointlist[3][0],pointlist[7][0]], [pointlist[3][1],pointlist[7][1]])
plt.plot([pointlist[4][0],pointlist[5][0]], [pointlist[4][1],pointlist[5][1]])
plt.plot([pointlist[4][0],pointlist[7][0]], [pointlist[4][1],pointlist[7][1]])
plt.plot([pointlist[5][0],pointlist[6][0]], [pointlist[5][1],pointlist[6][1]])
plt.plot([pointlist[6][0],pointlist[7][0]], [pointlist[6][1],pointlist[7][1]])