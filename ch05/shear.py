import sys
import numpy as np
import cv2


src = cv2.imread('ch05/tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

aff = np.array([[1, 0.5, 0],
                [0, 1, 0]], dtype=np.float32) # 2 X 3 행렬

h, w = src.shape[:2]
# dst = cv2.warpAffine(src, aff, (0, 0))
# 짤림
dst = cv2.warpAffine(src, aff, (w + int(h * 0.5), h))
# 전단 변환 비율 0.5를 세로크기에 곱한 결과 값을 가로크기에 더함

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
