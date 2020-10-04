import os
import cv2

# crate list of all negative images
with open('neg.txt', 'w') as f:
    for filename in os.listdir('negative'):
        f.write('negative/' + filename + '\n')

with open('pos.txt', 'w') as f:
    for filename in os.listdir('positive'):
        img = cv2.imread('positive/' +  filename)
        f.write('positive/' + filename + ' 1 0 0 ' + str(img.shape[1]) + ' ' + str(img.shape[0]) + '\n')
