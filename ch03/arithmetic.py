import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt


src1 = cv2.imread('ch03/lenna256.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('ch03/square.bmp', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

dst1 = cv2.add(src1, src2, dtype=cv2.CV_8U)# 0, 1 부분 합해서 1부분만 출력
dst2 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0.0) # 
dst3 = cv2.subtract(src1, src2) 
dst4 = cv2.absdiff(src1, src2) 

plt.subplot(2,3,1), plt.axis('off'), plt.imshow(src1, 'gray'), plt.title('src1')
plt.subplot(2,3,2), plt.axis('off'), plt.imshow(src2, 'gray'), plt.title('src2')
plt.subplot(2,3,3), plt.axis('off'), plt.imshow(dst1, 'gray'), plt.title('add')
plt.subplot(2,3,4), plt.axis('off'), plt.imshow(dst2, 'gray'), plt.title('addWeighted')
plt.subplot(2,3,5), plt.axis('off'), plt.imshow(dst3, 'gray'), plt.title('subtract')
plt.subplot(2,3,6), plt.axis('off'), plt.imshow(dst4, 'gray'), plt.title('absdiff')
plt.show()
