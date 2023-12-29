# bounding_box_detection_localizatoin
ROS package for person detection and localization

Clone the bounding_box_detection_localisation package to your env


The service is "predict_bounding_box".

The server node receives the image frame from the client and uses a pre-trained deep-learning model to detect and localise the person using a bounding box.

The client node requests the server node to predict the bounding box for a person in the image. 

The server node:
rosrun bounding_box_prediction bounding_box_server.py 


The client node:
rosrun bounding_box_prediction bounding_box_client.py 
