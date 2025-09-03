#-*-coding:utf-8-*-
# date:2021-03-20
# Author: Eric.Lee
'''
学习内容（Contents）:
    1、图像左右翻转
    2、图像上下翻转
    3、图像同时左右上下一起翻转
'''

import cv2 # 导入OpenCV库

if __name__ == "__main__":

    path = 'images/1.jpg'

    img = cv2.imread(path)# 读取图片
    cv2.namedWindow('image',0)
    cv2.imshow('image',img) # 显示图片

    img_flip = cv2.flip(img,1) # 图像左右翻转
    cv2.namedWindow('img_flip_LR',0)
    cv2.imshow('img_flip_LR',img_flip) # 显示图片
    cv2.waitKey(500)# 等待500ms

    img_flip = cv2.flip(img,0) # 图像上下翻转
    cv2.imshow('img_flip_UD',img_flip) # 显示图片
    cv2.waitKey(500)# 等待500ms

    img_flip = cv2.flip(img,-1) # 图像顺直水平同时翻转
    cv2.imshow('img_flip_LRUD',img_flip) # 显示图片
    cv2.waitKey(0)# 等待，直到键盘有按键按下

    cv2.destroyAllWindows()# 销毁图片显示窗口
