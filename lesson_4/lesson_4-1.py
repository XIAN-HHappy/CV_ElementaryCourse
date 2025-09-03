#-*-coding:utf-8-*-
# date:2021-04-13
# Author: Eric.Lee
'''
学习内容（Contents）:
    1、生成文件夹
'''
import os
if __name__ == "__main__":
    path = "./dataset"
    if not os.path.exists(path): # 如果文件夹不存在
        os.mkdir(path) # 生成文件夹
