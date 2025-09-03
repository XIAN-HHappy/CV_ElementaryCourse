#-*-coding:utf-8-*-
# date:2021-10-4
# Author: Eric.Lee
'''
学习内容（Contents）:
    1、读取 labelme mask
    2、图像和mask（掩码）旋转增强方式
'''
import os
import json
import cv2
import numpy as np
import shutil
import random
# 图像旋转
def M_rotate_image(image , angle , cx , cy):
    '''
    图像旋转
    :param image:
    :param angle:
    :return: 返回旋转后的图像以及旋转矩阵
    '''
    (h , w) = image.shape[:2]
    # (cx , cy) = (int(0.5 * w) , int(0.5 * h))
    M = cv2.getRotationMatrix2D((cx , cy) , -angle , 1.0)
    cos = np.abs(M[0 , 0])
    sin = np.abs(M[0 , 1])

    # 计算新图像的bounding
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    M[0 , 2] += int(0.5 * nW) - cx
    M[1 , 2] += int(0.5 * nH) - cy
    return cv2.warpAffine(image , M , (nW , nH),flags = cv2.INTER_NEAREST,borderValue = (0,0,0) ) , M

if __name__ == "__main__":
    path_ = "./datasets/"
    for f_ in os.listdir(path_):
        if ".json" not in f_:
            continue
        path_label = path_ + f_
        f = open(path_label, encoding='utf-8')#读取 json文件
        dict_ = json.load(f)
        print("dict_ keys : ",dict_.keys())
        dict_ = dict_["shapes"]
        path_img = path_label.replace(".json",".jpg")
        img_ = cv2.imread(path_img)
        img_b = np.zeros((img_.shape[0],img_.shape[1])).astype(np.uint8)
        for d_ in dict_:
            print(len(d_["points"]))
            points_array = np.zeros((1,len(d_["points"]),2),dtype = np.int32)


            for i in range(len(d_["points"])):
                x,y = d_["points"][i]
                points_array[0,i,0] = x
                points_array[0,i,1] = y
            cv2.drawContours(img_,points_array,-1,(0,255,0),thickness=-1)
            cv2.drawContours(img_b,points_array,-1,255,thickness=-1)

        cv2.namedWindow("img",0)
        cv2.imshow("img",img_)
        cv2.namedWindow("imgb",0)
        cv2.imshow("imgb",img_b)

        cx = int(img_.shape[1]/2)
        cy = int(img_.shape[0]/2)
        # 手势(gesture)分类建议是全角度旋转, 对于 Stanford dogs 数据集适当角度旋转扰动，目的是为了符合真实样本旋转角度样本分布情况。
        angle = random.randint(-180,180)
        range_limit_x = int(min(6,img_.shape[1]/16))
        range_limit_y = int(min(6,img_.shape[0]/16))
        offset_x = random.randint(-range_limit_x,range_limit_x)
        offset_y = random.randint(-range_limit_y,range_limit_y)
        if not(angle==0 and offset_x==0 and offset_y==0):
            img_,_  = M_rotate_image(img_ , angle , cx+offset_x , cy+offset_y)
            img_b,_  = M_rotate_image(img_b , angle , cx+offset_x , cy+offset_y)

        cv2.namedWindow("img_rot",0)
        cv2.imshow("img_rot",img_)
        cv2.namedWindow("imgb_rot",0)
        cv2.imshow("imgb_rot",img_b)


        if cv2.waitKey(0) == 27:
            break
