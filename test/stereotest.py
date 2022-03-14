#!/bin/env python3

# Change camera indices when on other device 
cam1Index = 0
cam2Index = 4 


import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt 

cam1 = cv.VideoCapture(cam1Index)
cam2 = cv.VideoCapture(cam2Index)

rv1 ,ImL = cam1.read()
rv2 ,ImR = cam2.read()

ImL = cv.cvtColor(ImL, cv.COLOR_RGB2GRAY)
ImR = cv.cvtColor(ImR, cv.COLOR_RGB2GRAY)

#if rv1 != 0 and rv2 !=0: 
#    raise ValueError("Camera measurements return non-zero return value")


stereo = cv.StereoSGBM_create(minDisparity=8,numDisparities=74, blockSize=2)
ImR = cv.resize(ImR, (1280,720), interpolation= cv.INTER_LINEAR)

disparity = stereo.compute(ImL,ImR)

plt.imshow(disparity,'gray')
plt.show()





