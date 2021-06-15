import sys
import numpy as np
import cv2


src = cv2.imread('ch03/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()


# dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)

#made_functions
gmin= np.min(src)
gmax= np.max(src)
dst = ((src - gmin) * 255. / (gmax - gmin)).astype(np.uint8) #numpy사용 동일 결과



cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey()

cv2.destroyAllWindows()
