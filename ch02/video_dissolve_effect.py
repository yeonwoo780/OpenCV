import sys
import numpy as np
import cv2


# 두 개의 동영상을 열어서 cap1, cap2로 지정
# 크기 : 1280 X 720, FPS : 24
cap1 = cv2.VideoCapture('ch02/video1.mp4')
cap2 = cv2.VideoCapture('ch02/video2.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print('video open failed!')
    sys.exit()

# 두 동영상의 크기, FPS는 같다고 가정함
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS)
# 48프레임. 첫 번째 영상의 2초, 두 번째 영상의 2초를 겹쳐서 효과 줌
effect_frames = int(fps * 2)

print('frame_cnt1:', frame_cnt1)
print('frame_cnt2:', frame_cnt2)
print('FPS:', fps)

# 프레임 간 시간 간격
delay = int(1000 / fps)

# 저장을 위해 w,h,fourcc 속성 값 추출
w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 출력 동영상 객체 생성
out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

# 1번 동영상 복사
for i in range(frame_cnt1 - effect_frames):# 뒤에 2초 남겨두고 앞부분만 저장
    ret1, frame1 = cap1.read()

    if not ret1:
        print('frame read error!')
        sys.exit()

    out.write(frame1)
    print('.', end='')

    cv2.imshow('output', frame1) # 프레임1 출력
    cv2.waitKey(delay)

# 1번 동영상 뒷부분과 2번 동영상 앞부분을 합성
for i in range(effect_frames):# 48번
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        print('frame read error!')
        sys.exit()

    # 합성, 짤라내기 위한 변수, w 넓이를 48로 나눔
    dx = int(w / effect_frames) * i

    #디졸브 효과
    #과중치를 이용. cv2.addWeighted 함수 이용하면 된다.
    alpha = i / effect_frames
    frame = cv2.addWeighted(frame1, 1 - alpha, frame2, alpha, 0)

    #alpha = i / effect_frames
    #frame = cv2.addWeighted(frame1, 1 - alpha, frame2, alpha, 0)

    out.write(frame)
    print('.', end='')

    cv2.imshow('output', frame)
    cv2.waitKey(delay)

# 2번 동영상을 복사
for i in range(effect_frames, frame_cnt2):
    ret2, frame2 = cap2.read()

    if not ret2:
        print('frame read error!')
        sys.exit()

    out.write(frame2)
    print('.', end='')

    cv2.imshow('output', frame2)
    cv2.waitKey(delay)

print('\noutput.avi file is successfully generated!')

# 프레임을 받아온 후 꼭 release를 써야 한다. 사용한 자원 해제 
cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()
