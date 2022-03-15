#!/bin/env python3

# Change camera indices when on other device 
cam1Index = 0
cam2Index = 4 

import os , subprocess ,sys, time
import cv2 as cv
#import numpy as np 
from matplotlib import pyplot as plt 

if sys.platform.startswith('windows'):
    cam1 = cv.VideoCapture(cam1Index)
    cam2 = cv.VideoCapture(cam2Index)
elif sys.platform.startswith('linux'):
    cam1 = cv.VideoCapture(f"/dev/video{cam1Index}")
    cam2 = cv.VideoCapture(f"/dev/video{cam2Index}")
else:
    raise OSError("OS not supported")

for cam in [cam1,cam2]:
    cam.set(cv.CAP_PROP_FOURCC,cv.VideoWriter.fourcc('M','J','P','G'))
    cam.set(cv.CAP_PROP_FPS, 25)
    cam.set(cv.CAP_PROP_FRAME_WIDTH,1280)
    cam.set(cv.CAP_PROP_FRAME_HEIGHT,720)

time.sleep(1)

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
minDisparity = 1
numDisparities = 45
blockSize = 13
P1 = 200
P2 = 4000
disp12MaxDiff = 15
preFilterCap = 2
uniquenessRatio = 1 
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






