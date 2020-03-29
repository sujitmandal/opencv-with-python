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
eye = cv2.CascadeClassifier('haarcascade_eye.xml')

video = cv2.VideoCapture(0)
first_frame = None

while True:
    check, frame = video.read()
    print(frame)

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
    cnts, _ = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for motion in cnts:
        if cv2.contourArea(motion) < 10000:
            continue
        
        (x, y, w, h) = cv2.boundingRect(motion)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
    
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()