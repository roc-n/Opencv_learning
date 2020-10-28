from cv2 import cv2 as cv


def cv_show(name, img):
    cv.imshow(name, img)
    k = cv.waitKey(0)
    if k == 27:
        cv.destroyAllWindows()


img = cv.imread(r'image\space-1569133.jpg', cv.IMREAD_COLOR)
# cv.imshow('img', img)
# k = cv.waitKey(0)&0xFF
# if k == 27:
#     cv.destroyAllWindows()
# elif k == ord('s'):
#     cv.imwrite('object.jpg', img)
#     cv.destroyAllWindows()
# earth = img[0:100, 0:500,0]
cv_show('img', img)
# cv_show('earth', earth)
b, g, r = cv.split(img)
print(img.shape)
print(b)
print(g)
print(r)
image_ = cv.merge((b, g, r))
print(image_.shape)
cur_img = img.copy()


cur_img[:, :, 0] = 0
cur_img[:, :, 1] = 0
cv_show('R', cur_img)  # 显示红色只保留R通道

cur_img[:, :, 0] = 0
cur_img[:, :, 2] = 0
# cv_show(;)


print(type(img))  # 底层格式
print(img.size)  # 像素点个数
print(img.dtype)  # 图像类型
