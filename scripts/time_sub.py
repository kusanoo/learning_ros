#!/usr/bin/env python
import rospy
from learning_ros.msg import Date  #changed

def callback(message):
    print("date : %d , time : %f" % (message.date,message.time) )

if __name__ == "__main__":
    rospy.init_node('time_sub')
    sub = rospy.Subscriber('Date_and_Time', Date , callback)
    rospy.spin()
