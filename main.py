#bismillah
#needed for comparision
import os
import random
import uuid
import tarfile
import numpy as np
import matplotlib.pyplot as plt
#the ones we need for facial cascade
import cv2
import sys 
import tensorflow as tf

#creating folders for images
pos_path = os.path.join('data' , 'positive')
neg_path = os.path.join('data' , 'negative')
anc_path = os.path.join('data' , 'anchor')

#file = tarfile.open('lfw.tgz')
#file.extractall('./lfw')
#file.close
#moving all pics from lfw file to neg
#for directory in os.listdir('lfw'):
'''
for file in os.listdir(os.path.join('lfw', directory)):
        ex_path = os.path.join('lfw', directory, file)
        new_path = os.path.join(neg_path, file)
        os.replace(ex_path, new_path)
'''

#face recognition from webcam
#cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(r"C:\Users\nadam\Downloads\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml")
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
            flags=cv2.CASCADE_SCALE_IMAGE
        )
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (44 , 250 , 120 ), 1)
    #captures images in video for comparision
    if cv2.waitKey(1) & 0xFF == ord('a'):
        imgname = os.path.join(anc_path, '{}.jpg'.format(uuid.uuid1()))
        cv2.imwrite(imgname, frame)
    if cv2.waitKey(1) & 0xFF == ord('p'):
        imgname = os.path.join(pos_path, '{}.jpg'.format(uuid.uuid1()))
        cv2.imwrite(imgname, frame)

    #showing the frame  
    cv2.imshow('Video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()

anchor = tf.data.Dataset.list_files(anc_path+'\*.jpg').take(300)
positive = tf.data.Dataset.list_files(pos_path+'\*.jpg').take(300)
negative = tf.data.Dataset.list_files(neg_path+'\*.jpg').take(300)

dir_test = anchor.as_numpy_iterator()
dir_test.next()
#dont forget scale factor

#reads in image from file, loads image
def preprocess(file_path):
    byte_img = tf.io.read_file(file_path)
    img = tf.decode_jpeg(byte_img)
    #resizes it (200x200x3), rescales it (between 0 & 1)
    img = tf.image.resize(img , (200,200))
    img = img / 255
    return img

img = preprocess()


positives = tf.data.Dataset.zip((anchor, positive, tf.data.Dataset.from_tensor_slices(tf.ones_like(len(anchor)))))
negatives = tf.data.Dataset.zip((anchor, negative, tf.data.Dataset.from_tensor_slices(tf.zeros_like(len(anchor)))))
data = positives.concatenate(negatives)
samples = data.as_numpy_iterator()
samples.next()

def preprocess_twin(input_img, val_img, label):
    return (preprocess(input_img), preprocess(val_img), label)

#data loader pipeline
data = data.map(preprocess_twin)
data = data.cache()
data = data.shuffle(buffer_size = 1024)

#training data
train_data = data.take(round(len(data)*.7))
train_data = train_data.batch(16)
train_data = train_data.prefetch(8)

#test data
test_data = data.skip(round(len(data)*.7))
test_data = data.take(round(len(data)*.3))
test_data = train_data.batch(16)
test_data = train_data.prefetch(8)


#criminal identification

#alert
#hamed was here (testing)
