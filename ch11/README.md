# Chapter_11

## 	머신 러닝

#### OpenCV 머신 러닝클래스

| ANN_MLP               | 인공 신경망(artificial neural network) 다층 퍼셉트론(multi-layer perceptron) 입니다. 여러 개의 은닉층을 포함한 신경망을 학습시킬 수 있고, 입력 데이터에 대한 결과를 예측할 수 있습니다. |
| --------------------- | ------------------------------------------------------------ |
| DTrees                | 이진 의사 결정 트리(decision trees)알고리즘입니다. DTrees 클래스는 부스팅 알고리즘은 구현한 ml::Boost 클래스와 랜덤 트리(random tree) 알고리즘을 구현한 ml::RTree 클래스의 부모 클래스 역할을 합니다. |
| Boost                 | 부스팅(boostring) 알고리즘입니다. 다수의 약한 불류기(weak classifier)에 적절한 가중치를 부여하여 성능이 좋은 분류기를 만드는 방법입니다. |
| RTrees                | 랜덤 트리(random tree) 또는 랜덤 포레스트(random forest) 알고리즘입니다. 입력 특징 벡터를 다수의 트리로 예측하고, 그 결과를 취합하여 분류 또는 회귀를 수행합니다. |
| EM                    | 기댓값 최대화(Expectation Maximizaion)를 의미합니다. 가우시안 혼합 모델(Gaussian mixture model)을 이용한 군집화 알고리즘입니다. |
| KNearest              | k 최근접 이웃(K-Nearest Neighbors) 알고리즘입니다. K 최근접 이웃 알고리즘은 샘플 데이터와 인접한 k개의 학습 데이터를 찾고, 이 중 가장 많은 개수에 해당하는 클래스를 샘플 데이터 클래스로 지정합니다. |
| LogisticRegression    | 로지스틱 회귀(logistic regression). 이진 분류 알고리즘의 일종입니다. |
| NormalBayesClassifier | 정규 베이즈 분류기 입니다. 정규 베이즈 분류기는 각 클래스의 특징 벡터가 정규 분포를 따른다고 가정합니다. 따라서 전체 데이터 분포는 가우시안 혼합 모델로 표현 가능합니다. 정규 베이즈 분류기는 학습 데이터로부터 각 클래스의 평균 벡터와 공분산 행렬을 계산하고, 이를 예측에 사용합니다. |
| SVM                   | 서포트 벡터 머신(sipport vector machine) 알고리즘 입니다. 두 클래스의 데이터를 가장 여유있게 분리하는 초평면을 구합니다. 커널 기법을 이용하여 비선형 데이터 분류에도 사용할 수 있으며, 다중 클래스 분류 및 회귀에도 적용할 수 있습니다. |
| SVMSDG                | 통계적 그래디언트 하향(stochastic gradient descent) SVM. 통계적 그래디언트 하향 방법을 SVM에 적용함으로써 대용량 데이터에 대해서도 빠른 학습이 가능합니다. |

<br>



- 머신 러닝 알고리즘 객체 생성

  cv2.ml.~~~_create()

  <br>

  

- 머신 러닝 알고리즘 학습

  cv2.ml_StatModel.train(samples, layout, responses)

  \- samples에서 N은 데이터 개수, d는 특징벡터의 차원 개수

  \- layout 인자는 보통 cv2.ROW_SAMPLE을 입력

  \- responses는 정답 행렬을 반환

  <br>



- 머신 러닝 알고리즘 예측

  cv2.ml_StatModel.predict(samples, results=None, flags=None)

  <br>

  

#### K 최근접 이웃알고리즘(kNN, k-Nearest Neighbor)

k 최근접 이웃 알고리즘은 특징 공간에서 테스트 데이터와 가장 가까이 있는 k개의 학습 데이터를 찾아 분류 또는 회귀를 수행하는 지도 학습 알고리즘

<br>



- KNN 알고리즘 객체생성

  cv2.ml.KNearest_create()

  <br>

  

- KNN 알고리즘으로 입력 데이터의 클래스 예측

  cv.ml_KNearest.findNearest(samples, k, results=None, neighborResponses=None, dist=None , flags=None)

  <br>

  

- 예제

  knnplane.py

  <br>

  

#### k-평균 알고리즘

k-means 알고리즘은 주어진 데이터를 k 개의 구역으로 나누는 군집화(clustering) 알고리즘입니다.

**비지도 학습**이며 데이터를 무작정 입력으로 주고 임의의 기준으로 나눠주는 형태로 동작하는 알고리즘

<br>



- K-mean 군집화 함수

  cv2.kmeans(data, K, bestLabels, criteria, attempts, flags, centers=None)

  <br>

  

- 예제

  kmeans.py

  <br>
