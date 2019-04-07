import cv2
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 

#This is create by SUjit Mandal

img_1 = cv2.imread(' ', 1)  #provide image path for example D:\\Python\\ggggggg.jpg
img_2 = cv2.imread(' ', 1)   #provide image path for example D:\\Python\\ggggggg.jpg
img_3 = cv2.imread(' ', 1)  #provide image path for example D:\\Python\\ggggggg.jpg

resize_1 = cv2.resize(img_1, (int(img_1.shape[1]/7), int(img_1.shape[0]/7)))
resize_2 = cv2.resize(img_2, (int(img_2.shape[1]/7), int(img_2.shape[0]/7)))
resize_3 = cv2.resize(img_3, (int(img_3.shape[1]/7), int(img_3.shape[0]/7)))

print(img_1)
print(img_2.shape)

while True:
    if resize_1.shape == resize_2.shape:
        print('image_1 and image_2 are same.')
        cv2.imshow('image_1', resize_1)
        cv2.imshow('image_2', resize_2)

    elif resize_1.shape == resize_3.shape:
            print('image_1 and image_3 are same.')
            cv2.imshow('image_1', resize_1)
            cv2.imshow('image_3', resize_3)

    elif resize_2.shape == resize_3.shape:
                print('image_2 and image_3 are same.')
                cv2.imshow('image_2', resize_2)
                cv2.imshow('image_3', resize_3)


    elif resize_1.shape != resize_2.shape and resize_1.shape != resize_3.shape and resize_2.shape != resize_3.shape:
                    print('The three image are not same!')
                    cv2.imshow('image_1', resize_1)
                    cv2.imshow('image_2', resize_2)
                    cv2.imshow('image_3', resize_3)

    else:
        print('please insert image!.')

    key = cv2.waitKey(1)
    if key == ord('e'):
            break
            
cv2.destroyAllWindows()
