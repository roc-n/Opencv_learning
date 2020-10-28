from cv2 import cv2 as cv
import numpy as np

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
# 四个参数参数分别为起始点，终点，颜色，线条厚度，-1则全部填充
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 6)
cv.imshow('line', img)

key = cv.waitKey(0)
if key == ord('q'):
    cv.destroyAllWindows()
