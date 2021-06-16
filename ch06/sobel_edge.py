import sys
import numpy as np
import cv2


src = cv2.imread('ch06/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(src, cv2.CV_32F, 0, 1)

mag = cv2.magnitude(dx, dy)
mag = np.clip(mag, 0, 255).astype(np.uint8)

# 흰색과 검은색으로만 나타내는 윤곽선 생성
dst = np.zeros(src.shape[:2], np.uint8)
dst[mag > 120] = 255 
# 120은 임계값, 값을 적절하게 설정하면 내가 원하는 부분만 나타낼 수 있음
#_, dst = cv2.threshold(mag, 120, 255, cv2.THRESH_BINARY)
# cv2 함수로 임계값 설정하기

cv2.imshow('src', src)
cv2.imshow('mag', mag)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
