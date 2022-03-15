#!/bin/env python3

# Change camera indices when on other device 
cam1Index = 4
cam2Index = 6

import os , subprocess ,sys, time
import cv2 as cv
#import numpy as np 
from matplotlib import pyplot as plt 

cam1 = cv.VideoCapture(cam1Index)
cam2 = cv.VideoCapture(cam2Index)

time.sleep(2)

rv1 ,ImL = cam1.read()
rv2 ,ImR = cam2.read()

cv.imwrite('Left.jpg',ImL)
cv.imwrite('Right.jpg',ImR)

ImL = cv.cvtColor(ImL, cv.COLOR_RGB2GRAY)
ImR = cv.cvtColor(ImR, cv.COLOR_RGB2GRAY)

# Dunno what the return values mean but this could be an error check
#if rv1 != 0 and rv2 !=0: 
#    raise ValueError("Camera measurements return non-zero return value")

# Variables for the stereo algorithm
minDisparity = 0
numDisparities = 16
blockSize = 12
P1 = 100
P2 = 1000
disp12MaxDiff = 1
preFilterCap = 1
uniquenessRatio = 3
speckleWindowSize = 400
speckleRange = 200

# Stereo algorith definition 
stereo = cv.StereoSGBM_create(minDisparity=minDisparity,
                              numDisparities=numDisparities,
                              blockSize=blockSize,
                              P1=P1,
                              P2=P2,
                              disp12MaxDiff=disp12MaxDiff,
                              preFilterCap=preFilterCap,
                              uniquenessRatio=uniquenessRatio,
                              speckleRange=speckleRange,
                              speckleWindowSize=speckleWindowSize)

# Resize if there is a deparity between cameras
#ImR = cv.resize(ImR, (1280,720), interpolation= cv.INTER_LINEAR)

disparity = stereo.compute(ImL,ImR)
#plt.imshow(disparity,'gray')
plt.show()


dispname = "disparity.jpg"
cv.imwrite(dispname,disparity)


fpath  = os.path.abspath(dispname)
if sys.platform.startswith('windows'):
    os.startfile(fpath)
elif sys.platform.startswith('darwin'): #MacOS
    os.call(('open', fpath))
else: #Assume linux at this point
    subprocess.run(('xdg-open', fpath))






