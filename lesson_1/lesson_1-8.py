#-*-coding:utf-8-*-
# date:2021-03-21
# Author: Eric.Lee
'''
学习内容（Contents）:
    1、加载相机并显示
'''

import cv2
if __name__ == "__main__":
    #加载相机
    cap = cv2.VideoCapture(0) #一般usb默认相机号为 0，如果没有相机无法启动，如果相机不为0需要自行确定其编号。

    while True:
        ret, img = cap.read()# 获取相机图像
        if ret == True:# 如果 ret 返回值为 True，显示图片
            cv2.namedWindow('camera',0)
            cv2.imshow("camera", img)
            key = cv2.waitKey(33)
            if key == 27:#当按键esc，退出显示
                break
        else:# ret 返回 False，退出循环
            break

    cap.release()#释放
    cv2.destroyAllWindows()#关闭显示窗口
