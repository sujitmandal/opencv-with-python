import os
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

cars_cascade = cv2.CascadeClassifier('haarcascade_car.xml')
video = cv2.VideoCapture('cars.mp4') 

try:
    if not os.path.exists('Save Video'):
        os.makedirs('Save Video')

except OSError:
    print('Error: Creating directory!')

print(video)

if (video.isOpened()== False): 
    print("Error opening video file") 


frame_width = int(video.get(3))
frame_height = int(video.get(4))
saveVideo = cv2.VideoWriter('./Save Video/output.mp4',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))



def detect(frame):
    car = cars_cascade.detectMultiScale(frame)
        
    for(x, y, w, h) in car:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 3)
    return(frame)

def silmulation():
    while(video.isOpened):
        check, frame = video.read()
        key = cv2.waitKey(1)

        if check==True:
            cars = detect(frame)
            saveVideo.write(cars)
            cv2.imshow("frame",cars)
        
        else:
            break

        if key == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    silmulation()