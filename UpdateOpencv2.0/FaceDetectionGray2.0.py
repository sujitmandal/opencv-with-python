import cv2

#Github: https://github.com/sujitmandal

#This programe is create by Sujit Mandal

"""
Github: https://github.com/sujitmandal
This programe is create by Sujit Mandal
LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/
Facebook : https://www.facebook.com/sujit.mandal.33671748
Twitter : https://twitter.com/mandalsujit37
"""


face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video = cv2.VideoCapture(0)



while True:

    check, frame = video.read()
    gray_face = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print(frame)
    faces = face.detectMultiScale(gray_face)
  

    
    for(x, y, w, h) in faces:
        cv2.rectangle(gray_face, (x,y), (x+w, y+h), (255,255,0), 3)
    
    cv2.imshow('gray', gray_face)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()