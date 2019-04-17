import cv2
import os

#This programe is create by Sujit Mandal

eye = cv2.CascadeClassifier('haarcascade_eye.xml')

try:
    if os.path.exists('eyeDetect'):
        os.makedirs("eyeDetect")
except OSError:
    print('Error: Creating directory of data')

video = cv2.VideoCapture(0)

a = 1
counter = 0
while True:
    a = a + 1
    cheak, frame = video.read()

    faces = eye.detectMultiScale(frame)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
    
    cv2.imshow("frame", frame)

    key = cv2.waitKey(1)

    if key == ord('e'):
        break

    if key == ord(' '):
        name = ('./eyeDetect/image_{}.jpg'.format(counter))
        cv2.imwrite(name, frame)
        print("{} Capture..".format(name))
        counter +=1
    
print(a)
video.release()
cv2.destroyAllWindows()

