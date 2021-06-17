# Chapter_2

## 	OpenCV-Python 기초 사용법

#### 영상의 속성과 픽셀 값 참조



#### 영상의 생성, 복사, 부분 영상 추출

img1 = np.empty((480, 640), dtype=np.uint8) # grayscale image

img2 = np.zeros((480, 640, 3), dtype=np.uint8)  # color image 

img3 = np.ones((480, 640), dtype=np.uint8) * 255 # white 

img4 = np.full((480, 640, 3), (0, 255, 255), dtype=np.uint8) # yellow



#### 마스크 연산과ROI

- ROI

  Region of Interest, 관심 영역영상에서 특정 

  연산을 수행하고자 하는 임의의 부분영역

  <br>

  

- 마스크 연산 

  OpenCV는 일부 함수에 대해 ROI 연산을 지원하며, 이때 마스크 영상을 인자로 함께 전달해야 함 (e.g.) cv2.copyTo(), cv2.calcHist(), cv2.bitwise_or(), cv2.matchTemplate(), etc. 

  마스크 영상은 cv2.CV_8UC1 타입(그레이스케일영상) 

  마스크 영상의 픽셀 값이 0이 아닌 위치에서만 연산이 수행됨 

  보통 마스크 영상으로는 0 또는 255로 구성된 이진 영상(binary image)을 사용

  <br>

  

- 마스크 연산을 지원하는 픽셀 값 복사 함수

  cv2.copyTo(src, mask, dst=None)

  <br>

  

#### OpenCV 그리기 함수

- 직선 그리기

  cv2.line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None) 

  \- pt1, pt2 : 직선의 시작점과 끝점. (x, y) 튜플

  \- thickness : 선 두께. 기본값은 1

  <br>

- 사각형 그리기

  cv2.rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None) 

  \- 사각형의 두 꼭지점 좌표 설정하기

  \- pt1, pt2 : 사각형의 두 꼭지점 좌표

  <br>

  

  cv2.rectangle(img, rec, color, thickness=None, lineType=None, shift=None) 

  \- 사각형 위치 정보 (시작점, 높이,길이)

  \- rec : 사각형 위치 정보. (x, y, w, h)

  <br>

  

- 원 그리기

  cv2.circle(img, center, radius, color, thickness=None, lineType=None, shift=None)

  \- center : 원의 중심 좌표

  <br>

  

- 다각형 그리기

  cv2.polylines(img, pts, isClosed, color, thickness=None, lineType=None, shift=None)

  \- pts : 다각형 외각 점들의 좌표 배열

  <br>

  

- 문자열 출력

  cv2.putText(img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None)

  <br>

  

#### 카메라와 동영상 처리하기 1

- 카메라 열기

  cv2.VideoCapture(index, apiPreference=None)

  <br>

  cv2.VideoCapture.open(index, apiPreference=None)

  <br>

  

- 동영상, 정지 영상 시퀀스, 비디오 스트림 열기

  cv2.VideoCapture(filename, apiPreference=None)

  <br>

  cv2.VideoCapture.open(filename, apiPreference=None)

  <br>

  

- 비디오 캡쳐가 준비되었는지 확인

  cv2.VideoCapture.isOpened()

  <br>

  

-  프레임 받아오기

  cv2.VideoCapture.read(image=None)

  <br>

  

- 카메라, 비디오 장치 속성 값 참조

  cv2.VideoCapture.get(propId)

  <br>

  cv2.VideoCapture.set(propId, value)

  <br>



#### 카메라와 동영상 처리하기 2

- 카메라와 동영상 처리하기

  Fourcc (4-문자 코드, four character code)를 지정

  \- cv2.VideoWriter_fourcc(*'DIVX')

  \- cv2.VideoWriter_fourcc(*'XVID')

  \- cv2.VideoWriter_fourcc(*'FMP4')

  \- cv2.VideoWriter_fourcc(*'X264')

  \- cv2.VideoWriter_fourcc(*'MJPG')



- 저장을 위한 동영상 파일 열기

  cv2.VideoWriter(filename, fourcc, fps, frameSize, isColor=None)

  <br>

  cv2.VideoWriter.open(filename, fourcc, fps, frameSize, isColor=None)

  <br>

  

#### 키보드 이벤트처리하기

- 키보드 입력 대기 함수

  cv2.waitKey(delay=None)



#### 마우스 이벤트처리하기

- 마우스 이벤트 콜백함수 등록 함수

  cv2.setMouseCallback(windowName, onMouse, param=None)

  <br>

  onMouse(event, x, y, flags, param)

  <br>



#### 트랙바 사용하기

- 트랙바 생성 함수

  cv2.createTrackbar(trackbarName, windowName, value, count, onChange)

  <br>

  onChange(pos) 

  <br>

  

- 연산 시간 측정 방법

  cv2.TickMeter() 

  <br>

  

#### 실전 코딩: 동영상 전환 이펙트

video_effect.py

video_dissolve_effect.py

참고
