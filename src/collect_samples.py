#we use this for collecting data for training and we do not need it currently for the ai

import cv2
import os
#import random
#import numpy as np
#import time
import uuid
#from matplotlib import pyplot as plt

# Setup paths
POS_PATH = os.path.join("..", "data", "data", "positive")
NEG_PATH = os.path.join("..", "data", "data", "negative")
ANC_PATH = os.path.join("..", "data", "data", "anchor")

'''
os.makedirs(POS_PATH)
os.makedirs(NEG_PATH)
os.makedirs(ANC_PATH)
'''

cap = cv2.VideoCapture(0)

shiftY = 350 
shiftX = 520

while cap.isOpened():
    ret, frame = cap.read()

    frame = frame[shiftY:shiftY+250, shiftX:shiftX+250, :]

    if cv2.waitKey(1) & 0XFF == ord('o'): # Press o to capture into anchor
        imgName = os.path.join(ANC_PATH, '{}.jpg'.format(uuid.uuid1()))
        cv2.imwrite(imgName, frame)
    if cv2.waitKey(1) & 0XFF == ord('p'): # Press p to capture into positive
        imgName = os.path.join(POS_PATH, '{}.jpg'.format(uuid.uuid1()))
        cv2.imwrite(imgName, frame)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

    if cv2.waitKey(1) & 0XFF == ord('w'):
        shiftY -= 10
    if cv2.waitKey(1) & 0XFF == ord('s'):
        shiftY += 10
    if cv2.waitKey(1) & 0XFF == ord('d'):
        shiftX += 10
    if cv2.waitKey(1) & 0XFF == ord('a'):
        shiftX -= 10

    cv2.imshow('Image Collection', frame)


cap.release()
cv2.destroyAllWindows()
