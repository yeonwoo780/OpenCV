import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt
# 컬러 영상 불러오기
src = cv2.imread('ch03/candies.png', cv2.IMREAD_COLOR)
if src is None:
    print('Image load failed!')
    sys.exit()
b_plane, g_plane, r_plane = cv2.split(src)
# src1 = cv2.merge([r_plane, g_plane, b_plane]) # cv2는 RGB로 읽지만 plt은 BGR로 읽어서 이미지 색이 변형되기 때문에 merge를 이용해 rgb로 변경해준다 
src1 = cv2.cvtColor(src, cv2.COLOR_BGR2RGB) # src 받아와서 bgr을 rgb로 변경

# dst1 = cv2.imshow('B_plane', b_plane)
# dst2 = cv2.imshow('G_plane', g_plane)
# dst3 = cv2.imshow('R_plane', r_plane)
plt.subplot(221), plt.axis('off'), plt.imshow(src1, 'gray'), plt.title('src')
plt.subplot(222), plt.axis('off'), plt.imshow(b_plane, 'gray'), plt.title('b_plane')
plt.subplot(223), plt.axis('off'), plt.imshow(g_plane, 'gray'), plt.title('G_plane')
plt.subplot(224), plt.axis('off'), plt.imshow(r_plane, 'gray'), plt.title('R_plane')
plt.show()