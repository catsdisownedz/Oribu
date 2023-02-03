import cv2
import os
import random
import numpy as np
import time
import uuid
from matplotlib import pyplot as plt

# Functional-API
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Layer, Conv2D, Dense, MaxPooling2D, Input, Flatten
import tensorflow as tf

# Avoid OOM rrros by settign the GPU Consumption Growth
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)

# Setup paths
POS_PATH = os.path.join("data", "positive")
NEG_PATH = os.path.join("data", "negative")
ANC_PATH = os.path.join("data", "anchor")

'''
os.makedirs(POS_PATH)
os.makedirs(NEG_PATH)
os.makedirs(ANC_PATH)
'''

#cap = cv2.VideoCapture(0)
#
#shiftY = 350 
#shiftX = 520
#
#while cap.isOpened():
#    ret, frame = cap.read()
#
#    frame = frame[shiftY:shiftY+250, shiftX:shiftX+250, :]
#
#    if cv2.waitKey(1) & 0XFF == ord('a'):
#        imgName = os.path.join(ANC_PATH, '{}.jpg'.format(uuid.uuid1()))
#        cv2.imwrite(imgName, frame)
#    if cv2.waitKey(1) & 0XFF == ord('p'):
#        imgName = os.path.join(POS_PATH, '{}.jpg'.format(uuid.uuid1()))
#        cv2.imwrite(imgName, frame)
#    if cv2.waitKey(1) & 0XFF == ord('q'):
#        break
#    #if cv2.waitKey(1) & 0XFF == ord('w'):
#    #    shiftY -= 10
#    #if cv2.waitKey(1) & 0XFF == ord('s'):
#    #    shiftY += 10
#    #if cv2.waitKey(1) & 0XFF == ord('d'):
#    #    shiftX += 10
#    #if cv2.waitKey(1) & 0XFF == ord('a'):
#    #    shiftX -= 10
#    cv2.imshow('Image Collection', frame)
#
#
#cap.release()
#cv2.destroyAllWindows()


anchor = tf.data.Dataset.list_files(os.path.join(ANC_PATH, "*.jpg")).take(300)
positive = tf.data.Dataset.list_files(os.path.join(POS_PATH, "*.jpg")).take(300)
negative = tf.data.Dataset.list_files(os.path.join(NEG_PATH, "*.jpg")).take(300)

def preprocess(file_path):
    byte_img = tf.io.read_file(file_path)
    img = tf.io.decode_jpeg(byte_img)
    img = tf.image.resize(img, (105, 105))
    img = img/255.0
    return img

def preprocess_twin(input_img, validation_img, label):
    return (preprocess(input_img), preprocess(validation_img), label)

positives = tf.data.Dataset.zip((anchor, positive, tf.data.Dataset.from_tensor_slices(tf.ones(len(anchor)))))
negatives = tf.data.Dataset.zip((anchor, negative, tf.data.Dataset.from_tensor_slices(tf.ones(len(anchor)))))

data = positives.concatenate(negatives)
data = data.map(preprocess_twin)
data = data.cache()
data = data.shuffle(buffer_size=1024)

trainData = data.take(round(len(data)*.7))
trainData = trainData.batch(16)
trainData = trainData.prefetch(8)

testData = data.skip(round(len(data)*.7))
testData = data.take(round(len(data)*.3))
testData = testData.batch(16)
testData = testData.prefetch(8)

def make_embedding():
    inp = Input(shape=(105, 105, 3), name='input_image')
    c1 = Conv2D(64, (10, 10), activation='relu')(inp)
    m1 = MaxPooling2D(64, (2, 2), padding='same')(c1)

    c2 = Conv2D(128, (7, 7), activation='relu')(m1)
    m2 = MaxPooling2D(64, (2, 2), padding='same')(c2)

    c3 = Conv2D(128, (4, 4), activation='relu')(m2)
    m3 = MaxPooling2D(64, (2, 2), padding='same')(c3)

    c4 = Conv2D(256, (4, 4), activation='relu')(m3)
    f1 = Flatten()(c4)
    d1 = Dense(4096, activation='sigmoid')(f1)

    return Model(inputs=[inp], outputs=[d1], name='embedding')

embedding = make_embedding()

class L1Dist(Layer):
    def __inti__(self, **kwargs):
        super().__init__()

    def clean(self, input_embedding, validation_embedding):
        return tf.math.abs(input_embedding - validation_embedding)

l1 = L1Dist()

def make_siamese_model():
    input_image = Input(name='input_img', shape=(100, 100, 3))
    validation_image = Input(name='validation_img', shape=(100, 100, 3))

    siamese_layer = L1Dist()
    siamese_layer._name = 'distance'
    distances = siamese_layer(embedding(input_image), embedding(validation_image))

    classifier = Dense(1, activation='sigmoid')(distances)
    return Model(inputs=[input_image, validation_image], outputs=classifier, name='SiameseNetwork')

siamese_model = make_siamese_model()
print(siamese_model.summary())
