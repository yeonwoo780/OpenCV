import cv2
import sys

print('Hello OpenCV', cv2.__version__)
img = cv2.imread('ch01/cat.bmp')
# img = cv2.imread('ch01/cat.bmp',cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Image load failed')
    sys.exit()

cv2.namedWindow('image') # 이름 설정 안써도 상관없음
# cv2.namedWindow('image', cv2.WINDOW_NORMAL) # 사이즈 조정 가능

cv2.imshow('image', img)
cv2.imwrite('catzz.png', img)
while True:
    if cv2.waitKey() == ord('q'):# q누르면 꺼짐
        break

cv2.waitKey()
# cv2.waitKey(3000) # 3초뒤 꺼짐

cv2.destroyAllWindows()