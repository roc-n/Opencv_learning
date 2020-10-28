from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('star.jpg', 0)
# flatten() 将数组变成一维
hist, bins = np.histogram(img.flatten(), 256, [0, 256])
# 计算累积分布图
cdf = hist.cumsum()  # 元素累计和，cdf为累计分布函数
# 构建 Numpy 掩模数组, cdf 为原数组,当数组元素为 0 时,掩盖(计算时被忽略)。
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
# 对被掩盖的元素赋值,这里赋值为 0
cdf = np.ma.filled(cdf_m,0).astype('uint8')



cdf_normalized = cdf * hist.max() / cdf.max()
plt.plot(cdf_normalized, color='b')
plt.hist(img.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc='upper left')
plt.show()


# Opencv均衡化：equalizeHist函数

img = cv2.imread('tree.jpg', 0)
equ = cv2.equalizeHist(img)
res = np.hstack((img, equ))
cv2.imwrite('res.jpg',res)


img = cv2.imread('tree.jpg',0)
# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
cv2.imwrite('clahe_2.jpg',cl1)