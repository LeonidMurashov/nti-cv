import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
import tensorflow as tf
import cv2
import sys

model_input_size = (224, 224)
model_path = 'weights/mobilenet-finetune/'

if len(sys.argv) < 2:
    print('Provide img path as arg1\n')
    exit(1)

img_path = sys.argv[1]

# Load classifier
model = tf.keras.models.load_model(model_path)

img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# Crop angles of 100x100 and enchance them
padding = 100
angles = [img[:padding, :padding], img[-padding:, :padding], 
          img[:padding, -padding:], img[-padding:, -padding:]]
angles = [cv2.resize(angle, model_input_size) for angle in angles]

# Slice image in patches
patches_coords = [[x, x + model_input_size[0], y, y + model_input_size[1]]
                   for x in range(0, img.shape[0], model_input_size[0])
                   for y in range(0, img.shape[1], model_input_size[1])]
patches = [cv2.resize(img[c[0]:c[1], c[2]:c[3]], model_input_size) for c in patches_coords]


# Check sing on every segment
result_patches = (model(np.array(patches)).numpy() > 0).any()

# Check sign in angles up-close
result_angles = (model(np.array(angles)).numpy() > 0).any()

# Check giant sign on whole image
result_whole = model(cv2.resize(img, model_input_size)[np.newaxis])[0][0].numpy() > 0

# Combine them
result = result_patches or result_angles or result_whole

print(result_patches, result_angles, result_whole)

if result:
	print('kruzhok')
