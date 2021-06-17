import sys
import numpy as np
import cv2


# 입력 영상 불러오기
src = cv2.imread('ch08/nemo.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

# 사각형 지정을 통한 초기 분할
rc = cv2.selectROI(src) # 초기 위치 지정하고 모서리 좌표 4개를 튜플값으로 반환
mask = np.zeros(src.shape[:2], np.uint8) # 마스크는 검정색으로 채워져있고 입력 영상과 동일한 크기

# 결과를 계속 업데이트 하고 싶으면 bgd, fgd 입력
cv2.grabCut(src, mask, rc, None, None, 5, cv2.GC_INIT_WITH_RECT)

# 0: cv2.GC_BGD, 2: cv2.GC_PR_BGD
# grabCut 자료에서 0,2는 배경, 1,3은 전경입니다.
# mask == 0 or mask == 2를 만족하면 0으로 설정 아니면 1로 설정합니다
mask2 = np.where((mask == 0) | (mask == 2), 0, 1).astype('uint8')
dst = src * mask2[:, :, np.newaxis]

#mask =mask *64

# 초기 분할 결과 출력
#cv2.imshow('mask', mask)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
