# Chapter_5

## 	기하학적 변환

기하학적 그래픽 변환 (Geometric Graphic Transformation)

 - 영상 내 물체 간의 기하학적 관계를 변환시킴으로써, 화소의 재배치를 이루는 변환
    . 영상 객체 간의 크기,위치,방향 등 공간 관계를 바꾸는 변환
    . 크게, 크기,이동,회전 변환

    <br>
    
 - 컴퓨터 그래픽스 상의 다양한 장치들은,
    . 저마다 고유한 좌표계를 사용하는데, 이들 간의 변환에 기하학적 변환이 사용됨

    <br>
    
 - 또한, 애니메이션 내 물체 이동,보는 각도 조절 등에도 이용됨

    <br>

    

기하학적 선형 변환 (Geometric Linear Transformation)
 - 선형변환을 기하학적으로 보여주는 변환 관계
    . 컴퓨터 그래픽스 등에 많이 활용됨
    . 영상 굴곡이 발생 안함

    <br>
    
 - 유사 변환/닮음 변환/상사 변환 (Similarity Transformation) 
    . 변환 전후에, 특징(모양)이 그대로 유지됨
       .. 즉, 각이 그대로 유지되고, 정점 간의 거리가 일정 비율로 유지됨
       .. 크기는 변할 수 있으나, 모양은 변하지 않음

    . 즉, 강체 변환(Rigid Transformation)에다가, 
       .. 크기조절(Scaling), 반사(Reflection) 변환이 추가된 것

    <br>
    
 - 어파인 변환 (Affine Transformation)
    . 유사변환에 전단(Shear),차등 크기조절이 추가됨
    . 어파인 변환 전후에, 
       .. 직선은 직선, 다각형은 다각형, 곡면은 곡면, 평행 선분은 평행으로 유지됨

    <br>
    
 - 원근 변환 (Perspective Transformation)
    . 변환 전후에, 직선에서 직선으로 변환되는 정도 만 유지됨
    
    <br>

 * 어파인변환,원근변환은 엄밀하게 수학적 의미에서는 선형변환이 아님

   <br>

   

기하학적 비선형 변환 (Geometric Nonlinear Transformation)
 - 워핑(warping),모핑(morphing) 등
    . 영상 굴곡이 발생됨
    
    <br>



#### 영상의 확대와 축소

cv2.resize(src, dsize, dst=None, fx=None, fy=None, interpolation=None)

- interpolation: 보간법 지정. 기본값은cv2.INTER_LINEAR

  cv2.INTER_NEAREST : 최근방 이웃보간법

  cv2.INTER_LINEAR : 양선형 보간법 (2x2 이웃 픽셀 참조) 

  cv2.INTER_CUBIC : 3차회선 보간법 (4x4 이웃 픽셀 참조) 

  cv2.INTER_LANCZOS4 : Lanczos 보간법 (8x8 이웃 픽셀 참조) 

  cv2.INTER_AREA : 영상 축소 시 효과적

  <br>



**영상의 대칭**

- cv2.flip(src, flipCode, dst=None) 

  - flipCode

    양수 (+1) 좌우 대칭 

    0 상하 대칭

    음수 (-1) 좌우 & 상하 대칭

    <br>

    

#### 이미지 피라미드

- 하나의 영상에 대해 다양한 해상도의 영상 세트를 구성한 것

- 100 X 100 크기의 고양이를 인식한다고 가정시 입력 영상 파일은 다양한 크기로 고양이를 표현 가능하므로 여러 해상도 구간에서 고양이를 인식할 수 있도록 이미지 피라미드 생성

  <br>

  

  **이미지 피라미드 다운샘플링**

  - cv2.pyrDown(src, dst=None, dstsize=None, borderType=None)

    dstsize : default(가로, 세로 크기의 1/2로 설정)

    <br>

  

  **이미지 피라미드 업 샘플링**

  - cv2.pyrUp(src, dst=None, dstsize=None, borderType=None)

    dstsize : default(입력 영상의 가로, 세로 크기의 2배 설정)

    <br>

    

#### 영상의 회전

- cv2.getRotationMatrix2D(center, angle, scale)

  angle : (반시계 방향) 회전 각도(degree). 음수는 시계 방향

  scale : 추가적인 확대비율

  <br>



####  리매핑(remapping)

- cv2.remap(src, map1, map2, interpolation, dst=None, borderMode=None, borderValue=None)

  map1 : 결과 영상의 (x, y) 좌표가 참조할 입력 영상의 x좌표

  map2 : 결과 영상의 (x, y) 좌표가 참조할 입력 영상의 y좌표
