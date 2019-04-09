#-*- coding:utf-8 -*-
'''
Created on 2019年4月8日

@author: Administrator
'''

import os 
import sys
import xml.etree.cElementTree as ET
import glob
import pandas as pd
import numpy as np

indir=input('please input the input directory:')   #xml目录
outdir=input('please input the output dierctory:')  #txt目录


def get_xml_file_path(indir):
    '''
    GET THE XML FILE PAHT IN ACCORDING FILES
    RETURN: XML_LISTS(list)
    '''
    xml_lists = []
    for xml in glob.glob(indir + '/*.xml'):
        xml_lists.append(xml)
    return xml_lists

def get_data(xml):
    '''
    FUNCTION:GET THE xmin,xmax,w IN EACH object OF XML
             GET THE objects IN EACH XML
    RETURN: tree,objects,w,xmin_list,xmax_list
    '''
    # get the structure of each xml file
    tree = ET.parse(xml)
    root = tree.getroot()
    # get the width of each img
    w = int(root.find('size')[0].text)
    # get each object of each xml file
    objects = root.findall('object')
    xmin_list = []
    xmax_list = []
    for member in root.findall('object'):
        xmin = int(member[4][0].text)
        xmax = int(member[4][2].text)
        xmin_list.append(xmin)
        xmax_list.append(xmax)
    return xmin_list,xmax_list,w,objects,tree

def xml_process(xml_lists):
    '''
    FUNCTION: CHANGE TEXT IN EACH ATTIBUTE
    NOTICE: THE TYPE OF XML TEXT MUST TO BE str
    '''
    for xml in xml_lists:
        # get the name of xml file(including postfix), rather than the path of xml file
        name = xml.split('\\')[-1]
        xmin ,xmax, w, objects,tree = get_data(xml)
        # get the dimention of the object
        obj_dimen = np.array(objects).shape
        
        # change content of each attribute
        for i in range(obj_dimen[0]):
            objects[i].find('bndbox').find('xmin').text = str(w-xmax[i])
            objects[i].find('bndbox').find('xmax').text = str(w-xmin[i])
        # save the new content to the new xml file
        tree.write(outdir + '/' + name.split('.')[0] +  '-h.xml')

    
def xml_to_csv(indir):
    '''
    FUNCTION: TRANSFORM XML FILE TO CSV FILE
    PARAMETERS: indir - THE PAHT OF XML FILE
    '''
    # define a list to store all the xml files
    xml_files = []
    
    # get corresponding content according xml files
    for xml in glob.glob(indir+'/*.xml'):
        tree = ET.parse(xml)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_files.append(value)
    
    # define the title of csv
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    # define pandas dataframe
    xml_df = pd.DataFrame(xml_files,columns = column_name)
    return xml_df

# def xml_to_txt(indir,outdir):    
#     os.chdir(indir)
#     annotations = os.listdir('.')
#     annotations = glob.glob(str(annotations)+'*.xml')
#     for i, file in enumerate(annotations):
# 
#         file_save = file.split('.')[0]+'.txt'
#         file_txt=os.path.join(outdir,file_save)
#         f_w = open(file_txt,'w')
# 
#         # actual parsing
#         in_file = open(file)
#         tree=ET.parse(in_file)
#         root = tree.getroot()
# 
#         for obj in root.iter('object'):
#                 current = list()
#                 name = obj.find('name').text
# 
#                 xmlbox = obj.find('bndbox')
#                 xn = xmlbox.find('xmin').text
#                 xx = xmlbox.find('xmax').text
#                 yn = xmlbox.find('ymin').text
#                 yx = xmlbox.find('ymax').text
#                 #print xn
#                 f_w.write(xn+' '+yn+' '+xx+' '+yx+' ')
#                 f_w.write(name.encode("utf-8")+'\n')

if __name__ == '__main__':
### xml_to_csv and save file
#     xml_df = xml_to_csv(indir)
      ## save file to csv
#     xml_df.to_csv(outdir+'/'+'label.csv',index=None)

    xml_lists = get_xml_file_path(indir)
    xml_process(xml_lists)