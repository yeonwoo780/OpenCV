# Chapter_9

## 	특징점 검출과매칭

#### 코너 검출

코너는 영상안에서 그림이 나타날 때 객체가 뾰족하게 튀어나온 부분

코너를 검출하는 이유는 코너점들이 영상에서 고유한 특징을 갖고 있어서 변별력 있게 잘 검출

But! 평탄한 영역(flat)과 에지(edge) 영역은 고유한 위치를 찾기 어렵다

코너(corner)는 변별력이 높은 편이며, 영상의 이동, 회전 변환에 강인

<br>



- 다양한 코너 검출 방법

  1. **해리스 - Harris**

     영상 내부 작은 영역이 모든 방향에 대해 변화가 큰 경우 코너로 규정

     코너 응답 함수 R을 반환 -> R(x,y)가 충분히 크면 코너로 구분

     cv2.cornerHarris() 함수 사용

     <br>

     

  2. **추적하기 좋은 특징 - Good Features to Track**

     해리스 코너 검출 방법을 기반으로 향상된 방법

     비최대 억제 수행

     코너 품질 함수를 정의 -> 가장 값이 큰 순서대로 정렬하여 반환

     cv2.goodFeaturesToTrack 함수 사용

     <br>

     

  3. **FAST - Features from Accelerated Segment Test**

     주변 16개 픽셀 값 크기를 분석

     기준 픽셀(p)보다 충분히 밝거나 또는 충분히 어두운 픽셀이 n개 연속으로 나타나면 코너로 인식(n은 보통 9)

     해리스, GFTT 방법보다 매우 빠르게 동작

     <br>

     

- 해리스 코너 응답 함수 계산

  cv2.cornerHarris(src, blockSize, ksize, k, dst=None, borderType=None)

  \- blockSize : 보통 3정도 입력합니다

  \- k : 논문에서 나온 상수이며 0.04~0.06을 입력합니다.

  \- 나머지 값은 디폴트로 지정해도 됩니다.

  <br>

  

- 추적하기 좋은 특징 코너 검출

  cv2.goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance, corners=None, mask=None, blockSize=None, useHarrisDetector=None, k=None)

  \- mindistance는 코너점이 너무 근접하게 나타나면 하나를 버립니다. 10으로 설정하면 10픽셀 근방 점들중 가장 큰거를 선택하고 나머지는 버립니다.

  \- corners는 3차원 실수 행렬(N,1,2)로 반환하며 N으 코너점 검출 갯수입니다. x 좌표는 [i, 0, 0], y좌표는 [i, 0, 1] 입니다. 실수로 저장되므로 int로 변환하여 사용해야 합니다.

  <br>

  

- FAST 코너 검출

  cv2.FastFeatureDetector_create(, threshold=None, nonmaxSuppression=None, type=None)

  \- threshold : 임계값을 50으로 설정했으면 p점보다 50더 밝거나 어두우면 코너로 판단합니다. 기본값은 10이지만 30~60 정도 설정하는 것이 좋습니다.

  \- type : 9_16은 16개 픽셀에서 9개가 밝거나 어두우면 코너로 검출하겠다는 의미

  <br>



#### 특징점 검출

- Harris, GFTT, FAST 코너의 문제점

  크기 변환에 취약하다는 단점

  <br>

  

- 특징점 검출

  고유한 특징을 나타내는 점들을 집합한 것을 특징점(feature point) or 키포인트(keypoint) or 관심점(interest point)

  특징점 주변의 부분 영상을 짤라서 특징점에 대한 특징을 기술하는 방법을 기술자(descriptor) or 특징 벡터(feature vector)

  <br>

  

- 크기 불변 특징점 검출 방법

  SIFT, KAZE, AKAZE, ORB 등 다양한 특징점 검출 방법에서 스케일 스페이스(scale-space), 이미지 피라미드(image pyramid)를 구성하여 크기 불변 특징점을 검출

  스케일 스페이스(Scale Space)는 리사이즈와 가우시안 블러링을 여러번 하는 방법

  가우시안 블러링을 통해 초점이 안맞는 가상의 영상을 만들어 완전한 코너는 아니지만 반복적으로 검출될 수 있는 점들을 검출하는 형태로 구현합니다. 대표적인게 SHIFT

  <br>

  

- OpenCV 특징점 검출 클래스: Feature2D 클래스와 파생 클래스

  cv2.KAZE_create(, ...)   

  cv2.AKAZE_create(, ...) 

  cv2.ORB_create(, ...) 

  cv2.xfeatures2d.SIFT_create(, ...) 

  <br>



- 특징점 검출함수

  cv2.Feature2D.detect(image, mask=None)

  <br>

  

- 검출된 특징점 그리기 함수

  cv2.drawKeypoints(image, keypoints, outImage, color=None, flags=None)

  <br>

  

#### 특징점 기술

- 기술자(Descriptor, feature vector)

  특징점 근방의 **부분 영상을 표현하는 실수** 또는 **이진 벡터**

  OpenCV에서는 2차원 행렬(numpy.ndarray)로 표현

  **행 개수**는 특징점 개수, **열 개수**는 특징점 기술자 알고리즘에 의해 다르게 정의

  KAZE 특징점 검출 방법으로 3159개의 특징점을 검출

  이런 경우에 행은 3159개 열은 64개

  float32 이므로 하나 당 4바이트이고 64열이므로 4 X 64 바이트가 특징점 하나를 표시하는데 필요한 데이터

  즉 4 X 64 X 3159 바이트를 차지

  <br>

  

- 실수 기술자

  기술자를 실수값으로 표현한 것

  **numpy.float32** 자료형을 사용하여 **실수 정보를 저장하는 방식**

  실수 기술자를 사용하는 알고리즘은 **SIFT**, **SURF**, **KAZE** 등

  실수 기술자는 보통 **L2 노름**(L2 norm)을 사용하여 유사도를 판단

  특징점 부근에 특징점 키포인트 객체 반환값 사이즈에 있는 멤버 변수를 이용해서 **적절한 크기의 부분영상**을 추출

  부분영상을 16X16로 분할하고 **그레디언트 방향성분**에 대한 히스토그램을 추출

  부분 영상에 대해서 각각의 작은 사각형에서 **방향 히스토그램**을 계산

  방향 히스토그램을 4X4 단위로 모아서 45도씩 8개의 방향으로 표현 4 X 4 X 8 = 128

  이처럼 **방향 성분으로 부분 영상의 특징을 기술**

  <br>

  

- 이진 기술자(Binarydescriptor)

  이진 테스트(Binary test)를 이용하여 부분 영상의 특징을 기술하는 방법

  **numpy.unit8** 자료형을 사용하여 **비트 단위로 영상 특징 정보**를 저장하는 방식

  이진 기술자를 사용하는 알고리즘은 **AKAZE**, **ORB**, **BRIEF** 등

  이진 기술자는 **해밍 거리**(Hamming distance)를 사용하여 유사도를 판단

  <br>

  특징점 주변 부분 영상을 짤라냄

  부분 영상안에서 미리 정의해둔 점을 고정시킴

  1번, 2번, 3번점 각각의 밝기를 비교

  1번과 2번 중 1번이 더 밝으면 1로 기술

  2번과 3번 중 2번이 더 어두우면 0으로 기술

  1번과 3번 중 1번이 더 밝으므로 1으로 기술

  정보를 취합하면 [1 0 1] 3비트 자료가 되는데 이 것으로 부분 영상의 특징을 기술

  기본적으로 **밝기 차이 값들을 이진수로 표현**

  <br>

  

- 특징점 기술자 계산 함수

  cv2.Feature2D.compute(image, keypoints, descriptors=None)

  <br>

  

- 특징점 검출 및 기술자 계산 함수

  cv2.Feature2D.detectAndCompute(image, mask=None, descriptors=None)

  <br>

  

#### 특징점 매칭

특징점 매칭은 두 영상에서 추출한 특징점 기술자를 비교하여 **서로 유사한 기술자를 찾는 작업**

실수 특징 벡터 : **L2 노름**(L2 norm) 사용

이진 특징 벡터 : **해밍 거리**(hamming distance) 사용

<br>

- OpenCV 특징점 매칭클래스

  match는 가장 비슷한거 1개를 매칭

  knnMatch는 비슷한거 k개를 매칭

  radiusMatch는 반경을 정해두고 반경에 들어오는 비슷한 것을 다 매칭. 갯수는 미지수

   <br>

  실제로 사용할 때는 match, knnMatch, radiusMatch를 상속받은 cv2.BFMatcher or cv2.FlannBasedMatcher를 이용

  <br>

  **cv2.BFMatcher**는 BF방법, 전수조사를 합니다.

  특징점이 많으면 시간이 오래 걸립니다.

   <br>

  **cv2.FlannBasedMatcher**는 특징점이 너무 많은 경우 근사화를 하여 조사하는 방법입니다.

  완전히 최솟값에 매칭을 못할 가능성이 있지만 속도가 빠릅니다.

  내부적으로 KD트리를 이용합니다.

  <br> 

  막상 실행해보면 둘의 속도차이는 얼마 없습니다.

   

  반환값은 **Dmatch객체**를 반환합니다.

  Dmatch는 **4개의 멤버**를 갖고 있습니다

  <br>

  

- 특징점 매칭 알고리즘 객체 생성

  cv2.BFMatcher_create(, normType=None, crossCheck=None)

  주의할 점은 실수 기술자, 이진 기술자를 쓰는 **알고리즘을 구분하여 normType인자**를 지정해줘야 한다.

  <br>

  

  cv2.DescriptorMatcher.knnmatch(queryDescriptors, trainDescriptors, k, mask=None, compactResult=None)

  <br>

  

- 특징점 매칭 결과 영상 생성

  cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches1to2, outImg,  matchColor=None, singlePointColor=None, matchesMask=None,  flags=None)



#### 좋은 매칭선별

1. **distance 값을 기준으로 정렬 후 상위 N개 선택하기**

    가장 좋은 매칭 결과에서 distance 값이 작은 것 N개를 사용하는 방법입니다.

    유사도가 높은 것이 좋은 매칭을 의미하는데 유사도가 높다는 것은 두 개의 **특징벡터의 distance 값이 작은 것**

   **cv2.DMatch.distance 값을 기준으로 내림차순 정렬 후 상위 N개를 선택**

   <br>

   

2. **가장 좋은 값과 두 번째로 좋은 값의 비율을 계산하기**

   가장 좋은 매칭 결과의 distance 값과 두 번째로 좋은 매칭 결과의 **distance 값의 비율**을 계산하는 방법

   비율의 임계값을 설정하여 **임계값보다 작으면 선택**함으로써 좋은 매칭 결과를 선별

   <br>

   

ORB 방법이 성능이 제일 떨어지지만 제일 빠릅니다.

AKAZE가 성능이 제일 좋습니다.

<br>



#### 이미지 스티칭(Image Stitching)

이미지 스티칭은 동일 장면의 사진을 자연스럽게(seamless) 붙여서 **한 장의 사진**으로 만드는 기술

여러장의 영상에서 특징점을 검출하고 **특징점이 동일한 것**들을 찾아서 두 장의 영상과의 **투시변환 관계**를 찾아내어 이어 붙임



- 이미지 스티칭 객체 생성

  cv2.Stitcher_create(, mode=None)

  <br>

  

- 이미지 스티칭함수

  cv2.Stitcher.stitch(images, pano=None)

  <br>

  
