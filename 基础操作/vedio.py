import numpy as np
from cv2 import cv2 as cv
from matplotlib import pyplot as plt

cap = cv.VideoCapture('stars.mp4')





# while (True):
#     ret, frame = cap.read()

#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

#     cv.imshow('frame', gray)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
if cap.isOpened():
    open, frame = cap.read()
else:
    open = False

while open:
    ret, frame = cap.read()
    if frame is None:
        break
    if ret is True:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        cv.imshow('result',gray)
        if cv.waitKey(50) & 0xFF == 27:
            break


cap.release()
cv.destroyAllWindows()
