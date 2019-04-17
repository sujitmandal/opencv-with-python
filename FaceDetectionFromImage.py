import numpy as np
import cv2

#This programe is create by Sujit Mandal

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
 
img = cv2.imread('') #path of the image which is going to be detected

resize = cv2.resize(img, (int(img.shape[1]/7), int(img.shape[0]/7)))

gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(resize,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = resize[y:y+h, x:x+w]

while True:
    cv2.imshow('frame', resize)

    key = cv2.waitKey(1)

    if key == ord('e'):
        break

cv2.destroyAllWindows()
