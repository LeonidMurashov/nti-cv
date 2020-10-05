# Instruciton

1. pip3 install requirements.txt
2. python3 main.py data/img1.jpg

## Algorithm

Script uses mobile-net ML
To achive better acuracy we use several image crops and resizes.

## Research

We tried several methods to achieve the best result. First was pattern match, which was good but unable to detect rotated and resized circles
The second was Haar cascade. This method is pretty accurate but during lack of time, we struggled to create a suitable dataset resulting in better results. One is better on one "type" of circles and the second one gives better results on different circles. Nevertheless, haar cascade is or exact or has a high rate of false negatives.

> Script take around 30s due to long loading times. The processing itself takes not more then a second.
> Team:  ***Branch predictors***
