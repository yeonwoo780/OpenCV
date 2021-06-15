import sys
import numpy as np
import cv2


# 컬러 영상 불러오기
src = cv2.imread('ch03/candies.png', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

# 컬러 영상 속성 확인
print('src.shape:', src.shape)  # src.shape: (480, 640, 3)
print('src.dtype:', src.dtype)  # src.dtype: uint8

#HUE 색 평면 분활
src_hsb =cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
H_plane, S_plane, V_plane = cv2.split(src_hsb)
# RGB 색 평면 분할
# b_plane, g_plane, r_plane = cv2.split(src)

#b_plane = src[:, :, 0]
#g_plane = src[:, :, 1]
#r_plane = src[:, :, 2]

# cv2.imshow('src', src)
# cv2.imshow('B_plane', b_plane)
# cv2.imshow('G_plane', g_plane)
# cv2.imshow('R_plane', r_plane)

#HUE display
cv2.imshow('H_plane', H_plane)
cv2.imshow('S_plane', S_plane)
cv2.imshow('V_plane', V_plane)

cv2.waitKey()

cv2.destroyAllWindows()
