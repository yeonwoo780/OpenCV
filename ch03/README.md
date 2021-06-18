# Chapter_3

## 	기본적인 영상 처리 기법

#### 영상의 밝기조절

화소 처리(Pointprocessing) 

입력 영상의 특정 좌표 픽셀 값을 변경하여 출력 영상의 해당 좌표 픽셀 값으로 설정하는 연산

결과 영상의 픽셀 값이 정해진 범위(e.g. 그레이스케일)에 있어야 함

반전, 밝기 조절, 명암비 조절 등

<br>

- 영상의 밝기 조절을 위한 영상의 덧셈 연산

  cv2.add(src1, src2, dst=None, mask=None, dtype=None)

  \- 참고 brightness.py

  <br>

  

#### 영상의 산술 및 논리 연산

- 가중치 합(weightedsum)

  두 영상의 같은 위치에 존재하는 픽셀 값에 대하여 가중합을 계산하여 결과 영상의 픽셀 값으로설정

  보통 𝛼 + 𝛽 = 1 이 되도록 설정 ➔ 두 입력 영상의 평균 밝기를 유지

  <br>

  

- 평균 연산(average)

  가중치를 𝛼 = 𝛽 = 0.5 로 설정한 가중치 합
  $$
  dst(x,y) = {1}/{2}(src(x,y)+src2(x,y))
  $$
  

- 가중치 합(weightedsum) 함수

  cv2.addWeighted(src1, alpha, src2, beta, gamma, dst=None, dtype=None)

  <br>

  

- 뺄셈 연산 함수

  cv2.subtract(src1, src2, dst=None, mask=None, dtype=None)

  <br>

  

- 차이 연산 함수

  cv2.absdiff(src1, src2, dst=None)

  \- 참고 arithmetic.py

  <br>

  

- 비트단위 AND, OR, XOR, NOT연산

  cv2.bitwise_and(src1, src2, dst=None, mask=None)

   cv2.bitwise_or(src1, src2, dst=None, mask=None)

  cv2.bitwise_xor(src1, src2, dst=None, mask=None)

  cv2.bitwise_not(src1, dst=None, mask=None)

  <br>



#### 컬러 영상과 색 공간

- (색상) 채널 분리

  cv2.split(m, mv=None)

  <br>

  

- (색상) 채널 결합

  cv2.merge(mv, dst=None)

  \-  참고 color.py



- 색 공간변환

  영상 처리에서는 특정한 목적을 위해 RGB 색 공간을 HSV, YCrCb, Grayscale 등의 다른 색 공간으로 변환하여 처리

  <br>

  

- 색 공간 변환 함수

  cv2.cvtColor(src, code, dst=None, dstCn=None)

  \- cv2.COLOR_BGR2GRAY / cv2.COLOR_GRAY2BGR  

  \- cv2.COLOR_BGR2RGB / cv2.COLOR_RGB2BGR 

  \- cv2.COLOR_BGR2HSV / cv2.COLOR_HSV2BGR

  \- cv2.COLOR_BGR2YCrCb / cv2.COLOR_YCrCb2BGR

  <br>

  

- HSV 색 공간

  Hue: 색상, 색의 종류 # 0 ~ 179

  Saturation: 채도, 색의 탁하고 선명한 정도 0 ~ 255

  Value: 명도, 빛의 밝기  0 ~ 255

  <br>

  

- YCrCb 색 공간

  PAL, NTSC, SECAM 등의 컬러 비디오 표준에 사용되는 색 공간

  영상의 밝기 정보와 색상 정보를 따로 분리하여 부호화 (흑백 TV 호환)

  0 ≤ 𝑌 ≤255

  0 ≤ 𝐶𝑟 ≤ 255

  0 ≤ 𝐶𝑏 ≤ 255

  <br>



#### **히스토그램 분석**

- 히스토그램(Histogram)

  영상의 픽셀 값 분포를 그래프의 형태로 표현

  예를 들어 그레이스케일 영상에서 각 그레이스케일 값에 해당하는 픽셀의 개수를 구하고, 이를 막대 그래프의 형태로 표현

  <br>

- 정규화된 히스토그램(Normalizedhistogram)

  각 픽셀의 개수를 영상 전체 픽셀 개수로 나누어준 것

  해당 그레이스케일 값을 갖는 픽셀이 나타날 확률

  <br>

  

-  히스토그램 구하기

  cv2.calcHist(images, channels, mask, histSize, ranges, hist=None, accumulate=None)

  \- 참고 histogram1.py

  \- 참고 histogram2.py

  <br>



#### 영상의 명암비조절

- 명암비

  밝은 곳과 어두운 곳 사이에 드러나는 밝기 정도의 차이

  <br>

  

- 기본적인 명암비 조절 예제

  contrast1.py

  <br>

  

- 히스토그램 스트레칭(Histogramstretching)

  영상의 히스토그램이 그레이스케일 전 구간에서 걸쳐 나타나도록 변경하는 선형 변환기법

  <br>

  

- 정규화 함수

  cv2.normalize(src, dst, alpha=None, beta=None, norm_type=None, dtype=None,  mask=None)

  \- 참고 contrast2.py

  <br>



#### 히스토그램 평활화

- 히스토그램 평활화(Histogramequalization)

  히스토그램이 그레이스케일 전체 구간에서 균일한 분포로 나타나도록 변경하는 명암비 향상기법

  히스토그램 균등화, 균일화,평탄화

  <br>

  

- 히스토그램 평활화를 위한 함수

  cv2.equalizeHist(src, dst=None) 

  \-  equalize.py

  <br>

  

-  컬러 히스토그램평활화

  \- equalize.py

  <br>



#### 특정 색상 영역 추출

\- 참고 inrange1.py

- 특정 범위 안에 있는 행렬 원소 검출

  cv2.inRange(src, lowerb, upperb, dst=None)

  \- inrange2.py

  <br>

####  실전 코딩: 크로마 키 합성

\- chroma_key.py







