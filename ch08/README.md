# Chapter_8

## 	영상 분할과 객체 검출

#### 그래프 컷(graph cut)

[개념 링크](https://seonghyeon-drew.tistory.com/7)

- Segmentatian

  이미지를 세분화한다는 것은 이미지에 있는 픽셀들을 군집화하겠다는 의미
  
  <br>
  
- 분수령 알고리즘 (Watershed algorithm)

  이미지의 픽셀 하나하나를 높이라고 생각해보자. 

  그러면 이미지를 조감도의 형태로 볼 수 있을 것이다. 

  일반적으로 이미지의 픽셀은 부드럽게 표현된다. 

  그 이유는 인접한 픽셀끼리 값의 차이가 대부분 크게 나지 않기 때문이다.

  급격한 변화를 보이는 부분은 대체로 테두리의 역할을 한다. 

  어찌됏든 이미지를 조감도로 보고 그 이미지에서 가장 낮은 부분 (극소점)들을 찾고 그곳에다가 각자 다른 색깔의 물을 붓는다고 생각해보자. 

  처음에는 각자 다른 색깔의 물 웅덩이가 생기지만 그 웅덩이를 나누는 산맥까지 물이 차오르면 서로 다른 물 웅덩이가 섞이게 되는 시점이 생기게 된다. 

  바로 그 부분이 이미지 구역을 나누는 경계선으로 정의하는 것이 분수령 알고리즘이다.

  <br>

- 그래프 컷(Graph cut)

  이번에는 이미지를 그래프라고 생각해보자. 각각의 픽셀을 정점으로 정의하고 간선을 유사도라고 생각하면 그리드 또는 매쉬라고 부르는 형태의 그래프로 생각해볼 수 있다. 그리고 그래프에서 유명한 최대 유량 알고리즘을 이용하여 정점을 두 집합으로 나누는 것이 이 알고리즘이다.

  <br>

- 그랩컷 함수

  cv2.grabCut(img, mask, rect, bgdModel, fgdModel, iterCount, mode=None)

  mask: 입출력 마스크. cv2.GC_BGD(0), cv2.GC_FGD(1),cv2.GC_PR_BGD(2),  cv2.GC_PR_FGD(3) 네 개의 값으로 구성됨.  cv2.GC_INIT_WITH_RECT 모드로 초기화.

  <br>

#### HOG 보행자 검출

- HOG(Histogram of Oriented Gradients)

  영상의 지역적 그래디언트 방향 정보를 특징 벡터로 사용
  
  <br>
  
- HOG 알고리즘

  임의의 크기의 사각형을 정의해서 부분 영상을 추출

  추출한 부분 영상의 크기를 정규화 합니다. (64X128)

  64X128 영상을 8X8 크기의 셀(cell)로 분할

  각 셀마다 방향과 크기 성분을 이용하여 방향 히스토그램을 계산

  각각의 셀에서 방향 성분을 9개로 구분하여 9가지 방향에 대한 히스토그램을 생성(180도를 20도씩 9가지 방향, 대칭하면 360도)

  <br>

- 블록 히스토그램 구하기

  8X8 셀 4개를 하나의 블록으로 지정

  즉, 블록 하나의 크기는 16X16

  8픽셀 단위로 이동합니다. (stride = 8)

  각 블록의 히스토그램 빈(bin) 개수는 4X9 = 36

  하나의 부분 영상 패치에서의 특징 백터 크기는 7 X 15 X 36 = 3780

  <br>

- OpenCV에서 HOG 보행자 검출 알고리즘 사용하기

  1. **HOG 기술자 객체 생성 및 보행자 검출을 위해 학습된 분류기 계수 불러오기**

     cv2.HOGDescriptor()

     cv2.HOGDescriptor_getDefaultPeopleDetector() 

     <br>

     

  2. **SVM 분류기 계수 등록하기**

     cv2.HOGDescriptor.setSVMDetector(svmdetector)

     <br>

     

  3.  **HOG 멀티스케일 객체 검출 함수**

     cv2.HOGDescriptor.detectMultiScale(img, hitThreshold=None, winStride=None,  padding=None, scale=None, finalThreshold=None,  useMeanshiftGrouping=None)

