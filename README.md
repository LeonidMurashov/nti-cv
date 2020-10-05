# Instruciton

1. check requirements
2. run main.py with image in arg1

## Requirements

- tensorflow [ pip3 install tf-nightly ]
- numpy      [ pip3 install numpy ]
- opencv     [ pip3 install opencv-python ]

## Algorithm

Script uses 2 methods. First is mobile-net ML. Second is opencv Haar cascade.
To achive better acuracy we use several image crops and resizes.

Haar cascade was trainer on images from Vk and generated sumples. It have realy small rate of false positive and used only as second method in case of first couldn't detect circle.
  
> Team:  ***Branch predictors***
