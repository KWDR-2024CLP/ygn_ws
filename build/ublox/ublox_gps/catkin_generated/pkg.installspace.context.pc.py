# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include".split(';') if "${prefix}/include" != "" else []
PROJECT_CATKIN_DEPENDS = "tf;roscpp;ublox_msgs;ublox_serialization;rtcm_msgs;nmea_msgs".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lublox_gps".split(';') if "-lublox_gps" != "" else []
PROJECT_NAME = "ublox_gps"
PROJECT_SPACE_DIR = "/home/l2y/ygn_ws/install"
PROJECT_VERSION = "1.5.0"
