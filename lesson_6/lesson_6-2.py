#-*-coding:utf-8-*-
# date:2021-07-21
# Author: Eric.Lee
'''
学习内容（Contents）:
    1、相机图像存储图片
'''
import os
import cv2
import time
if __name__ == "__main__":
    path = "./images/" # 图像保存路径
    if not os.path.exists(path): # 如果文件夹不存在
        os.mkdir(path) # 生成文件夹

    #加载相机
    cap = cv2.VideoCapture(0) #一般usb默认相机号为 0，如果没有相机无法启动，如果相机不为0需要自行确定其编号。
    frame_idx = 0
    loc_time = time.localtime()
    str_time = time.strftime("%Y-%m-%d_%H-%M-%S", loc_time)
    while True:
        ret, img = cap.read()# 获取相机图像
        if ret == True:# 如果 ret 返回值为 True，显示图片
            cv2.namedWindow('camera',0)
            cv2.imshow("camera", img)

            cv2.imwrite("{}{}-{}.png".format(path,str_time,frame_idx),img)
            frame_idx += 1
            key = cv2.waitKey(33)
            if key == 27:#当按键esc，退出显示
                break
        else:# ret 返回 False，退出循环
            break

    cap.release()#释放
    cv2.destroyAllWindows()#关闭显示窗口
