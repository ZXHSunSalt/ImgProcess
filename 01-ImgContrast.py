#-*- coding:utf-8 -*-
'''
Created on 2019年4月8日

@author: Administrator
'''
import os
import cv2
import numpy as np

indir = input('please input the image path:')
outdir = input('please input the output path of image:')

def get_imge_list(indir):
    '''
    FUNCTION: GET EACH IMAGE OF THE CURRENT PATH
    RETURN : IMAGE LIST(NOT INCLUDING PATH,JUST THE FILE NAME)
    '''
    img_lists = []
    # get all the files in the input path
    file_lists = os.listdir(indir)
    # get the image files
    for file in file_lists:
        if file[-3:] == 'jpg':
            img_lists.append(file)
    return img_lists

def img_contrast(indir, img_lists):
    '''
    FUNCTION: GENERATE IMAGES WITH 4 DIFFERENT BRIGHTNESS LEVELS AND SAVE THE FILES WITH NEW NAME
              G(x,y) = aF(x,y)+b
    PARAMETERS: img_lists - image file names (not the path)
    '''
    # set for count the numbers of images
    flag = 1
    
    # do contrast process for each img
    for img_name in img_lists:
        img = cv2.imread(indir + '/' + img_name)
        # set the brightness level interval,each interval is 0.4
        internal = np.arange(0.4,2,0.4)
        for i in internal:
            # change value of each image, it is must be array
            res = np.uint8(np.clip((i*img) + i*25, 0, 255))
            cv2.imwrite(outdir + '/' + img_name.split('.')[0] +'_L'  + str(i) + '.jpg', res)
        
        print('finished %d pictures'%flag)
        flag += 1
        
if __name__ == '__main__':
    img_lists = get_imge_list(indir)
    img_contrast(indir, img_lists)
