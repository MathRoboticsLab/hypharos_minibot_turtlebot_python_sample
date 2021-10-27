#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def laserCallback(data):
    rospy.loginfo("I heard laser scan %s", data.header.seq)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/scan", LaserScan, laserCallback)
    rospy.spin()

if __name__ == "__main__":
    listener()
