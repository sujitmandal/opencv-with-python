import cv2
import time
import pandas
import os
from datetime import datetime

first_frame = None
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('haarcascade_eye.xml')

video = cv2.VideoCapture(0) 


while True:
    check, frame = video.read()
    status = 0

    faces = face.detectMultiScale(frame)
    eyes = eye.detectMultiScale(frame)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
        for (x, y, w, h) in eyes:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)

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

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1

        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
        cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 0, 255), 3)
    
    
    #cv2.imshow("Gray Frame", gray)
    cv2.imshow("Color Frame", frame)


    key = cv2.waitKey(1)
    if key == ord('e'):
        break


video.release()
cv2.destroyAllWindows()