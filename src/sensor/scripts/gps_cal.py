#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import NavSatFix, Imu
import math

class ObjectGPSLocalization:
    def __init__(self):
        rospy.init_node('object_gps_localization', anonymous=True)

        # 드론의 초기 상태 변수
        self.drone_gps = None  # 드론 GPS 좌표
        self.drone_heading = None  # 드론 헤딩 방향 (IMU로부터 받아야 함)
        self.drone_altitude = 10.0  # 드론 고도 (고정값)
        self.camera_angle = 60.0  # 카메라 각도 (고정값)

        # ROS 토픽 구독
        rospy.Subscriber("/ublox/fix", NavSatFix, self.gps_callback)
        rospy.Subscriber("/imu/data", Imu, self.imu_callback)  # IMU 데이터를 받아오는 토픽 구독

        # `detect_gps` 토픽에 퍼블리시할 Publisher 생성
        self.gps_pub = rospy.Publisher('/detect_gps', NavSatFix, queue_size=10)

    def gps_callback(self, data):
        """드론의 GPS 좌표 업데이트"""
        self.drone_gps = (data.latitude, data.longitude)
        

    def imu_callback(self, data):
        """IMU 데이터를 사용하여 드론 헤딩 업데이트"""
        # 헤딩 각도 추출 (가정: IMU 데이터에서 yaw가 헤딩 방향)
        self.drone_heading = data.orientation.z  # 또는 적절한 헤딩 값 추출 방식 사용
        

    def calculate_object_gps(self, object_distance, object_angle_offset):
        """
        감지된 객체의 GPS 좌표 계산
        :param object_distance: 객체까지의 거리 (m)
        :param object_angle_offset: 카메라 중심으로부터 객체까지의 각도 오프셋 (도)
        :return: 객체 GPS 좌표 (위도, 경도)
        """
        if self.drone_gps is None or self.drone_heading is None:
            rospy.logwarn("GPS 또는 헤딩 데이터가 부족합니다.")
            return None

        # 총 각도 계산 (드론 헤딩 + 객체의 상대 각도)
        total_angle = self.drone_heading + object_angle_offset
        rospy.loginfo(f"Total Angle: {total_angle}")

        # 객체의 상대 위치 계산 (삼각함수 활용)
        delta_latitude = object_distance * math.cos(math.radians(total_angle)) / 111320
        delta_longitude = object_distance * math.sin(math.radians(total_angle)) / (
            111320 * math.cos(math.radians(self.drone_gps[0]))
        )

        # 객체 GPS 좌표 계산
        object_gps = (
            self.drone_gps[0] + delta_latitude,
            self.drone_gps[1] + delta_longitude
        )
        return object_gps

    def process_object(self, object_pixel_x, frame_width):
        """
        카메라에서 객체 픽셀 좌표를 받아 객체까지의 거리를 계산하고 GPS 좌표를 구합니다.
        :param object_pixel_x: 객체의 X축 픽셀 좌표
        :param frame_width: 카메라 프레임의 너비
        """
        # 카메라 중심으로부터의 각도 계산
        camera_fov = 90.0  # 카메라의 수평 시야각 (FOV)
        object_angle_offset = ((object_pixel_x - frame_width / 2) / frame_width) * camera_fov

        # 객체까지의 거리 계산 (삼각함수 사용)
        object_distance = self.drone_altitude / math.tan(math.radians(self.camera_angle))

        # 객체 GPS 계산
        object_gps = self.calculate_object_gps(object_distance, object_angle_offset)
        if object_gps:
            rospy.loginfo(f"객체의 GPS 좌표: {object_gps}")

            # GPS 데이터를 NavSatFix 메시지로 퍼블리시
            gps_msg = NavSatFix()
            gps_msg.latitude = object_gps[0]
            gps_msg.longitude = object_gps[1]
            gps_msg.altitude = self.drone_altitude  # 고도도 포함

            # `detect_gps` 토픽에 퍼블리시
            self.gps_pub.publish(gps_msg)
        else:
            rospy.logwarn("객체의 GPS 좌표를 계산할 수 없습니다.")

    def run(self):
        rospy.spin()


if __name__ == "__main__":
    try:
        node = ObjectGPSLocalization()
        node.run()
    except rospy.ROSInterruptException:
        pass

