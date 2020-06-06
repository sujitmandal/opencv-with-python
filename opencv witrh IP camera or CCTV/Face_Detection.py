import os
import cv2
import numpy as np
import requests

#Github: https://github.com/sujitmandal
#This programe is create by Sujit Mandal
"""
Github: https://github.com/sujitmandal
This programe is create by Sujit Mandal
LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/
Facebook : https://www.facebook.com/sujit.mandal.33671748
Twitter : https://twitter.com/mandalsujit37
"""


laptopCam = cv2.VideoCapture(0)
port_address = ('http://192.168.0.101:8080//')
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def IpCam():
    ipCamRequest = requests.get(port_address + 'shot.jpg')
    ipCamArray = np.array(bytearray(ipCamRequest.content), dtype=np.uint8)
    ipcam = cv2.imdecode(ipCamArray, -1)
    return(ipcam)

def FaceDetection(frame):
    face = faceCascade.detectMultiScale(frame)

    for(x, y, w, h) in face:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)

    return(frame)

def Surveillance():
    while True:
        check, lapCam = laptopCam.read()
        ipcam = IpCam()
        

        key = cv2.waitKey(1)

        if check==True:
            face = FaceDetection(lapCam)
            ipcam = FaceDetection(ipcam)

            cv2.imshow('Ip Cam', ipcam)
            cv2.imshow("Web Cam",face)
        
        else:
            break

        if key == ord('q'):
            break

    
    laptopCam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    Surveillance()
    
