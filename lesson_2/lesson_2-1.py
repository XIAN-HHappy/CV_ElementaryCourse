#-*-coding:utf-8-*-
# date:2021-03-21
# Author: Eric.Lee
'''
学习内容（Contents）:
    1、绘制空心圆
    2、绘制实心圆
'''

import cv2 # 导入OpenCV库

if __name__ == "__main__":

    path = 'images/1.jpg'
    img = cv2.imread(path)

    x,y = 500,400 # 圆心 ,为整形 int
    Rr = 60# 半径,为整形 int
    cv2.circle(img, (x,y), Rr, (0,0,255), -1) #绘制实心圆
    #
    x,y = 300,200 # 圆心 ,为整形 int
    Rr = 120# 半径,为整形 int
    cv2.circle(img, (x,y), Rr, (0,255,0), 4) #绘制空心圆

    cv2.namedWindow('image',0)
    cv2.imshow('image',img)# 显示图片

    cv2.waitKey(0)# 等待，直到键盘有按键按下
    cv2.destroyAllWindows() # 销毁所有显示窗口
