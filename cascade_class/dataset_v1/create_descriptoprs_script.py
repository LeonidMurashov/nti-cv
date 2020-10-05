import os
import cv2



# crate list of all negative images
with open('neg.txt', 'w') as f:
    for filename in os.listdir('negative'):
        f.write('negative/' + filename + '\n')
    for filename in os.listdir('../dataset_v2/cutted_negatives'):
        f.write('../dataset_v2/cutted_negatives/' + filename + '\n')
    for filename in os.listdir('../dataset_v2/video_frames'):
        f.write('../dataset_v2/video_frames/' + filename + '\n')
    for filename in os.listdir('../dataset_v2/negative'):
        f.write('../dataset_v2/negative/' + filename + '\n')


with open('pos.txt', 'w') as f:
    for filename in os.listdir('positive'):
        img = cv2.imread('positive/' +  filename)
        f.write('positive/' + filename + ' 1 0 0 ' + str(img.shape[1]) + ' ' + str(img.shape[0]) + '\n')
# create list of positive where only one fixed in the bottom left forner
    for filename in os.listdir('../dataset_v2/positives_with_left_bottom'):
        img = cv2.imread('../dataset_v2/positives_with_left_bottom/' +  filename)
        end = (180, 1655)
        start = (50, 1530)
        f.write('../dataset_v2/positives_with_left_bottom/' + filename + ' 1 50 1530 130 125\n')

