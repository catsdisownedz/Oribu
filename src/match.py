#import os
#import time
#
#anc_path = os.path.join("..", "data", "anchor")
#
#def preprocess(file_path):
#    byte_img = tf.io.read_file(file_path)
#    img = tf.io.decode_jpeg(byte_img)
#    img = tf.image.resize(img, (105, 105))
#    img = img/255.0
#    return img
#
#def check_face(file):
#    img = preprocess(file)
#
#
#while True:
#    for file in os.listdir(anc_path):
#        pass

from sms import notify

notify("DF")
