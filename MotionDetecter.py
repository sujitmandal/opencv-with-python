import cv2
import time
import pandas
import os
from datetime import datetime

#This is create by SUjit Mandal

first_frame = None
status_list = [None ,None]
time = []
df = pandas.DataFrame(columns = ["Start","End"])

video = cv2.VideoCapture(0) 

try:
    if not os.path.exists('Color'):
        os.makedirs('Color')
    if not os.path.exists('Threshold'):
        os.makedirs('Threshold')
    if not os.path.exists('gray'):
        os.makedirs('gray')
    if not os.path.exists('Difference Frame'):
        os.makedirs('Difference Frame')
    if not os.path.exists('mixd color'):
        os.makedirs('mixd color')
    if not os.path.exists('HSV Color'):
        os.makedirs('HSV Color')
    if not os.path.exists('lab coloer'):
        os.makedirs('lab coloer')

except OSError:
   print ('Error: Creating directory of data')

img_counter_color = 0
img_counter_Threshold = 0
img_counter_gray = 0
img_counter_Difference_Frame = 0
img_counter_mixd_color = 0
img_counter_HSV_Color = 0
img_counter_lab = 0 

while True:
    check, frame = video.read()
    status = 0

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    mixd_color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mixd_color = cv2.GaussianBlur(mixd_color, (21, 21), 1)
    HSV_Color = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    lab_color = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

    if first_frame is None:
        first_frame = gray
        continue
        
    diff_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)

    (_, cnts, _) = cv2.findContours(thresh_frame.copy(),
                    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1

        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.rectangle(mixd_color, (x, y), (x + w, y + h), (0, 0, 255), 3)
        cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 0, 255), 3)
        cv2.rectangle(diff_frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
        cv2.rectangle(thresh_frame, (x, y), (x + w, y + h), (255, 255, 0), 3)
        cv2.rectangle(HSV_Color, (x, y), (x + w, y + h), (255, 255, 0), 3)
        cv2.rectangle(lab_color, (x, y), (x + w, y + h), (255, 255, 0), 3)
    status_list.append(status)
    
    status_list = status_list[-2:]
    if status_list[-1] == 1 and status_list[-2] == 0:
        time.append(datetime.now())
    
    if status_list[-1] == 0 and status_list[-2] == 1:
        time.append(datetime.now())
    
    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Difference Frame", diff_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)
    cv2.imshow('mixd color Frame', mixd_color)
    cv2.imshow('HSV Color Frame', HSV_Color)

    key = cv2.waitKey(1)
    if key == ord('e'):
        if status == 1:
            time.append(datetime.now)
        break
    elif key == ord(' '):
        img_name_color = ("./Color/image_{}.jpg".format(img_counter_color))
        cv2.imwrite(img_name_color, frame)
        print("{} Capture...".format(img_name_color))
        img_counter_color += 1
    #elif key == ord('c'):
        img_name_Threshold = ("./Threshold/image_{}.jpg".format(img_counter_Threshold))
        cv2.imwrite(img_name_Threshold, thresh_frame)
        print('{} Capture...'.format(img_name_Threshold))
        img_counter_Threshold += 1
    #elif key == ord('v'):
        img_name_gray = ("./gray/image_{}.jpg".format(img_counter_gray))
        cv2.imwrite(img_name_gray, gray)
        print('{} Capture...'.format(img_name_gray))
        img_counter_gray += 1
    #elif key == ord('b'):
        img_name_Difference_Frame = ("./Difference Frame/image_{}.jpg".format(img_counter_Difference_Frame))
        cv2.imwrite(img_name_Difference_Frame, diff_frame)
        print("'{} Capture...".format(img_name_Difference_Frame))
        img_counter_Difference_Frame += 1
    #elif key == ord('x'):
        img_name_mixd_color = ("./mixd color/image_{}.jpg".format(img_counter_mixd_color))
        cv2.imwrite(img_name_mixd_color, mixd_color)
        print('{} Capture...'.format(img_name_mixd_color))
        img_counter_mixd_color =+ 1
    #elif key == ord('n'):
        img_name_HSV_Color = ("./HSV Color/image_{}.jpg".format(img_counter_HSV_Color))
        cv2.imwrite(img_name_HSV_Color, HSV_Color)
        print('{} Capture...'.format(img_name_HSV_Color))
    #elif key == ord('m'):
        img_name_lab = ("./lab coloer/image_{}.jpg".format(img_counter_lab))
        cv2.imwrite(img_name_lab, lab_color)
        print('{} Capture....'.format(img_name_lab))

for i in range(0, len(time), 2):
    df = df.append({"Start":time[i], "End":time[i + 1]}, ignore_index = True)
df.to_csv("Time_of_MotionDetecter.csv")

video.release()
cv2.destroyAllWindows()
