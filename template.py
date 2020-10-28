from cv2 import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('blackmagician.jpg')
cv.imshow('nae',img)

template = cv.imread('black_template.jpg')

methods = 'TM_SQDIFF'
res = cv.matchTemplate(img, template, cv.TM_SQDIFF)
print(res.shape)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
# print(min_val)
# print(max_val)
# print(min_loc)
# print(max_loc)


top_left = min_loc
bottom_right = max_loc
cv.rectangle(img, top_left, bottom_right, 255, 2)

plt.subplot(121), plt.imshow(res, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.show()
