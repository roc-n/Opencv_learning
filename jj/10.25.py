import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt



img= cv2.imread('../image/FrontGround.jpg')
img = cv2.resize(img,(800,800))
orgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
mask = np.zeros(img.shape[:2],np.uint8)  # 制作黑色遮罩
bgd = np.zeros((1,65),np.float64)
fgd = np.zeros((1,65),np.float64)
rect = (70,94,631,660)
mask3 = cv2.grabCut(img,mask,rect,bgd,fgd,5,cv2.GC_INIT_WITH_RECT)[0]  # 缺少会导致边缘有缺损，矩阵模式
# mask6 = np.where((mask==2)|(mask==0),0,1).astype('uint8')  # 如果图像中像素为2或0，则将其改0，否则改为1，
# img = img*mask6[:,:,np.newaxis]
# cv2.imwrite('../image/newmask.jpg',img)

plt.subplot(221)
plt.imshow(mask3)
plt.axis('off')

mask2 = cv2.imread('../image/newmask.jpg',0)
mask2 = cv2.resize(mask2,(800,800))
# mask2Show = cv2.imread('../image/newmask.jpg',-1)
# mask2Show = cv2.resize(mask2Show,(800,800))
# m2rgb=cv2.cvtColor(mask2Show,cv2.COLOR_BGR2RGB)
mask[mask2 == 0] = 0     # 颜色映射 ，人工遮罩后的图片中被遮罩的部分 映射到 原图上，对原图进行遮罩
mask[mask2 == 255] = 1   # 这里使用自定义模板

plt.subplot(222)
plt.imshow(mask3)
plt.axis('off')

mask, bgd, fgd = cv2.grabCut(img,mask,None,bgd,fgd,2,cv2.GC_INIT_WITH_MASK)  # 蒙版模式，去掉被画上黑色的区域
plt.subplot(223)
plt.imshow(mask3)
plt.axis('off')

mask = np.where((mask==2)|(mask==0),0,1).astype('uint8')
ogc = img*mask[:,:,np.newaxis]
ogc=cv2.cvtColor(ogc,cv2.COLOR_BGR2RGB)
# plt.subplot(121)
# plt.imshow(m2rgb)
# plt.axis('off')
plt.subplot(224)
plt.imshow(ogc)
plt.axis('off')
plt.show()


pointImg = cv2.imread("../image/blocks.jpg")
pointImg = cv2.resize(pointImg,(800,800))
gray = cv2.cvtColor(pointImg,cv2.COLOR_BGR2GRAY)

# 通过显示设定数量的优先点，来达到精确捕捉角点，但是准确度不如下面的方法
# corners = cv2.goodFeaturesToTrack(gray,84,0.01,10)
# for i in corners:
#     x,y = i.ravel()
#     cv2.circle(pointImg,(x,y),3,255,-1)
# plt.imshow(pointImg),plt.show()

kernel = np.ones((5,5),np.uint8)
cv2.imshow('gray2',gray)
gray = cv2.erode(gray,kernel,2)  # 通过腐蚀运算填补黑块内部的白色空隙
cv2.imshow('gray1',gray)
gray = cv2.threshold(gray,90,255,cv2.THRESH_BINARY)[1]  # 设置过滤无关边界内容
gray = cv2.GaussianBlur(gray,(3,3),0)  # 使图像模糊，便于减少无关图像干扰

gray = np.float32(gray)

dst = cv2.cornerHarris(gray,2,3,0.04)  # 找到Harris角点
dst = cv2.dilate(dst,None)  # 膨胀操作
ret, dst = cv2.threshold(dst,0.01*dst.max(), 255, 0)  # 二值化，除去不相关图像
dst = cv2.GaussianBlur(dst,(3,3),0)  # 使图像模糊，便于减少无关图像干扰
dst = np.uint8(dst)


centroids = cv2.connectedComponentsWithStats(dst)[3]  # 寻找连通区域
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)  # 设置终止条件，迭代30次或移动0.001
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria) # cv2.cornerSubPix（）检测十分精细，但不便于显示

res = np.hstack((centroids,corners))
res = np.int0(res)
# cv2.cornerHarris检测出的角点，粗略
pointImg[dst>0.1012*dst.max()] = [0,0,255]
# cv2.cornerSubPix检测出的角点，精确
pointImg[res[:,1],res[:,0]] = [0,0,255]
# 绿色点为修正点
pointImg[res[:,3],res[:,2]] = [0,255,0]

cv2.imshow('dst2',pointImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
