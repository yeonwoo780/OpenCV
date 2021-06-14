import sys
import cv2

src = cv2.imread('ch02/opencv-logo-white.png', cv2.IMREAD_UNCHANGED)
mask = src[:,:,-1]
src = src[:,:,0:3]
dst = cv2.imread('ch02/field.bmp', cv2.IMREAD_COLOR)

if src is None or mask is None:
    print('Image load failed!')
    sys.exit()

#mask = logo[:, :, 3]    # mask는 알파 채널로 만든 마스크 영상
#logo = logo[:, :, :-1]  # logo는 b, g, r 3채널로 구성된 컬러 영상
h, w = mask.shape[:2]
crop = dst[0:h, 0:w]  # logo, mask와 같은 크기의 부분 영상 추출

cv2.copyTo(src, mask, crop)
#crop[mask > 0] = logo[mask > 0]
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()