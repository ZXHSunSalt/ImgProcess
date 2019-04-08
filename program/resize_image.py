import os
import cv2


def read_images(load_path):
	image_lists = []
	image_names = os.listdir(load_path)
	for each in image_names:
		image_lists.append(each)
	return image_lists

def main(image_path, images):
	for each_image in images:
		img = cv2.imread(each_image)
		image_resize = cv2.resize(img,(128,128), interpolation=cv2.INTER_CUBIC)
		cv2.imwrite(image_path + '.jpg',image_resize)

if __name__ == '__main__':
	load_path = input('please input the load_path:')
	image_path = input('please input the image_storing_path:')
	image_lists = read_images(load_path)
	main(image_path,image_lists)