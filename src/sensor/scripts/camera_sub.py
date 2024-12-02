#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import torch
import cv2
import numpy as np
from ultralytics import YOLO
import logging

class CameraSubscriberNode:
    def __init__(self):
        # ROS 노드 초기화
        rospy.init_node('camera_subscriber_node', anonymous=True)

        # 로그 레벨을 ERROR로 설정하여 출력되는 메시지를 최소화
        logging.basicConfig(level=logging.ERROR)

        # CvBridge 객체 생성
        self.bridge = CvBridge()

        # 모델 경로 지정
        model_path = "/home/l2y/ygn_ws/src/sensor/scripts/YGNDR.pt"

        # YOLO 모델 로드 (ultralytics 사용), verbose=False로 설정하여 텍스트 출력 비활성화
        self.model = YOLO(model_path, verbose=False)  # verbose=False 설정

        self.model.eval()  # 모델을 평가 모드로 설정

        self.camera_device = 2  

        # OpenCV를 사용하여 외부 카메라 연결
        self.cap = cv2.VideoCapture(self.camera_device)

        if not self.cap.isOpened():
            rospy.logerr("Could not open video device")
            return

        # 카메라 이미지 구독자 생성
        self.image_sub = rospy.Subscriber('/camera/image_raw', Image, self.callback)

        # 결과 출력용 OpenCV 창
        self.pub_window = "Custom Model Detection"

    def preprocess(self, frame):
        """
        모델 입력에 맞게 이미지를 전처리합니다.
        """
        # 크기 조정 및 텐서 변환
        input_image = cv2.resize(frame, (640, 640)) 
        input_image = np.transpose(input_image, (2, 0, 1)) 
        input_image = torch.tensor(input_image).float() / 255.0 
        input_image = input_image.unsqueeze(0)  
        return input_image

    def callback(self, data):
        # 카메라에서 이미지를 직접 가져옵니다
        ret, frame = self.cap.read()
        if not ret:
            rospy.logerr("Failed to capture image")
            return

        # 이미지 전처리
        input_tensor = self.preprocess(frame)

        # 모델 추론
        with torch.no_grad():
            results = self.model(input_tensor)

        # 결과 후처리 (예: 바운딩 박스 및 클래스 출력)
        for result in results:
            boxes = result.boxes.xyxy.cpu().numpy()  # [x1, y1, x2, y2]
            confidences = result.boxes.conf.cpu().numpy()  # 신뢰도
            classes = result.boxes.cls.cpu().numpy()  # 클래스

            for i, confidence in enumerate(confidences):
                if confidence > 0.5:  # 신뢰도 필터링
                    x1, y1, x2, y2 = boxes[i].astype(int)
                    class_id = int(classes[i])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f"Class {class_id}: {confidence:.2f}",
                                (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # 결과 이미지 표시
        cv2.imshow(self.pub_window, frame)
        cv2.waitKey(1)

    def run(self):
        rospy.spin()  # 노드를 계속 실행

    def __del__(self):
        self.cap.release()  # 카메라 자원 해제
        cv2.destroyAllWindows()  # 종료 시 창 닫기

if __name__ == '__main__':
    try:
        camera_subscriber = CameraSubscriberNode()
        camera_subscriber.run()
    except rospy.ROSInterruptException:
        pass

