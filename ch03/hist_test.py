import cv2
import sys

src = cv2.imread('ch03/field.bmp', cv2.IMREAD_COLOR)
if src is None:
    print('Image load failed!')
    sys.exit()

b_plane, g_plane, r_plane = cv2.split(src)
b_plane = cv2.equalizeHist(b_plane)
g_plane = cv2.equalizeHist(g_plane)
r_plane = cv2.equalizeHist(r_plane)

dst_rgb = cv2.merge((b_plane, g_plane, r_plane))

cv2.imshow('src', src)
cv2.imshow('dst', dst_rgb)
cv2.waitKey()
cv2.destroyAllWindows()