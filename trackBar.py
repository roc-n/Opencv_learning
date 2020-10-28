from imread import cv
from cv2 import cv2
import numpy as np

# 回调函数


def nothing(x):
    pass


img = np.zeros((600, 1000, 3), np.uint8)
img[:] = (255, 255, 255)
cv2.namedWindow('Trackbar image')

cv2.createTrackbar('R', 'Trackbar image', 0, 255, nothing)
cv2.createTrackbar('G', 'Trackbar image', 0, 255, nothing)
cv2.createTrackbar('B', 'Trackbar image', 0, 255, nothing)

switch = '0:OFF\n1:ON'
cv2.createTrackbar(switch, 'Trackbar image', 0, 1, nothing)

while True:
    cv2.imshow('Trackbar image', img)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

    r = cv2.getTrackbarPos('R', 'Trackbar image')
    g = cv2.getTrackbarPos('G', 'Trackbar image')
    b = cv2.getTrackbarPos('B', 'Trackbar image')
    s = cv2.getTrackbarPos(switch, 'Trackbar image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [r, g, b]

s = [[1, 2, 3] for i in range(6)]
p = [1, 2, 3, 4, 5]
p[:] = [1, 1, 1]

# print(test)

print(p)


cv2.destroyWindow("Trackbar image")
