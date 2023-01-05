# Classification-Bottle-Cap
## Purpose.
- Webcam + YOLO V5를 활용하여 실시간으로 병뚜껑 객체 분류
- [YOLO V5란?](https://github.com/ultralytics/yolov5)

## Demo
![BottleCap-TestVideo](https://user-images.githubusercontent.com/82144756/210784153-5bae305b-3c95-4ad6-a46f-779488c598ac.gif)

## Function.
1. 정확히 일치하는 병뚜껑 객체별 분류
2. 유사 색상 병뚜껑 객체끼리 분류(ex: 칠성사이다, 스프라이트와 같은 유사 초록색 병뚜껑은 같은 병뚜껑으로 간주)

## Tech Stack.
<img src="https://img.shields.io/badge/Python 3.8-3776AB?style=for-the-badge&logo=Python&logoColor=white"><img src="https://img.shields.io/badge/opencv-5C3EE8?style=for-the-badge&logo=opencv&logoColor=black"><img src="https://img.shields.io/badge/YOLO V5-00FFFF?style=for-the-badge&logo=YOLO&logoColor=black">

## Notebook Settings.
- Hardware Accelerator: GPU
- GPU Class: Premium
- Runtime Shape: Standard

## DataSet.
- [roboflow](https://roboflow.com/) 를 활용한 Custom DataSet 제작.

## DataSet Class.
1. 티오피
2. 토레타
3. 펩시
4. 코카콜라
5. 진로토닉워터
6. 칠성사이다
7. 스프라이트
8. 스프라이트 ver2
9. 환타 - 파인애플
10. 델몬트 - 포도
11. 스파클
12. 탐사수
13. 평창수
14. 아이시스 - 분홍
15. 아이시스 - 하늘
16. 아이시스 - 파랑