import os
import cv2

path_dir = 'cutted_negatives/'

for image in os.listdir(path_dir):
    img = cv2.imread(path_dir + image)
    shape = (img.shape[0], img.shape[1]) 
    end = (180, 1655)
    start = (50, 1530)
    color = (192, 192, 192)
    img = cv2.rectangle(img, start, end, color, -1)
    cv2.imwrite(path_dir + image, img)
