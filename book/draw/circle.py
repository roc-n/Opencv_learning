from cv2 import cv2 as cv
import numpy as np

def cv_show(name, img):
    cv.imshow(name, img)
    k = cv.waitKey(0)
    if k == 27:
        cv.destroyAllWindows()


img = np.zeros((512, 512, 3), np.uint8)
#圆心与半径
# cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
cv.circle(img, (447, 63), 63, (0, 0, 255), 3)

cv_show('img',img)