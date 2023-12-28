# bounding_box_detection_localizatoin
ROS package for person detection and localization

Clone the bounding_box_detection_localisation package to your env


The server node recieves the image frame from the client and use a pretrained deep learning mode to predict the bouding box around the detected person.
The client node requests the server node to predict the bounding box for a person in the image. 

The server node:
rosrun bounding_box_prediction bounding_box_server.py 


The client node:
rosrun bounding_box_prediction bounding_box_client.py 
