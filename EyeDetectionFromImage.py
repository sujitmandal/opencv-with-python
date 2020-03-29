import numpy as np
import cv2

#This is Create by Sujit Mandal

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
 
img = cv2.imread('') #path of the image which is going to be detected


resize = cv2.resize(img, (int(img.shape[1]/7), int(img.shape[0]/7)))
gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)

eyes = eye_cascade.detectMultiScale(gray)

for (x,y,w,h) in eyes:
    cv2.rectangle(resize,(x,y),(x+w,y+h),(255,0,0),2)

while True:
    cv2.imshow('frame', resize)

    key = cv2.waitKey(1)
    if key == ord('e'):
        break

cv2.destroyAllWindows()