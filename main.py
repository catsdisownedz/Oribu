#bismillah
import numpy as np
import matplotlib.pyplot as plt
#the ones we need for facial cascade
import cv2
import sys 

#face recognition from webcam
cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2. VideoCapture(0)
#capturing frame by frame 
while True:
    ret, frame = video_capture.read()
#turning into grayscale and making a rectangle appear around face 
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )
for (x, y, w, h) in faces:
  cv2.rectangle(frame, (x, y), (x+w, y+h), (44 , 250 , 120 ), 2)
 #showing the frame  
 cv2.imshow('Video', frame)
  
  
#dont forget scale factor

#criminal identification

#alert
#hamed was here (testing)
