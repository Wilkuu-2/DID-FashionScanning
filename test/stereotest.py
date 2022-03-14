#!/bin/env python3

# Change camera indices when on other device 
cam1Index = 0
cam2Index = 4 


import cv2 as cv
#import numpy as np 
from matplotlib import pyplot as plt 

cam1 = cv.VideoCapture(cam1Index)
cam2 = cv.VideoCapture(cam2Index)

rv1 ,ImL = cam1.read()
rv2 ,ImR = cam2.read()

ImL = cv.cvtColor(ImL, cv.COLOR_RGB2GRAY)
ImR = cv.cvtColor(ImR, cv.COLOR_RGB2GRAY)

# Dunno what the return values mean but this could be an error check
#if rv1 != 0 and rv2 !=0: 
#    raise ValueError("Camera measurements return non-zero return value")

# Variables for the stereo algorithm
minDisparity = 0,
numDisparities = 16,
blockSize = 3,
P1 = 0,
P2 = 0,
disp12MaxDiff = 0,
preFilterCap = 0,
uniquenessRatio = 0,
speckleWindowSize = 0,
speckleRange = 0,
mode = cv.StereoSGBM.MODE_SGBM 

# Stereo algorith definition 
stereo = cv.StereoSGBM_create(minDisparity=minDisparity,
                              numDisparities=numDisparities,
                              blockSize=blockSize,
                              P1=P1,
                              P2=P2,
                              disp12MaxDiff=disp12MaxDiff,
                              preFilterCap=preFilterCap,
                              uniquenessRatio=uniquenessRatio)

# Resize if there is a deparity between cameras
#ImR = cv.resize(ImR, (1280,720), interpolation= cv.INTER_LINEAR)

disparity = stereo.compute(ImL,ImR)

plt.imshow(disparity,'gray')
plt.show()





