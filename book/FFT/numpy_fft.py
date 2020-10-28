from cv2 import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

img = cv.imread('star.jpg', 0)
f = np.fft.fft2(img)
fshift = np.fft.fft2(f)
# 构建振幅图
magnitude_spectrum = 20 * np.log(np.abs(fshift))

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Source'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

# 逆变换
rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)
fshift[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Source'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(img_back)  # 此处不添加camp参数,可能与逆傅立叶变换有关
plt.title('Source'), plt.xticks([]), plt.yticks([])

plt.show()
