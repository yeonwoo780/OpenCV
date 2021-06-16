import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt

src = cv2.imread('ch05/rose.bmp') # src.shape=(320, 480)

if src is None:
    print('Image load failed!')
    sys.exit()

dst1 = cv2.resize(src, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
dst2 = cv2.resize(src, (1920, 1280))  # cv2.INTER_LINEAR
dst3 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_CUBIC)
dst4 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_LANCZOS4)

# cv2.imshow('src', src)
# cv2.imshow('dst1', dst1[500:900, 400:800])
# cv2.imshow('dst2', dst2[500:900, 400:800])
# cv2.imshow('dst3', dst3[500:900, 400:800])
# cv2.imshow('dst4', dst4[500:900, 400:800])
# cv2.waitKey()
# cv2.destroyAllWindows()

# plt는 cv2와 달리 RGB로 받아와 RGB로 변환 필수
src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
dst1 = cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB)
dst2 = cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB)
dst3 = cv2.cvtColor(dst3, cv2.COLOR_BGR2RGB)
dst4 = cv2.cvtColor(dst4, cv2.COLOR_BGR2RGB)

plt.subplot(231), plt.axis('off'), plt.imshow(src), plt.title('src')
plt.subplot(232), plt.axis('off'), plt.imshow(dst1[500:900, 400:800]), plt.title('INTER_NEAREST')
plt.subplot(233), plt.axis('off'), plt.imshow(dst2[500:900, 400:800]), plt.title('INTER_LINEAR')
plt.subplot(234), plt.axis('off'), plt.imshow(dst3[500:900, 400:800]), plt.title('INTER_CUBIC')
plt.subplot(235), plt.axis('off'), plt.imshow(dst4[500:900, 400:800]), plt.title('INTER_LANCZOS4')
plt.show()