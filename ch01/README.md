# Chapter_1

## 	OpenCV-Python 시작

영상이란? 픽셀이 바둑판 모양의 격자에 나열되어 있는 형태(2차원 행렬)



영상의 표현 방법

- grayscale

  밝기정보만 256단계로 구성(흑백사진 생각)

  

- truecolor

  다양한 색상 표현

  R,G,B색 성분을 256 단계로 표현



영상 데이터의 크기

- 그레이스 케일 영상 : (가로크기) X (세로크기)Bytes
- 트루컬러 영상 : (가로크기) X (세로크기) X 3 Bytes



영상 파일형식의 특징

- BMP

  픽셀 데이터를 압축하지 않고 그대로 저장

  파일 용량이 큰 편

  파일 구조가 단순해서 별도의 라이브러리 도움 없이 파일 입출력 프로그래밍 가능

  

- JPG

  주로 사진과 같은 컬러 영상을 저장

  손실 압축(lossycompression)

  압축률이 좋아서 파일 용량이 크게 감소

  디지털 카메라 사진 포맷으로 주로 사용

  

- GIF

  256 색상 이하의 영상을 저장

  일반 사진을 저장 시 화질 열화가 심함

  무손실 압축(losslesscompression)

  움직이는 GIF지원

  

- PNG

  Portable Network Graphics

  무손실 압축 (컬러 영상도 무손실 압축)

  알파 채널(투명도)을지원



영상 파일불러오기

- cv2.IMREAD_COLOR

  BGR 컬러영상으로 읽기(기본값)

  shape = (rows, cols, 3)

  

- cv2.IMREAD_GRAYSCALE

  그레이스케일 영상으로 읽기

  shape = (rows, cols)

  

- cv2.IMREAD_UNCHANGED

  영상 파일 속성 그대로 읽기

  ex) 투명한 PNG 파일: shape = (rows, cols,4)



matplotlib을 이용한 영상 출력

```python
# 컬러 영상 출력
imgBGR = cv2.imread('ch01/cat.bmp')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB) # plt 처리위한 RGB처리

plt.axis('off')
plt.imshow(imgRGB)
plt.show()

# 그레이스케일 영상 출력
imgGray = cv2.imread('ch01/cat.bmp', cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.show()

# 두 개의 영상을 함께 출력
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray')
plt.show()
```

위처럼 반드시 plt출력시 RGB값으로 변경 필수
