import sys
import numpy as np
import cv2


# 그레이스케일 영상 불러오기
src = cv2.imread('ch03/lenna.bmp', cv2.IMREAD_GRAYSCALE)
#src = cv2.imread('lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.add(src, 100) # 밝기 100 
#dst = cv2.add(src, (100,100,100,0))
#dst =src +100
#dst = np.clip(src + 100., 0, 255).astype(np.uint8) (수정시)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

# 컬러 영상 불러오기
src = cv2.imread('ch03/lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.add(src, (0, 0, 100, 0)) # b,g,r + 100 씩?
#dst = np.clip(src + 100., 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
