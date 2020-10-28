import numpy as np
from cv2 import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('object.jpg', 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()