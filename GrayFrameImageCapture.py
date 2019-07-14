import cv2
import time
import pandas
import os
from datetime import datetime

#This programe is create by Sujit Mandal

'''
note: in order to capture image yoy need to press "space" key from keybord

'''

first_frame = None
status_list = [None ,None]
time = []
df = pandas.DataFrame(columns = ["Start","End"])

video = cv2.VideoCapture(0) 

try:
    if not os.path.exists('gray'):
        os.makedirs('gray')
 
except OSError:
   print ('Error: Creating directory of data')

img_counter_gray = 0

while True:
    #check, frame = video.read(0)
    check, frame = video.read()
    status = 0

    #print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
    if first_frame is None:
        first_frame = gray
        continue
        
    diff_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)

    (_, cnts, _) = cv2.findContours(thresh_frame.copy(),
                    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    
    status_list.append(status) 
    
    status_list = status_list[-2:]
    if status_list[-1] == 1 and status_list[-2 ] == 0:
        time.append(datetime.now())
    
    if status_list[-1] == 0 and status_list[-2] == 1:
        time.append(datetime.now())
    
    cv2.imshow("Gray Frame", gray)

    key = cv2.waitKey(1)
    if key == ord('e'):
        if status == 1:
            time.append(datetime.now)
        break
    elif key == ord(' '): #this key will capture image 
        img_name_gray = ("./gray/image_{}.jpg".format(img_counter_gray))
        cv2.imwrite(img_name_gray, gray)
        print('{} Capture...'.format(img_name_gray))
        img_counter_gray += 1
    

for i in range(0, len(time), 2):
    df = df.append({"Start":time[i], "End":time[i + 1]}, ignore_index = True)
df.to_csv("Time_of_MotionDetecter.csv")

video.release()
cv2.destroyAllWindows()