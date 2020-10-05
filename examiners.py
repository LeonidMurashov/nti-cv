import tensorflow as tf
import cv2
import numpy as np

# use ML model to detect circle 
def examiner_ML(img_path, model, model_input_size):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    patches_coords = [[x, x + model_input_size[0], y, y + model_input_size[1]]
                   for x in range(0, img.shape[0], model_input_size[0])
                   for y in range(0, img.shape[1], model_input_size[1])]
    patches = [cv2.resize(img[c[0]:c[1], c[2]:c[3]], model_input_size) for c in patches_coords]

    predictions = model(np.array(patches)).numpy() > 0
    for i, coords in enumerate(patches_coords):
        if predictions[i]:
            return(True)

# try to make image smaller
    if img.shape[0] > model_input_size[0] or img.shape[1] > model_input_size[1]:
        img = cv2.resize(img, ( model_input_size[0], model_input_size[1]))
        prediction = model(img[np.newaxis]) > 0
        if prediction.numpy()[0][0]:
            return(True)
    return(False)        

# second method, might work when firts not
def examiner_Cascade(img_path, cascade):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    circles = cascade.detectMultiScale(gray)
    if circles.size:
        return(True)
    return(False) 
