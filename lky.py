from cv2 import cv2
import numpy as np
img = cv2.imread('image/label.jpg')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # 转化为hsv的的图
cv2.namedWindow("imge", cv2.WINDOW_NORMAL)
cv2.imshow("imge", img)
lower_blue = np.array([90, 43, 46])
upper_blue = np.array([110, 255, 255])
# kernel = np.ones((5, 5), np.uint8)
# erosion = cv2.erode(img2, kernel, iterations=1)
mask = cv2.inRange(img2, lower_blue, upper_blue)  # 追踪你所需要的颜色的物品#读取红色物体，但未灰色
res = cv2.bitwise_and(img2, img, mask=mask)  # 让hsv的图有色彩#二值化处理，让其有颜色
# cv2.imshow("imge2", erosion)
gray_img = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("imge", th)
cv2.waitKey(0)
