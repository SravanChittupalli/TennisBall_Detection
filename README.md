# TennisBall_Detection
This code detects tennis balls and draws contours around it and displays area and radius of ball

Topic subscribed by Subscriber is "/usb_cam/image_raw"
This Topic is published by usb_cam_node in usb_cam package

Process:
1) Subscribe to the topic on which the laptop camera is publishing on
2) The image datatype that we get in ROS is not compatable with OpenCV
3) So , convert it to format required by OpenCV by using a cv_bridge
4) Convert the BGR image to HSV image as HSV image has a given color in a predefined range of HUE
5) apply a yellow mask
6) find contours , contour area , smallest fitting circle for the contour
7) draw the contour and circle

