import cv2
import numpy as np
import os
import pandas
from datetime import datetime
from matplotlib import pyplot as plt

#This is create by Sujit Mandal

status_list = [None ,None]
time = []
df = pandas.DataFrame(columns = ["Start","End"])

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video = cv2.VideoCapture(0)

try:
    if os.path.exists("FaceDetect"):
        os.makedirs('FaceDetect')
except OSError:
    print('Error: Creating directory of data')

cv2.namedWindow("frame")
img_counter = 0
a = 1
while True:
    a = a + 1
    status = 0
    check, frame = video.read()
    #print(frame)
    faces = face.detectMultiScale(frame)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)


    status_list.append(status)

    status_list = status_list[-2:]
    if status_list[-1] == 1 and status_list[-2] == 0:
        time.append(datetime.now())
    
    if status_list[-1] == 0 and status_list[-2] == 1:
        time.append(datetime.now())

    cv2.imshow("frame",frame)

    key = cv2.waitKey(1)

    if key == ord('e'):
        if status == 1:
            time.append(datetime.now)
        break

    if key == ord(' '):
        name = ("./FaceDetect/image_{}.jpg".format(img_counter))
        cv2.imwrite(name, frame)
        print("{} written!".format(name))
        img_counter +=1 

for i in range(0, len(time), 2):
    df = df.append({"Start":time[i], "End":time[i + 1]}, ignore_index = True)
df.to_csv("Time_of_Movments_FaceDetectio.csv")

print(a)
video.release()
cv2.destroyAllWindows()
