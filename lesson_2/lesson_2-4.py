#-*-coding:utf-8-*-
# date:2021-03-22
# Author: Eric.Lee
'''
学习内容（Contents）:
    1、图像上绘制文本
    2、保存图片
'''

import cv2 # 导入OpenCV库

if __name__ == "__main__":

    path = 'images/1.jpg'
    img = cv2.imread(path)

    cv2.putText(img, " Hello Computer Vision !", (5,55),cv2.FONT_HERSHEY_DUPLEX, 1.5, (55, 0, 220),7)
    cv2.putText(img, " Hello Computer Vision !", (5,55),cv2.FONT_HERSHEY_DUPLEX, 1.5, (255, 50, 50),2)
    cv2.imwrite("save.jpg",img)
    cv2.namedWindow('image',0)
    cv2.imshow('image',img)# 显示图片

    cv2.waitKey(0)# 等待，直到键盘有按键按下
    cv2.destroyAllWindows() # 销毁所有显示窗口
