from cv2 import cv2 as cv
import numpy as np

img = cv.imread('star.jpg')
px = img[100, 100]
print(px)
blue = img[100, 100, 0]
print(blue)

# 修改像素的值
img[100, 100] = [12, 0, 255]
print(img[100, 100])

# 获取像素值及修改的更好方法(利用numpy进行矩阵运算)
print(img.item(100, 100, 2))
img.itemset((10, 10, 2), 99)
print(img.item(10, 10, 2))

#获取图像属性，图像的属性包括:行,列,通道,图像数据类型,像素数目等
print(img.shape)  #(行数，列数，通道数)
print(img.size)  #图像像素数目
print(img.dtype)  #图像数据类型(debug时很重要)

