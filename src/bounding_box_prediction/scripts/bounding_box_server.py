#!/usr/bin/env python

import rospy
from bounding_box_prediction.srv import BoundingBoxPrediction
from sensor_msgs.msg import Image
import tensorflow as tf  
import time
from cv_bridge import CvBridge
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
sys.path.remove('/home/abdalraheem/catkin_ws_ijjeh/devel/lib/python2.7/dist-packages')


model = tf.keras.models.load_model('/home/abdalraheem/PycharmProjects/GRVC_repo/Event_based_DL_model/Trained_models/Detection_models/checkpoints/detection_model.h5')
model.summary()
bridge = CvBridge()

def handle_bounding_box_prediction(req):
    # t1 = time.time()
    cv_image = bridge.imgmsg_to_cv2(req.image, desired_encoding="mono8")
    class_pred, bbox_pred = model.predict(cv_image)
    xmin, ymin, xmax, ymax = bbox_pred[0]    
    xmin = round(xmin * 346)
    ymin = round(ymin * 260)
    xmax = round(xmax * 346)
    ymax = round(ymax * 260)
    # prediction_result = (10, 20, 30, 40)
    # xmin, ymin, xmax, ymax = 10, 20, 30, 40
    # print('time :', time.time()-t1)	
    return xmin, ymin, xmax, ymax

def bounding_box_server():
    
    rospy.init_node('bounding_box_server')	
    s = rospy.Service('predict_bounding_box', BoundingBoxPrediction, handle_bounding_box_prediction)
    print("Ready to predict bounding box.")
	
    rospy.spin()

if __name__ == "__main__":    
    bounding_box_server()
    
	
