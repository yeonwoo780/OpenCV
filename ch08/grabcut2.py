import sys
import numpy as np
import cv2


# 입력 영상 불러오기
src = cv2.imread('ch08/messi5.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

# 사각형 지정을 통한 초기 분할
mask = np.zeros(src.shape[:2], np.uint8)  # 마스크
bgdModel = np.zeros((1, 65), np.float64)  # 배경 모델 무조건 1행 65열, float64
fgdModel = np.zeros((1, 65), np.float64)  # 전경 모델 무조건 1행 65열, float64

rc = cv2.selectROI(src)

# RECT는 사용자가 사각형 지정. 이 값에서 계속 업데이트
cv2.grabCut(src, mask, rc, bgdModel, fgdModel, 1, cv2.GC_INIT_WITH_RECT)

# 0: cv2.GC_BGD, 2: cv2.GC_PR_BGD
mask2 = np.where((mask == 0) | (mask == 2), 0, 1).astype('uint8')
dst = src * mask2[:, :, np.newaxis]

# 초기 분할 결과 출력
cv2.imshow('dst', dst)

# 마우스 이벤트 처리 함수 등록
def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN: # 왼쪽 버튼은 전경
        cv2.circle(dst, (x, y), 3, (255, 0, 0), -1) # 파랑색 색칠
        cv2.circle(mask, (x, y), 3, cv2.GC_FGD, -1) # 마스크에 전경 강제 지정
        cv2.imshow('dst', dst)
    elif event == cv2.EVENT_RBUTTONDOWN: # 오른쪽 버튼은 배경
        cv2.circle(dst, (x, y), 3, (0, 0, 255), -1) # 빨강색 원
        cv2.circle(mask, (x, y), 3, cv2.GC_BGD, -1) # 마스크에 배경 강제 지정
        cv2.imshow('dst', dst)
    elif event == cv2.EVENT_MOUSEMOVE:# 마우스 움직임
        if flags & cv2.EVENT_FLAG_LBUTTON: # 왼쪽 누르고 움직이면 전경
            cv2.circle(dst, (x, y), 3, (255, 0, 0), -1)
            cv2.circle(mask, (x, y), 3, cv2.GC_FGD, -1)
            cv2.imshow('dst', dst)
        elif flags & cv2.EVENT_FLAG_RBUTTON: # 오른쪽 누르고 움직이면 배경
            cv2.circle(dst, (x, y), 3, (0, 0, 255), -1)
            cv2.circle(mask, (x, y), 3, cv2.GC_BGD, -1)
            cv2.imshow('dst', dst)


cv2.setMouseCallback('dst', on_mouse)

while True:
    key = cv2.waitKey()
    if key == 13:  # ENTER
        # 사용자가 지정한 전경/배경 정보를 활용하여 영상 분할
        cv2.grabCut(src, mask, rc, bgdModel, fgdModel, 1, cv2.GC_INIT_WITH_MASK)# 마스크 초기화
        mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
        dst = src * mask2[:, :, np.newaxis]
        cv2.imshow('dst', dst)
    elif key == 27:
        break

cv2.destroyAllWindows()
