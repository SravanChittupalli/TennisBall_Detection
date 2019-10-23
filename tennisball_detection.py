#! /usr/bin/env python

import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge , CvBridgeError
from cv_bridge import CvBridge , CvBridgeError
import sys

bridge = CvBridge()
yellowLower = (30 , 120 , 10)
yellowUpper = (60 , 255 , 255)

# def threshold(gray_image):
#     threshold_image = cv2.adaptiveThreshold(gray_image , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY_INV , 13 , 0)
#     return threshold_image

def yellow_filter(cv_img):
    mask = cv2.inRange(cv_img , yellowLower , yellowUpper)
    return mask

def get_contours(mask):
    mod_img , contour , hierarchy = cv2.findContours(mask , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
    return mod_img , contour , hierarchy

def draw_contours(cv_image , mod_img , contour):
    for c in contour:
        area = cv2.contourArea(c)
        ((x, y), radius) = cv2.minEnclosingCircle(c)

        if ( area > 10000 and area < 75000 and radius < 190 ):
            cv2.drawContours(cv_image , [c] , -1 , (0 , 255,0) , 3)
            cv2.circle(cv_image, (int(x), int(y)), int(radius),(0, 255, 255), 2)
            print("{}   {}".format(area , radius))
            #cv2.imshow("FINAL_TRACKING" , cv_image)
    return cv_image

def callback(ros_image):
    global bridge
    try:
        cv_image = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    except CvBridgeError as e:
        print(e)
    #gray_image = cv2.cvtColor(cv_image , cv2.COLOR_BGR2GRAY)
    #threshold_image = threshold(gray_image)
    hsv_image = cv2.cvtColor(cv_image , cv2.COLOR_BGR2HSV)
    mask = yellow_filter(hsv_image)
    mod_img , contour , hierarchy = get_contours(mask) 
    cv_image = draw_contours(cv_image , mod_img , contour)
    cv2.imshow("CV2_IMAGE" , cv_image)
    cv2.waitKey(3)

def main(args):
    rospy.init_node("video_stream" , anonymous=True)
    rospy.Subscriber("/usb_cam/image_raw" , Image , callback)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting Down")
    cv2.destroyAllWindows()

if __name__=="__main__":
    main(sys.argv)