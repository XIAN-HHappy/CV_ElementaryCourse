#-*-coding:utf-8-*-
# date:2021-03-21
# Author: Eric.Lee
'''
学习内容（Contents）:
    1、绘制线段
'''

import cv2 # 导入OpenCV库

if __name__ == "__main__":

    path = 'images/1.jpg'
    img = cv2.imread(path)

    x1,y1 = 200,200# 坐标，为整形 int
    x2,y2 = 500,500# 坐标，为整形 int
    cv2.line(img, (x1,y1),(x2,y2), (0,150,255), 5)

    cv2.namedWindow('image',0)
    cv2.imshow('image',img)# 显示图片

    cv2.waitKey(0)# 等待，直到键盘有按键按下
    cv2.destroyAllWindows() # 销毁所有显示窗口
