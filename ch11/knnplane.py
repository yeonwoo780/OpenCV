import numpy as np
import cv2

# 트랙바 콜백 함수
def on_k_changed(pos):
    global k_value

    k_value = pos
    if k_value < 1:
        k_value = 1

    trainAndDisplay()

# 리스트로 변환하여 train과 label에 데이터 저장
def addPoint(x, y, c):
    train.append([x, y])
    label.append([c])

# 시각화 함수
def trainAndDisplay():
    # train, label 90개의 데이터를 ndarray로 저장합니다.
    # train은 float32, label은 int32로 입력해야 합니다.
    trainData = np.array(train, dtype=np.float32)
    labelData = np.array(label, dtype=np.int32)

    # ROW_SAMPLE 인자는 데이터 하나가 한 행으로 들어가는 것을 의미
    knn.train(trainData, cv2.ml.ROW_SAMPLE, labelData)

    # 영상의 모든 픽셀을 클래스에 맞게 색칠
    h, w = img.shape[:2]
    for y in range(h):
        for x in range(w):
            sample = np.array([[x, y]]).astype(np.float32)
            
            # 모든 픽셀에 대해 몇번 클래스인지 계산합니다.
            # ret이 아닌 res를 받아오고 rest[0,0]도 가능
            ret, _, _, _ = knn.findNearest(sample, k_value)

            ret = int(ret)
            if ret == 0:
                img[y, x] = (128, 128, 255)
            elif ret == 1:
                img[y, x] = (128, 255, 128)
            elif ret == 2:
                img[y, x] = (255, 128, 128)

    # train 데이터를 원으로 시각화
    for i in range(len(train)):
        x, y = train[i]
        l = label[i][0]

        if l == 0:
            cv2.circle(img, (x, y), 5, (0, 0, 128), -1, cv2.LINE_AA)
        elif l == 1:
            cv2.circle(img, (x, y), 5, (0, 128, 0), -1, cv2.LINE_AA)
        elif l == 2:
            cv2.circle(img, (x, y), 5, (128, 0, 0), -1, cv2.LINE_AA)

    cv2.imshow('knn', img)


# 학습 데이터 & 레이블
# 2차원 평면 상에 점들을 찍고 3개의 점들로 구분.
train = []
label = []

k_value = 1 # 초기값
img = np.full((500, 500, 3), 255, np.uint8) # 컬러 영상 제작
knn = cv2.ml.KNearest_create() # KNearest 객체 생성

# 랜덤 데이터 생성
NUM = 30
rn = np.zeros((NUM, 2), np.int32) # 30행 2열, 60개

# (150, 150) 근방의 점은 0번 클래스로 설정
cv2.randn(rn, 0, 50) # 가우시안 분포를 따르는 함수
for i in range(NUM):
    addPoint(rn[i, 0] + 150, rn[i, 1] + 150, 0) # x,y 값에 150을 더함

# (350, 150) 근방의 점은 1번 클래스로 설정
cv2.randn(rn, 0, 50)
for i in range(NUM):
    addPoint(rn[i, 0] + 350, rn[i, 1] + 150, 1)

# (250, 400) 근방의 점은 2번 클래스로 설정
cv2.randn(rn, 0, 70)
for i in range(NUM):
    addPoint(rn[i, 0] + 250, rn[i, 1] + 400, 2)

# 영상 출력 창 생성 & 트랙바 생성
cv2.namedWindow('knn')
cv2.createTrackbar('k_value', 'knn', 1, 5, on_k_changed)

# KNN 결과 출력
trainAndDisplay()

cv2.waitKey()
cv2.destroyAllWindows()
