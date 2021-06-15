import sys
import numpy as np
import cv2

src = cv2.imread('ch04/rose.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
#정수계산 dst1
blr = cv2.GaussianBlur(src, (0, 0), 2)
dst1 = np.clip(2.0*src - blr, 0, 255).astype(np.uint8)

#실수 계산 dst2
src_f = src_ycrcb[:, :, 0].astype(np.float32) #여기서 실수로 바꿔줌
blr = cv2.GaussianBlur(src_f, (0, 0), 2.0)
src_ycrcb[:, :, 0] = np.clip(2. * src_f - blr, 0, 255).astype(np.uint8)
dst2 = cv2.cvtColor(src_ycrcb, cv2.COLOR_YCrCb2BGR)

#원본 src
cv2.imshow('src', src)
cv2.moveWindow('src', 50, 50)
cv2.imshow('dst1', dst1)
cv2.moveWindow('dst1', 100, 500)
cv2.imshow('dst2', dst2)
cv2.moveWindow('dst2', 700, 500)
cv2.waitKey()
cv2.destroyAllWindows()