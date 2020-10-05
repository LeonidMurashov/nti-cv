import os
import cv2



# crate list of all negative images
with open('neg.txt', 'w') as f:
    for filename in os.listdir('negative'):
        f.write('negative/' + filename + '\n')
    for filename in os.listdir('cutted_negatives'):
        f.write('cutted_negatives/' + filename + '\n')
    for filename in os.listdir('video_frames'):
        f.write('video_frames/' + filename + '\n')

# create list of positive where only one fixed in the bottom left forner
with open('pos_generated.txt', 'w') as f:
    for filename in os.listdir('positives_with_left_bottom'):
        img = cv2.imread('positives_with_left_bottom/' +  filename)
        end = (180, 1655)
        start = (50, 1530)
        f.write('positives_with_left_bottom/' + filename + ' 1 50 1530 130 125\n')
