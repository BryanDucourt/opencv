import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
# if you want to display a video, just need to replace the '0' below with
# the filename of the video
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print('cannot open camera')
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print('cannot get frame')
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
