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

video = cv2.VideoCapture('a.mp4')

try:
    if not os.path.exists('images'):
        os.makedirs('images')

except OSError:
    print('Error: Creating directory of Images')

cur_frame = 0

while True:
    check, frame = video.read()
    
    if check:
        image = ('./images from video/image' + str(cur_frame) + '.jpg')
        print('Creating..' + image)
        
        cv2.imwrite(image, frame)
        cur_frame += 1

        cv2.imshow('Frame', frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break  
    else: 
        break


video.release()
cv2.destroyAllWindows()