import cv2

#This is create by Sujit Mandal

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('haarcascade_eye.xml')

video = cv2.VideoCapture(0)

a = 1

while True:
    a= a + 1 
    cheak, frame = video.read()

    faces = face.detectMultiScale(frame)
    eyes = eye.detectMultiScale(frame)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
        for (x, y, w, h) in eyes:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)
    
    cv2.imshow("frame", frame)

    key = cv2.waitKey(1)

    if key == ord('e'):
        break
print(a)
video.release()
cv2.destroyAllWindows()
    
