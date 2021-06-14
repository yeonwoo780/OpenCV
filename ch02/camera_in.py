import sys
import cv2


# 카메라 열기
cap = cv2.VideoCapture(0) # 기본 카메라 열기

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

# 카메라 프레임 크기 출력
print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# 카메라 프레임 처리
while True:
    ret, frame = cap.read() # ret에는 True, frame에는 해당 프레임이 저장

    if not ret:
        break

    inversed = ~frame  # 반전

    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)

    if cv2.waitKey(10) == 27: # 10초 기다린후 다음 처리
        break

cap.release()
cv2.destroyAllWindows()
