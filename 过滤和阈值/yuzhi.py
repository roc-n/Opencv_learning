from cv2 import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('star.jpg',cv.IMREAD_GRAYSCALE)
ret,thresh1=cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2=cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
ret,thresh5=cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
images = [img,thresh1,thresh2,thresh3,thresh4,thresh5]
titles=['Original_Image','Binary','Binary_INV','TRUNC','TOZERO','TOZERO_INV']
for i in range(6):
    plt.subplot(1, 3, i + 1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])#传入空列表不显示x,y轴数值
 
plt.show()
    