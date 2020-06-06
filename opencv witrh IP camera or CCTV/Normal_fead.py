import os
import cv2
import numpy as np
import requests

port_address = 'http://192.168.0.101:8080//'

#Github: https://github.com/sujitmandal
#This programe is create by Sujit Mandal
"""
Github: https://github.com/sujitmandal
This programe is create by Sujit Mandal
LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/
Facebook : https://www.facebook.com/sujit.mandal.33671748
Twitter : https://twitter.com/mandalsujit37
"""

img_width = 512
img_height = 512


while True:

    ipCamRequest = requests.get(port_address + 'shot.jpg')
    ipCamArray = np.array(bytearray(ipCamRequest.content), dtype=np.uint8)
    ipcam = cv2.imdecode(ipCamArray, -1)
    
    cv2.imshow('WebCam', ipcam)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


cv2.destroyAllWindows()