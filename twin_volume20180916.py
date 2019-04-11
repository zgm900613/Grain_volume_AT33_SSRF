# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 12:22:41 2018

@author: 朱高明
"""

import pandas as pd
import numpy as np
import os
import math
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import metrics
#from sklearn.metrics import r2_score


def in_excel(file_path):   #define a function to import excel file
    x = pd.read_excel(file_path)
    xM = x.ix[:, :]
    xMatrix = np.matrix(xM)
    return(xMatrix)

file_names = os.listdir(r'G:\SynchrotronXray\SSRF20170103\AT33-100\10deg\Gauss')
a = 'G:/SynchrotronXray/SSRF20170103/AT33-100/10deg/Gauss/'
#FWHM_Para = in_excel(r'G:\SynchrotronXray\SSRF20170103\para\FWHM_parameter.xlsx')



data_list = []
for i in range(len(file_names)):
    file_path = a + file_names[i]
    data = in_excel(file_path)
    data_list.append(data)

Area = np.zeros((len(data_list[0]), 9))
Area_fraction = np.zeros((len(data_list[0]), 9))


#for i in range(len(file_names)):#去掉峰面积太小的峰， 去掉峰FWHM太大的
#    for j in range(len(data_list[0])):
#        for k in range(10):
#            if data_list[i][j, 12 * k + 7] < 5:#去掉峰面积太小的峰
#                data_list[i][j, 12 * k + 10] = 0
#            if data_list[i][j, 12 * k + 9] > 0.4:#去掉峰FWHM太大的
#                data_list[i][j, 12 * k + 10] = 0
#            if data_list[i][j, 12 * k + 3] > 34 or data_list[i][j, 12 * k + 3] < 14:#去掉theta不准的
#                data_list[i][j, 12 * k + 10] = 0
for i in range(len(data_list[0])):#求Area
#    for j in range(len(data_list[0])):
    for j in range(9):
        Area[i, j] = data_list[j][i, 12 * 4  + 10]

for i in range(len(data_list[0])):
    for j in range(9):
        Area_fraction[i, j] = Area[i, j] / sum(Area[i, :])

#for i in range(len(file_names)):#求FWHM Theta2
#    for j in range(len(data_list[0])):
#        for k in range(10):
#            FWHM[j, k] += data_list[i][j, 12 * k + 9] * data_list[i][j, 12 * k + 10] / Area[j, k]
#            Theta2[j, k] += data_list[i][j, 12 * k + 3] * data_list[i][j, 12 * k + 10] / Area[j, k]    
#
#for i in range(len(data_list[0])):#求g
#    for j in range(10):
#        g[i, j] = 1/(0.688/2/math.sin(Theta2[i, j]/2/180*math.pi)) * 10

#for i in range(len(data_list[0])):
#    for j in range(10):
#        FWHM[i, j] = 

#
fig = plt.figure(figsize = (20, 20))
for i in range(len(data_list[0])):
    ax1 = fig.add_subplot(8, 10, i+1)
    ax1.bar(range(9), Area_fraction[i])
#    slope[i, 0], intercept[i, 0], R2[i, 0] = linefit(g[i, :], FWHM[i, :])
#    ax1.set_ylim([0, 0.3])
    
fig2 = plt.figure(figsize = (8,8))#ax2 = fig2.add_subplot(1,1,1)
ax2 = fig2.add_subplot(111)
ax2.bar(range(9), Area_fraction[6])



#    
#ax1 = plt.figure(figsize = (10,10))
#ax11 = ax1.add_subplot(111)
#ax11.scatter(1,1)
##ax11.show()
##
#ax2 = plt.figure(figsize = (10,10))
#ax22 = ax2.add_subplot(111)
#
#ax22.scatter(1,1)
#ax22.show()









