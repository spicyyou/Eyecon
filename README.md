# 빅데이터 청년인재 고려대과정 4조 

1. 프로젝트명: C'MON(CNN based online class MONitoring System)
*수업 듣고 싶으면 드루와!! Come ON!*
2. 프로젝트 기간: 2020.07.06 ~ 2020.08.31
3. 팀원: 이다혜, 이상헌, 이지원, 이지현, 홍유진 
4. 프로젝트 개요: Convolutional Neural Network를 이용한 이미지 분석 기반의 비대면 온라인 수업 학습자 모니터링 시스템

# WHAT

포스트 코로나 시대, 비대면 강의의 질 향상을 위한 딥러닝 기반의 수업 참여도 모니터링 시스템

![image](https://user-images.githubusercontent.com/43233184/90980736-34180300-e598-11ea-8be8-88ea989a635c.png)

본 팀이 구현하는 시스템은 다음과 같이 크게 세 가지 부분으로 나눌 수 있다. 

1. 학습자 화면  

    학습자는 온라인 비대면 수업에 참여함으로써 수업을 듣는 본인의 웹캠 영상을 일정 시간 간격마다 서버에 전송하게 된다.  서버는 이미지 데이터를 받아 학습자의 수업 참여도를 산출하고, 이를 다시 학습자에게 제공하여 본인의 수업 참여 정도를 스스로 모니터링 할 수 있도록 돕는다. 

2. 딥러닝 모델을 포함하는 서버

    서버는 학습자의 이미지 데이터를 받아 딥러닝 모델을 통한 분석 과정을 거쳐서 학습자가 수업에 잘 참여하고 있는지 혹은 참여하지 않고 있는지를 판단한다.  또한 해당 수업을 수강하는 여러 학습자들의 수업 참여도를 취합한다.  

3. 교수자 화면  

    교수자는 본인의 수업을 수강하는 모든 학습자들의 수업 참여도를 한눈에 알아볼 수 있도록 시각화 된 통계자료를 제공받는다. 이를 통해 수업 난이도 조절 및 학습자의 참여 유도 등 수업의 질을 높이는 데 참고할 수 있으며 학습자에게 피드백을 전달할 수 있다.

# HOW

## Model

![image](https://user-images.githubusercontent.com/43233184/90980751-53169500-e598-11ea-80dc-94cb02115190.png)

## Web

# Repository

```
- Data
- Web
- Models 
```

# Reference

- Palmero, C., Selva, J., Bagheri, M. A., & Escalera, S. (2018). Recurrent cnn for 3d gaze estimation using appearance and shape cues. arXiv preprint arXiv:1805.03064.
- Zhang, X., Sugano, Y., Fritz, M., & Bulling, A. (2017). It's written all over your face: Full-face appearance-based gaze estimation. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition Workshops (pp. 51-60).
- Zhu, W., & Deng, H. (2017). Monocular free-head 3d gaze tracking with deep learning and geometry constraints. In Proceedings of the IEEE International Conference on Computer Vision (pp. 3143-3152).
- Krafka, K., Khosla, A., Kellnhofer, P., Kannan, H., Bhandarkar, S., Matusik, W., & Torralba, A. (2016). Eye tracking for everyone. In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 2176-2184).
- Zhang, X., Sugano, Y., Fritz, M., & Bulling, A. (2015). Appearance-based gaze estimation in the wild. In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 4511-4520).
- 김지혜. "개인 간, 개인 내에서 학습자의 학업불안과 지각된 유능성이 자기모니터링을 매개로 성취에 미치는 영향." 국내석사학위논문 한국교원대학교 대학원, 2020. 충청북도.
- 김태동, 민병아, 이원욱, 박태준, 김태공, 이중엽, ... & 김진우. (2016). 온라인 강의시청 맥락에서 사용자 주도의 컨트롤제한을 통한 인지된 비통제성이 강의 집중에 미치는 영향: 심리적반발이론을 중심으로. 한국 HCI 학회 학술대회, 15-24.
