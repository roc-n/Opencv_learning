from cv2 import cv2 as cv
import imutils
img = cv.imread('star.jpg')
(h, w, d) = img.shape
print('width={},height={},depth={}'.format(w, h, d))

# cv.imshow('img', img)
# cv.waitKey(0)

(B, G, R) = img[400, 350]
print('R={},G={},B={}'.format(R, G, B))

roi = img[290:380, 290:380]
# cv.imshow('roi', roi)
# cv.waitKey(0)

resized = cv.resize(img, (300, 200))#后面的元组一二个元素分别代表w,h.
# cv.imshow('fixed img', resized)
# cv.waitKey(0)

r = 300.0 / w
dim = (300, int(h * r))#dimension
resized = cv.resize(img, dim)
# cv.imshow('resized', resized)
# cv.waitKey(0)

center = (w // 2, h // 2)
M = cv.getRotationMatrix2D(center, -180, 1.0)
rotated=cv.warpAffine(img,M,(w,h))
cv.imshow('Opencv Rotation', rotated)
cv.waitKey(0)
rotated = imutils.rotate_bound(img, -45)
cv.imshow('Opencv Rotation', rotated)
cv.waitKey(0)

blurred = cv.GaussianBlur(img, (5, 5), 0)
cv.imshow('blurred', blurred)
cv.waitKey(0)