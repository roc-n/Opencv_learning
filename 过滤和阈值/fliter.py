from cv2 import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('tree.jpg', cv.IMREAD_COLOR)
median=cv.medianBlur(img,5)



cv.imshow('median', median)
cv.waitKey(0)
cv.destroyAllWindows()