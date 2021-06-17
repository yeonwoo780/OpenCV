import sys
import numpy as np
import cv2


# 영상 불러오기
src1 = cv2.imread('ch09/graf1.png', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('ch09/graf3.png', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

# 특징점 알고리즘 객체 생성 (KAZE, AKAZE, ORB 등)
feature = cv2.KAZE_create()
# feature = cv2.AKAZE_create()
# feature = cv2.ORB_create()#default 500 개

# 특징점 검출 및 기술자 계산
kp1 = feature.detect(src1)
_, desc1 = feature.compute(src1, kp1)

kp2, desc2 = feature.detectAndCompute(src2, None)

print('desc1.shape:', desc1.shape) # 카제 (3159, 64) 어카제 2418,61 ORB (500,32)
print('desc1.dtype:', desc1.dtype) # 카제 float32    어카제 unit8   ORB unit8
print('desc2.shape:', desc2.shape) # 카제 (3625, 64) 어카제(2884,61 ORB (500, 32)
print('desc2.dtype:', desc2.dtype) # 카제 flot.64    어카제 unit8   ORB unit8 1바이트

# 검출된 특징점 출력 영상 생성
dst1 = cv2.drawKeypoints(src1, kp1, None,
                         flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
dst2 = cv2.drawKeypoints(src2, kp2, None,
                         flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()
