#-*- coding:utf-8 -*-
'''
Created on 2019年4月9日

@author: Administrator
'''
import cv2
import pandas as pd
import csv


# csv_path = input('please input the csv path:')
# 
# df = pd.read_csv(csv_path)
# row, col = df.shape[0],df.shape[1]
# 
# for i in range(row):
#     w = df.width[i]
#     xmin = df.xmin[i]
#     xmax = df.xmax[i]
#     ymin = df.ymin[i]
#     ymax = df.ymax[i]
#     
#     n_xmin = w-xmax
#     n_xmax = w-xmin
#     new_box_LU = (w-xmax,ymin)
#     new_box_RD = (w-xmin,ymax)
#     
#     print(n_xmax,n_xmin)
img_path = 'C:\\Users\\Administrator\\Desktop\\wj013520-h.jpg'
w=720
x_min = 122
x_max = 226
y_min = 1
y_max = 28
img = cv2.imread(img_path)
new_img = cv2.rectangle(img,(w-x_max,y_min),(w-x_min,y_max),(128,128,128),2)
cv2.imwrite("C:\\Users\\Administrator\\Desktop\\img1-h.jpg" , new_img)
print((w-x_max,y_min),(w-x_min,y_max))
if __name__ == '__main__':
    pass