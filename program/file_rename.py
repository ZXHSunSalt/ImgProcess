import os
import numpy as np
input_path_name =  input('please input the path:')
dst_path = input('please input the dst path:')
#path_name :表示你需要批量改的文件夹

for item in os.listdir(input_path_name):#进入到文件夹内，对每个文件进行循环遍历
#	os.path.join(path_name,item)表示找到每个文件的绝对路径并进行拼接操作
#	rename img file name
#   os.rename(os.path.join(input_path_name,item),os.path.join(input_path_name,(input_path_name.split('\\')[-1]+ str(i)+'.jpg')))
		os.rename(os.path.join(input_path_name,item),os.path.join(dst_path,(item.split('.')[0] +'_L'  + str(0.4) + '.xml')))


		


	
