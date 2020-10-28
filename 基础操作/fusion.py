from cv2 import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img1 = cv.imread(r'image\castle.jpg', cv.IMREAD_COLOR)
img2 = cv.imread(r'image\horse.jpg', cv.IMREAD_COLOR)

plt.imshow(img1)
plt.xticks([])
plt.yticks([])
plt.show()