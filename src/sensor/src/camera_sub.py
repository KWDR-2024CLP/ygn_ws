#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CameraSubscriberNode:
    def __init__(self):
        # ROS 노드 초기화
        rospy.init_node('camera_subscriber_node', anonymous=True)
        
        # CvBridge 객체 생성
        self.bridge = CvBridge()

        # 이미지 토픽 구독
        self.image_sub = rospy.Subscriber('/camera/image_raw', Image, self.image_callback)

    def image_callback(self, msg):
        try:
            # ROS 이미지 메시지를 OpenCV 이미지로 변환
            cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")

            # OpenCV를 사용해 이미지를 창에 표시
            cv2.imshow("Received Camera Image", cv_image)

            # 'q' 키를 누르면 창 종료
            if cv2.waitKey(1) & 0xFF == ord('q'):
                rospy.signal_shutdown("User pressed 'q', shutting down...")

        except Exception as e:
            rospy.logerr("Error converting image: %s" % str(e))

    def run(self):
        rospy.spin()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    camera_subscriber = CameraSubscriberNode()
    camera_subscriber.run()

