import numpy as np
from cv2 import cv2


def cv_show(name, img):
    cv2.imshow(name, img)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()


# Create a black image
img = np.zeros((512, 512, 3), np.uint8)
pts = np.array([[10, 5], [200, 300], [70, 20], [500, 100],
                [40, 89]], np.int32)  # 必须为int32类型
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], False, (0, 255, 255))

cv_show('img', img)
