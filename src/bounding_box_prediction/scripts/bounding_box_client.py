#!/usr/bin/env python

import rospy
from bounding_box_prediction.srv import BoundingBoxPrediction
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

# import sys
# sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
# sys.path.remove('/home/abdalraheem/catkin_ws_ijjeh/devel/lib/python2.7/dist-packages')


bridge = CvBridge()

def bounding_box_client():
    rospy.wait_for_service('predict_bounding_box')
    try:
        predict_bounding_box = rospy.ServiceProxy('predict_bounding_box', BoundingBoxPrediction)
        cv_image_gray = cv2.imread('/home/abdalraheem/PycharmProjects/GRVC_repo/Event_based_DL_model/new_dataset/Day_1/1564641316222536269.png', cv2.IMREAD_GRAYSCALE)

        ros_image = bridge.cv2_to_imgmsg(cv_image_gray, encoding="mono8")

	# cv2.imshow('test', cv_image_gray)
	# cv2.waitKey(1000)
	# cv2.destroyAllWindows()
        response = predict_bounding_box(ros_image)
        print("Bounding Box Prediction Result:", response)

    except rospy.ServiceException as e:
        print("Service call failed:", e)

if __name__ == '__main__':
    rospy.init_node('bounding_box_client')
    bounding_box_client() 

