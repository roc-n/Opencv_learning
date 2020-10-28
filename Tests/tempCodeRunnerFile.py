newMask = cv.imread('image/mess_mask.png', 0)
mask[newMask == 0] = 0
mask[newMask == 255] = 1