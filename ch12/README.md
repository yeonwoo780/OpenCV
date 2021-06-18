# Chapter_12

## 	딥러닝

#### OpenCV DNN 모듈

- 네트워크 불러오기

  cv2.dnn.readNet(model, config=None, framework=None)

  <br>

  

-  네트워크 입력블롭(blob) 만들기

  cv2.dnn.blobFromImage(image, scalefactor=None, size=None, mean=None, swapRB=None, crop=None, ddepth=None)

  <br>

  

- 네트워크 입력설정하기

  cv2.dnn_Net.setInput(blob, name=None, scalefactor=None, mean=None)

  <br>

  

- 네트워크 순방향 실행 (추론)

  cv2.dnn_Net.forward(outputName=None) 

  cv2.dnn_Net.f orward(outputNames=None, outputBlobs=None)

  <br>

