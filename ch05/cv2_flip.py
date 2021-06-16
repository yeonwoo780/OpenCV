import sys
import numpy as np
import cv2

src = cv2.imread('ch05/tekapo.bmp')
if src is None:
    print('Image load failed!')
    sys.exit()

for f in(-1, 0, 1):
    dst = cv2.flip(src, f , dst=None)
    cv2.imshow('dst',dst)
    cv2.moveWindow('dst', 30, 300)
    cv2.waitKey()

cv2.waitKey()
cv2.destroyAllWindows()