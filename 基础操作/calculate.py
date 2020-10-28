from cv2 import cv2 as cv

img = cv.imread(r'image\horse-2255876.jpg')

img_ = img + 10
img_cut = img_[:5,:, 0]
img=img[:5,:,0]
print(img)

print('\n')
print(img_cut)

image_sum=(img_cut+img)
print(image_sum)