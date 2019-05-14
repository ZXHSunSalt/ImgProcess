# coding=utf-8
import os
# 全局变量
VIDEO_PATH = input('please input the path of video:' + '\n')# 视频地址
EXTRACT_FOLDER = input('please input the path of storing video:' + '\n') # 存放帧图片的位置
EXTRACT_FREQUENCY = 10# 帧提取频率

def directory_exits(directory):
    if os.path.exists(directory):
        return True
    else:
        return False

def make_directory(directory):
    """创建目录"""
    os.makedirs(directory)

def extract_frames(video_path, dst_folder, video_name,index):
    # 主操作
    import cv2
    video = cv2.VideoCapture()
    if not video.open(video_path):
        print("can not open the video")
        exit(1)
    count = 1
    while True:
        _, frame = video.read()
        if frame is None:
            break
        if count % EXTRACT_FREQUENCY == 0:
            save_path = dst_folder+'/'+video_name+ str(index) +'.jpg'
            cv2.imwrite(save_path, frame)
            index += 1
        count += 1
    video.release()
    return index


def main(item_path,video_name):
    # 抽取帧图片，并保存到指定路径
    if not directory_exits(EXTRACT_FOLDER):
        make_directory(EXTRACT_FOLDER)
    num = extract_frames(item_path, EXTRACT_FOLDER,video_name,0)
    return num

if __name__ == '__main__':
    c1 = 0
    c2 = 0
    c3 = 0
    list1 = os.listdir(VIDEO_PATH)
    for each in list1:
        list2 = os.listdir(VIDEO_PATH+'/'+each)
        for video in list2:
            list3 = os.listdir(VIDEO_PATH+'/'+each+'/'+video)
            for v in list3:
                file_type = v[-3:]
                if file_type == 'mp4' or file_type == 'avi':
                    item_path = VIDEO_PATH+'/'+each+'/'+video+'/'+v
                    try:
                        num = main(item_path,each+'_'+video+'_'+v[:-4])
                        c3 += num
                    except:
                        print("load file error!")
    # 打印出所提取帧的总数
    print("Totally save {:d} pics".format(c3))           