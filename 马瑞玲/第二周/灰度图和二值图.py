
# img.shape[0]：图像的垂直尺寸（高度）
# img.shape[1]：图像的水平尺寸（宽度）
# img.shape[2]：图像的通道数
#img.shape[:2] 取彩色图片的长、宽。img.shape[:3] 则取彩色图片的长、宽、通道

import numpy as np
import matplotlib.pyplot as plt
import cv2

img1 = cv2.imread("/Applications/八斗/20240901/lenna.png")
high1, wide1 = img1.shape[:2]
img2 = np.zeros([high1, wide1], img1.dtype)
for h in range(high1):
    for w in range(wide1):
        m = img1[h, w]
        img2[h, w]= int(m[0] * 0.11 + m[1] * 0.59 + m[2] * 0.3)
print("原图三色通道显示:%s" % img1)
print("灰度图单色通道显示:%s" % img2)
cv2.imshow("img1 show gray", img2)
cv2.imshow("show", img1)

#二值图
img3 = np.zeros([high1, wide1], img1.dtype)
for h in range(high1):
    for w in range(wide1):
        if img2[h, w] <= 128:
            img3[h, w] = 0
        else:
            img3[h, w] = 1

plt.imshow(img3, cmap='gray')
plt.show()
cv2.waitKey(0)
