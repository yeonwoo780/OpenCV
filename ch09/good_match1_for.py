import sys
import numpy as np
import cv2


# 영상 불러오기
src1 = cv2.imread('ch09/graf1.png', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('ch09/graf3.png', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

# 특징점 알고리즘 객체 생성 (KAZE, AKAZE, ORB 등)
for i in (cv2.KAZE_create(), cv2.AKAZE_create(), cv2.ORB_create()):
    feature = i


    # 특징점 검출 및 기술자 계산
    kp1, desc1 = feature.detectAndCompute(src1, None)
    kp2, desc2 = feature.detectAndCompute(src2, None)

    # 특징점 매칭
    matcher = cv2.BFMatcher_create()
    # matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING) # 이진 기술자
    matches = matcher.match(desc1, desc2)

    # 좋은 매칭 결과 선별, sort 기준을 distance 값으로 설정
    matches = sorted(matches, key=lambda x: x.distance)
    good_matches = matches[:80] # 상위 80개 선별

    print(i)
    print('# of kp1:', len(kp1))
    print('# of kp2:', len(kp2))
    print('# of matches:', len(matches))
    print('# of good_matches:', len(good_matches))
    print("")
    # 특징점 매칭 결과 영상 생성
    dst = cv2.drawMatches(src1, kp1, src2, kp2, good_matches, None)

    cv2.namedWindow('dst',cv2.WINDOW_NORMAL)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()
