# Chapter_10

## 	객체 추적과 모션 벡터

#### 배경 차분: 정적 배경 차분

배경 차분(Background Subtraction : BS)은 등록된 **배경 모델과 현재 입력 프레임과의 차영상을 이용**하여 전경 **객체를 검출**하는 방법

배경 영상을 model이라는 용어를 써서 배경 영상을 등록시켜두고 **배경 영상과 다른 부분을 찾아서** 그 부분이 새로 나타난 객체라고 판단하는 방식으로 작동

**배경과 현재 프레임의 차이가 있는 부분**을 검출

<br>



#### 배경 차분: 이동 평균 배경

이동 평균 배경 방법은 현재 프레임과 이전 프레임까지의 배경 영상에 가중치를 곱하여 영상을 갱신

수백장의 영상을 저장하는 대신 매 프레임이 들어올 때마다 평균 영상을 갱신하는 방법
$$
B
(
x
,
y
,
t
)
=
α
⋅
I
(
x
,
y
,
t
)
+
(
1
−
α
)
⋅
B
(
x
,
y
,
t
−
1
)
$$
B(x,y,t) : 갱신된 배경 영상

α : 현재 프레임에 대한 가중치

I(x,y,t) : 현재 프레임

B(x,y,t-1) : 이전 프레임까지의 배경 영상

<br>



- 이동 평균 계산을 위한 가중치 누적 함수

  cv2.accumulateWeighted(src, dst, alpha, mask=None)

  \- alpha 값은 보통 0.01

  \- 0.01은 3~4초만에 100개의 프레임이 입력되어 1

  <br>



#### MOG 배경모델

- MOG란?

  Mixture of Gaussian, GMM(Gaussian Mixture Model)을 의미

  **각 픽셀에 대해 MOG 확률 모델을 설정하여 배경과 전경을 구분**하는 방법

  영상의 각각의 픽셀 값을 배경 영상으로 정의

  미리 정의해둔 배경 영상의 각각의 픽셀마다 가우시안 모델을 정의

  **픽셀 값이 정해진된 것이 아니라 픽셀 값이 가우시안 형태를 따르는 모델로 정의**

  <br>

  

- 다양한 배경 모델 구성 방법

  **(1) Static scene**

   static scene은 배경 영상을 고정하는 것을 의미합니다.

   <br>

  **(2) Single Gaussian model**

   Single Gaussian model은 픽셀마다 가우시안 모델을 정의하겠다는 의미입니다.

   노이즈를 제거하기 위해 가우시안 블러를 한번 적용한 것과 관련된 기법입니다.

   가우시안 블러를 적용해서 차영상을 구하는 것과 비슷한 형태입니다.

   <br>

  **(3) Gaussian mixture model**

   Gaussian mixture model은 가우시안을 여러 번 적용하는 것입니다.

   예를 들어, 나뭇잎이 바람에 흔들리게 되면 (x,y)위치가 나뭇잎과 하늘이 번갈아 나타날 수 있습니다.

   이처럼 두 개의 가우시안 배경 모델을 등록시켜 놓는 형태입니다.

   <br>

  **(4) Adaptive Gaussian mixture model**

   Adaptive Gaussian mixture model은 가우시안을 몇 번 적용시킬 것인지 자동으로 판단하는 프로그램입니다.

  <br>

  

- BackgroundSubtractorMOG2 클래스 생성함수

  cv2.createBackgroundSubtractorMOG2(, history=None, varThreshold=None, detectShadows=None)



- 전면 객체 마스크 생성 함수

  cv2.BackgroundSubtractor.apply(image, fgmask=None, learningRate=None)

