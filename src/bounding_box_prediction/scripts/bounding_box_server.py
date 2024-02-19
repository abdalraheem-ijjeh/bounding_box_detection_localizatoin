#!/usr/bin/env python3

import rospy
from bounding_box_prediction.srv import BoundingBoxPrediction
from sensor_msgs.msg import Image
import tensorflow as tf  
from keras.models import load_model
import time
from cv_bridge import CvBridge
import sys
import cv2
import numpy as np


tf.config.set_visible_devices([], 'GPU')

# sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
# sys.path.remove('/home/abdalraheem/catkin_ws_ijjeh/devel/lib/python2.7/dist-packages')


model = load_model('/home/abdalraheem/catkin_ws/src/bounding_box_prediction/dl_models/detection_model.h5')
model.summary()

bridge = CvBridge()

def handle_bounding_box_prediction(req):
    cv_image = bridge.imgmsg_to_cv2(req.image, desired_encoding="mono8")
    cv_image = cv2.resize(cv_image, (346,260))
    # cv2.imshow('test', cv_image)
    # cv2.waitKey(2000)
    # cv2.destroyAllWindows()
    cv_image = np.expand_dims(cv_image, axis=-1)
    cv_image = np.expand_dims(cv_image, axis=0)
    class_pred, bbox_pred = model.predict(cv_image)
    xmin, ymin, xmax, ymax = bbox_pred[0]    
    xmin = round(xmin * 346)
    ymin = round(ymin * 260)
    xmax = round(xmax * 346)
    ymax = round(ymax * 260)
    return xmin, ymin, xmax, ymax

def bounding_box_server():
    
    rospy.init_node('bounding_box_server')	
    s = rospy.Service('predict_bounding_box', BoundingBoxPrediction, handle_bounding_box_prediction)
    print("Ready to predict bounding box.")
	
    rospy.spin()

if __name__ == "__main__":    
    bounding_box_server()
    
	
