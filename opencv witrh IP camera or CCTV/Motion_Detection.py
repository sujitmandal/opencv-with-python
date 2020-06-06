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
port_address = 'http://192.168.0.101:8080//'


img_width =512
img_height = 512
first_frame = None


while True:
    img_req = requests.get(port_address + 'shot.jpg')
    img_arr = np.array(bytearray(img_req.content), dtype=np.uint8)
    frame = cv2.imdecode(img_arr, -1)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)


    if first_frame is None:
        first_frame = gray
        continue

    diff_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)
    cnts, _ = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for motion in cnts:
        if cv2.contourArea(motion) < 10000:
            continue

        (x, y, w, h) = cv2.boundingRect(motion)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
    
    cv2.imshow("Color Frame", frame)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


cv2.destroyAllWindows()