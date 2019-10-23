# TennisBall_Detection
This code detects tennis balls and draws contours around it and displays area and radius of ball

Topic subscribed by Subscriber is "/usb_cam/image_raw"
This Topic is published by usb_cam_node in usb_cam package

Code Logic:
1) Subscribe to the topic on which the laptop camera is publishing on
2) The image datatype that we get in ROS is not compatable with OpenCV
3) So , convert it to format required by OpenCV by using a cv_bridge
4) Convert the BGR image to HSV image as HSV image has a given color in a predefined range of HUE
5) apply a yellow mask
6) find contours , contour area , smallest fitting circle for the contour
7) draw the contour and circle

How to use the code:
1)Install ROS
2)Create catkin_ws
3)In src folder create a file
4)Then clone this to that file
5)Then come back to catkin_ws folder and then run command 'catkin_make' in terminal
6)in new terminal run roscore
7)in another terminal type command :
                      'rosrun usb_cam usb_cam_node _pixel_format:=yuyv'
  This will switch on the laptop cam and message will be published 

8)In a new terminal type:
                      'rosrun ($FILE_NAME)  tennisball_detection.py'
                      

If there is an error while executing step 8, go to properties of the script file and make the programe executable


-------------------------------------------------------THANK YOU-------------------------------------------------------------------
