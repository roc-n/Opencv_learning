from cv2 import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('tree.jpg')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

hist = cv.calcHist([hsv], [0, 1], None, [150, 256], [0, 180, 0, 256])

plt.imshow(hist, interpolation='nearest')
plt.show()