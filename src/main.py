#bismillah
import os
import random
import time
import uuid
import tarfile
import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys 
import tensorflow as tf

anc_path = os.path.join('..', 'data' , 'anchor')
face_cascade_path = "/Users/hamed/documents/obiru/env/lib/python3.11/site-packages/cv2/data/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(face_cascade_path)
video_capture = cv2. VideoCapture(0)
while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w, :]
        print(x, y, w, h)
        imgname = os.path.join(anc_path,f'{str(uuid.uuid1())}.jpg')
        cv2.imwrite(imgname,face)

    if cv2.waitKey(1) & 0xFF == ord('p'):
        imgname = os.path.join(pos_path, '{}.jpg'.format(uuid.uuid1()))
        cv2.imwrite(imgname, frame)

    #showing the frame  
    cv2.imshow('Video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(3)

video_capture.release()
cv2.destroyAllWindows()
