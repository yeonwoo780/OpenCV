import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt

img_names = ['ch09/img1.jpg', 'ch09/img2.jpg', 'ch09/img3.jpg']

imgs = []
i = 0
for name in img_names:
    img = cv2.imread(name)
    i += 1
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    if img is None:
        print('Image load failed!')
        sys.exit()

    plt.imshow(img1)
    plt.show()
    imgs.append(img)

stitcher = cv2.Stitcher_create()
status, dst = stitcher.stitch(imgs)

if status != cv2.Stitcher_OK:
    print('Stitch failed!')
    sys.exit()

cv2.imwrite('ch09/output.jpg', dst)

cv2.namedWindow('dst', cv2.WINDOW_NORMAL)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
