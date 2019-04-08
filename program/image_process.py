# encoding:utf-8

import cv2
import os

image_lists = []
def read_images(load_path):
	# 读取文件夹中的每一张图片名
	each_image_name = os.listdir(load_path)
	#获取把图片的完整路径
	for i in range(len(each_image_name)):
		if each_image_name[i][-3:] == 'jpg':
			image_lists.append(load_path + '\\' + each_image_name[i])
	return image_lists


def main(image_store_path):
	i = 0
	for image_path in image_lists:
		#用opencv读取图片
		image = cv2.imread(image_path)
		#获得图片不带.jpg的图片名
		image_name = image_path.split('\\')[-1].split('.')[0]

		# Flipped Horizontally 水平翻转
		h_flip = cv2.flip(image, 1)
		new_name_h = image_store_path + '\\' + image_name + '-' + 'h'+ '.jpg' 
		cv2.imwrite(new_name_h, h_flip)
		i+=1
		# # Flipped Vertically 垂直翻转
		# v_flip = cv2.flip(image, 0)
		# new_name_v = image_store_path + '\\' + image_name + '-' + 'v'+ '.jpg' 
		# cv2.imwrite(new_name_v, v_flip)
		# i+=1
		# # Flipped Horizontally & Vertically 水平垂直翻转
		# hv_flip = cv2.flip(image, -1)
		# new_name_hv = image_store_path + '\\' + image_name + '-' + 'hv'+ '.jpg' 
		# cv2.imwrite(new_name_hv, hv_flip)
		# i+=1

	print('FINISHED! TOTALLY GENERIZE %d IMAGES'%i)



if __name__ == "__main__":
	load_path = input('please input the load_path:' + '\n')
	image_store_path = input('please input the image_path:'+'\n')
	read_images(load_path)
	main(image_store_path)