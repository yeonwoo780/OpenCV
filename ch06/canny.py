import sys
import numpy as np
import cv2


src = cv2.imread('ch06/building.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# dst = cv2.Canny(src, 50, 150)
dst = cv2.Canny(src, 100, 200)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
