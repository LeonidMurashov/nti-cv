import sys
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import cv2
import numpy as np

import examiners

model_input_size = (224, 224)
model_path = 'weights/mobilenet-finetune/'
cascade_path = 'cascade_class/dataset_v1/cascade/cascade.xml'

if(len(sys.argv) < 2):
    print('Provide img path as arg1\n')
    exit()

img_path = sys.argv[1]

# import ML model
model = tf.keras.models.load_model(model_path)

if examiners.examiner_ML(img_path, model, model_input_size):
    print('kruzhok')
    exit()

# import cascade
cascade = cv2.CascadeClassifier(cascade_path)

if examiners.examiner_Cascade(img_path, cascade):
    print('kruzhok')





