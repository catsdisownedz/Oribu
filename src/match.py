#runs through the entire dataset and compares the anchor with the images stored:
# returns 1 if the anchor matches with a face in the criminal folder 
# returns 0 if the anchor if there is no match with anyone in the folder

import os
import time
from notif.sms.sms import notify

anc_path = os.path.join("..", "data", "anchor")

def preprocess(file_path):
    byte_img = tf.io.read_file(file_path)
    img = tf.io.decode_jpeg(byte_img)
    img = tf.image.resize(img, (105, 105))
    img = img/255.0
    return img

def check_face(file):
    img = preprocess(file)



while True:
    for file in os.listdir(anc_path):
        img_path = os.path.join(anc_path, file)
        res, name = check_face(img_path)
        print("Result: " + str(res))
        print("Name: " + name)
        print("")
        if res:
            #notify(name)
            print("Sending")
        os.remove(img_path)
