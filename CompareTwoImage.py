import cv2
import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt 

#This is create by SUjit Mandal

img_1 = cv2.imread('', 1)  #provide image path for example D:\\Python\\ggggggg.jpg
img_2 = cv2.imread(' ', 1) #provide image path for example D:\\Python\\ggggggg.jpg



resize_1 = cv2.resize(img_1, (int(img_1.shape[1]/7), int(img_1.shape[0]/7)))
resize_2 = cv2.resize(img_2, (int(img_2.shape[1]/7), int(img_2.shape[0]/7)))

print('img_1')
print(img_1.shape)
#print(img_2)
#print(img_2.shape)


while True:
    if resize_1.shape == resize_2.shape:
        print('The two image are same!')
        cv2.imshow('image_1', resize_1)
        cv2.imshow('image_2', resize_2)
        
    else:
        print('The two image are not same!')
        cv2.imshow('image_1', resize_1)
        cv2.imshow('image_2', resize_2)

    key = cv2.waitKey(1)
    if key == ord('e'):
        break

cv2.destroyAllWindows()


