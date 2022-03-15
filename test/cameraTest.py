
import sys  
import cv2 as cv

camind = 4 

if sys.platform.startswith('linux'):
    #cam = cv.VideoCapture(4) #uses GStreamer as its interface with the camera 
    cam = cv.VideoCapture(f"/dev/video{camind}") #uses native kernel driver: v4l2 
elif sys.platform.startswith('windows'):
    cam = cv.VideoCapture(camind)
else:
    raise OSError("OS not supported")

print("Setting encoding")
cam.set(cv.CAP_PROP_FOURCC,cv.VideoWriter.fourcc('M','J','P','G'))
print("Setting fps")
cam.set(cv.CAP_PROP_FPS, 25)
print("Setting resolution ")
cam.set(cv.CAP_PROP_FRAME_WIDTH,1920)
cam.set(cv.CAP_PROP_FRAME_HEIGHT,1080)


print("Camera configured")

ret, pic = cam.read()

cv.imwrite("camtest.jpg", pic)
print("Picture taken")
