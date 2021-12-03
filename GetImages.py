'''
Captures and saves an image every n seconds. 

Used to save images for further analysis

'''


from time import sleep
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils
import datetime
import json
import os

import datetimefunction as dtf

font = cv2.FONT_HERSHEY_SIMPLEX

capture_delay = 10.00 # [seconds]

time_fmt = "%Y-%m-%d %H:%M:%S %f"
imagepath = "/home/pi/images/basedline/"

width = 1920
height = 1088

# width = 3280
# height = 2464

counter = 0
camera = PiCamera()
camera.resolution = (width, height)
camera.framerate = 2.0

camera.rotation = 0



rawCapture = PiRGBArray(camera)
rawCapture.truncate(0)
sleep(0.1)
camera.capture(rawCapture,format='bgr',use_video_port=False)
current_image = rawCapture.array
gray = cv2.cvtColor(current_image,cv2.COLOR_BGR2GRAY) # convert to gray image for motion detection
gray = cv2.GaussianBlur(gray,(21,21),0)
ave = gray.copy().astype("float")
sleep(capture_delay)



timestamp = datetime.datetime.now().strftime(time_fmt)[:-2]
dtf.CheckImageDir(imagepath,timestamp)


Preview = False

start_hour = 7
end_hour = 17
DaysWeek = ["Mon","Tues","Wed","Thu","Fri"]
 

n = 1
while True:
    print("iteration number {}".format(n))
    message_text ="none" # reset the message_text


    rawCapture = PiRGBArray(camera)
    sleep(0.1)
    camera.capture(rawCapture,format='bgr',use_video_port=False)
    current_image = rawCapture.array
    
    time = datetime.datetime.now()
    timestamp = time.strftime(time_fmt)[:-2] 
    hour = int(time.strftime("%H"))
    day = time.strftime("%a")

    datetime.datetime.now().strftime(time_fmt)[:-2] 
    save_path = dtf.CheckImageDir(imagepath,timestamp) # check if the correct paths exists, and create them
    minutes = dtf.GetMinutes(timestamp) # get the minutes, if minutes %10 == 0 save image

    if (hour > start_hour) & (hour <= end_hour) & (day in DaysWeek):
        fn = dtf.buldfilename(timestamp) # filename for current image
        cv2.imwrite(os.path.join(save_path,"{}".format(fn)),current_image)
        print(f"Image {fn} saved")             

    if Preview == True:
        cv2.imshow("images",current_image)
        key  = cv2.waitKey(500)
        if key == ord('q') & 0xFF:
            break
    rawCapture.truncate(0)
    sleep(capture_delay)
    n=n+1
    plt.close()
