
import exifWrite
import sys
import cv2 as cv
import os

cameras = []

def addCamera(num):
    if sys.platform.startswith('linux'):
        #cam = cv.VideoCapture(4) #uses GStreamer as its interface with the camera 
        cameras.append(cv.VideoCapture(f"/dev/video{num}")) #uses native kernel driver: v4l2 
    elif sys.platform.startswith('windows'):
        cameras.append(cv.VideoCapture(num))
    else:
        raise OSError("OS not supported")

def setSettings(cam,settings):
    for a in settings:
        cam.set(a[0],a[1])

def makePicture(ind,filename, x_off=0, y_off=0, width=1440 , height=1080):
   print(f"[Taking picture] {ind} {filename}")
   ret, pic = cameras[ind].read()
   print(f"[WRITING] {filename} ({ret})")

   cropped_pic = pic[y_off:min(1080,height+y_off),x_off:min(1920,width+x_off)]
   
   cv.imwrite(filename,cropped_pic)

def makePictures(path,picIndex,exifData):
    for c in range(len(cameras)):
        campath = os.path.join(path, f"{c}")
        if not os.path.exists(campath):
           os.makedirs(campath)
        imgpath = os.path.join(campath,f"img{picIndex}.jpg")
        makePicture(c,imgpath, x_off=270)
        exifWrite.setExif(imgpath,exifData)


def main():
    print("Take pictures, then move the camera")
    input("Press any button to start taking pictures")
   
    addCamera(0)

    sett = [[[cv.CAP_PROP_FOURCC,cv.VideoWriter.fourcc('M','J','P','G')],
            [cv.CAP_PROP_FPS, 25],
            [cv.CAP_PROP_FRAME_WIDTH,1440],
            [cv.CAP_PROP_FRAME_HEIGHT,1080]], 
            [[cv.CAP_PROP_FOURCC,cv.VideoWriter.fourcc('M','J','P','G')],
            [cv.CAP_PROP_FPS, 25],
            [cv.CAP_PROP_FRAME_WIDTH,1920],
            [cv.CAP_PROP_FRAME_HEIGHT,1080]]]

    setSettings(cameras[0],sett[0])


    i = 0
    while True:
        makePictures("pictures",i,exifWrite.exampleTag)
        input("Press any button for the next picture")
        i = i + 1

if __name__ == "__main__":
    main()
        

