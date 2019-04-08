#-*- coding:utf-8 -*-
'''
Created on 2019年4月8日

@author: Administrator
'''

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Administrator\\Desktop\\020.jpg")
internal = np.arange(0.4,2,0.4)
for i in internal:
    res = np.uint8(np.clip((i*img) + i*25,0,255))
    cv2.imwrite('C:\\Users\\Administrator\\Desktop\\' + 'L-L' + str(i) + '.jpg', res)

if __name__ == '__main__':
    pass