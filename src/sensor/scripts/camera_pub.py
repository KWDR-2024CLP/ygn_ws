#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CameraPublisherNode:
    def __init__(self):
        # ROS 노드 초기화
        rospy.init_node('camera_publisher_node', anonymous=True)
        
        # CvBridge 객체 생성
        self.bridge = CvBridge()

        # 카메라 이미지 퍼블리셔 생성
        self.image_pub = rospy.Publisher('/camera/image_raw', Image, queue_size=10)

        # OpenCV로 카메라 캡처 (웹캠 사용, 0번 디바이스)
        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            rospy.logerr("Cannot open camera")
            rospy.signal_shutdown("Unable to open camera")

    def run(self):
        rate = rospy.Rate(10)  # 10Hz로 퍼블리시
        while not rospy.is_shutdown():
            ret, frame = self.cap.read()
            if not ret:
                rospy.logerr("Failed to capture image")
                continue

            # OpenCV 이미지를 ROS 이미지로 변환
            image_msg = self.bridge.cv2_to_imgmsg(frame, "bgr8")

            # ROS 이미지 퍼블리시
            self.image_pub.publish(image_msg)

            rate.sleep()

        self.cap.release()

if __name__ == '__main__':
    try:
        camera_publisher = CameraPublisherNode()
        camera_publisher.run()
    except rospy.ROSInterruptException:
        pass

