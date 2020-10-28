from cv2 import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# 展示图像
def cv_show(name, img):
    cv.imshow(name, img)
    k = cv.waitKey(0)
    if k == 27:
        cv.destroyAllWindows()


def calculate(newpoint, oldpoint):
    """
    计算两点之间距离
    """
    vector1 = np.array([newpoint[0], newpoint[1]])
    vector2 = np.array([oldpoint[0], oldpoint[1]])
    distance = np.linalg.norm(vector1 - vector2)
    return distance


def check(point, points_list):
    """
    检测是否为新的中心点
    """
    if (point[0] - points_list[-1][0]) > 5 or (point[1] - points_list[-1][1]) > 5:
        return True
    return False


def update(newpoint, points_list, choice):
    """
    更新信息
    """
    global Max_dis_1, Maxpoint_1, Max_dis_2, Maxpoint_2
    for old in points_list:
        distance = calculate(newpoint, old)
        if choice == 1:
            if (distance > Max_dis_1):
                Max_dis_1 = distance
                Maxpoint_1.clear()
                Maxpoint_1.append(newpoint)
                Maxpoint_1.append(old)
        else:
            if (distance > Max_dis_2):
                Max_dis_2 = distance
                Maxpoint_2.clear()
                Maxpoint_2.append(newpoint)
                Maxpoint_2.append(old)
    points_list.append(newpoint)


def nothing(x):
    pass


Max_dis_1 = 0  # 声明最大距离
Max_dis_2 = 0

Maxpoint_1 = []  # 储存最大距离两端点
Maxpoint_2 = []

points_list_1 = []  # 存储每个棋子的中心点序列
points_list_2 = []

img = cv.imread('image/test_img.jpeg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 转化为灰度图
template1 = cv.imread('image/test_img_white.jpeg', 0)
template2 = cv.imread('image/test_img_black.jpeg', 0)
w1, h1 = template1.shape[::-1]
w2, h2 = template2.shape[::-1]
# 模板匹配
res1 = cv.matchTemplate(img_gray, template1, cv.TM_CCOEFF_NORMED)
res2 = cv.matchTemplate(img_gray, template2, cv.TM_CCOEFF_NORMED)
# min1_val1, max1_val, min1_loc, max1_loc = cv.minMaxLoc(res1)
# min2_val, max2_val, min2_loc, max2_loc = cv.minMaxLoc(res2)

# 设定阈值
thresh1 = 0.7
thresh2 = 0.8
loc1 = np.where(res1 >= thresh1)
loc2 = np.where(res2 >= thresh2)

# 对于白子
for pt in zip(*loc1[::-1]):
    newpoint = (pt[0] + w1 / 2, pt[1] + h1 / 2)
    cv.rectangle(img, pt, (pt[0] + w1, pt[1] + h1), (0, 0, 255), 1)  # 绘制轮廓
    if len(points_list_1) == 0:
        points_list_1.append(newpoint)
    elif check(newpoint, points_list_1):
        update(newpoint, points_list_1, 1)  # 若为新点则更新

# 对于黑子
for pt in zip(*(loc2[::-1])):
    newpoint = (pt[0] + w2 / 2, pt[1] + h2 / 2)
    cv.rectangle(img, pt, (pt[0] + w2, pt[1] + h2), (0, 255, 0), 1)
    if len(points_list_2) == 0:
        points_list_2.append(newpoint)
    elif check(newpoint, points_list_2):
        update(newpoint, points_list_2, 2)

print(Maxpoint_1)
print(Maxpoint_2)

# 转化为整数点以作直线
line_point_1_a = (int(Maxpoint_1[0][0]), int(Maxpoint_1[0][1]))
line_point_1_b = (int(Maxpoint_1[1][0]), int(Maxpoint_1[1][1]))
line_point_2_a = (int(Maxpoint_2[0][0]), int(Maxpoint_2[0][1]))
line_point_2_b = (int(Maxpoint_2[1][0]), int(Maxpoint_2[1][1]))
# 画出直线
cv.line(img, line_point_1_a, line_point_1_b, (0, 0, 255), 2)
cv.line(img, line_point_2_a, line_point_2_b, (0, 255, 0), 2)


cv.namedWindow('template')
cv.createTrackbar('Canny_thresh1', 'template', 41, 255, nothing)
cv.createTrackbar('Canny_thresh2', 'template', 237, 255, nothing)
# cv.createTrackbar('thresh', 'template', 100, 255, nothing)
# cv.createTrackbar('minLine', 'template', 5, 50, nothing)
# cv.createTrackbar('maxlineGap', 'template', 1, 50, nothing)

while True:
    lower = cv.getTrackbarPos('Canny_thresh1', 'template')
    upper = cv.getTrackbarPos('Canny_thresh2', 'template')
    edges = cv.Canny(img_gray, lower, upper, apertureSize=3)
    # thresh = cv.getTrackbarPos('thresh', 'template')
    # minLineLength = cv.getTrackbarPos('minLine', 'template')
    # maxLineGap = cv.getTrackbarPos('maxlineGap', 'template')
    thresh=100
    minLineLength = 5
    maxLineGap=1
    lines = cv.HoughLinesP(edges, 1, np.pi / 180, thresh,  # 第二第三参数都为精确度
                           minLineLength, maxLineGap)
    img_ = img.copy()
    for line in lines:  # 此处教材有误，按教材只能画出一条
        x1 = line[0][0]
        y1 = line[0][1]
        x2 = line[0][2]
        y2 = line[0][3]
        cv.line(img_, (x1, y1), (x2, y2), (255, 0, 255), 2)
    cv.imshow('template', img_)
    key = cv.waitKey(10)
    if key == 27:
        break