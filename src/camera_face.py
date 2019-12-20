#!/usr/bin/env python 

# libraries:
import rospy
import cv2
import time
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
from std_msgs.msg import String
from std_msgs.msg import Int32
from sensor_msgs.msg import Image


class camera:
  def __init__(self):
    # create a node
    rospy.init_node('node_camera_face', anonymous=True)
    # publisher object
    self.pub = rospy.Publisher('topic_camera_face', Image, queue_size=10)
    # bridge object
    self.bridge = CvBridge()
    # classifier using haar cascade file
    self.face_classifier = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

  def callback(self, data):
    # convert img to cv2
    cv2_frame = self.bridge.imgmsg_to_cv2(data, "bgr8")
    # gray convertion
    gray_cv2_frame = cv2.cvtColor(cv2_frame, cv2.COLOR_BGR2GRAY)
    # face detection
    det_faces = self.face_classifier.detectMultiScale(gray_cv2_frame, minSize=(50, 50))   
    # draw retangle in faces
    for (x, y, largura, altura) in det_faces:	
		  # Desenho do retangulo. No final cor e largura da borda
		  cv2.rectangle(cv2_frame, (x,y), (x + largura, y + largura), (0, 0 , 255), 2)    
    # convert img to ros and pub image
    ros_frame = self.bridge.cv2_to_imgmsg(cv2_frame, "bgr8")
    self.pub.publish(ros_frame)

  def listener(self):
    # subscribe to a topic
    rospy.Subscriber('depth_camera/rgb/image_raw', Image, self.callback)  
    # simply keeps python from exiting until this node is stopped
    rospy.spin()


# main function
if __name__	== '__main__':
  try:
    cam_print = camera()  
    cam_print.listener()  
  except rospy.ROSInterruptException:
    pass			