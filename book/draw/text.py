from cv2 import cv2 as cv
import numpy as np
from circle import cv_show




img = np.zeros((512, 512, 3), np.uint8)
font = cv.FONT_HERSHEY_COMPLEX
# 要传入的文字，位置，字体，大小，颜色，线条粗细
cv.putText(img, 'OpenCv', (10, 500), font, 3,
           (255, 255, 255), 2, lineType=cv.LINE_AA)
cv_show('text', img)
