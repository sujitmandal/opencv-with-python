import cv2
import numpy as np
import matplotlib.pyplot as plt

#Tfis is Create by Sujit Mandal

img = cv2.imread('') #path of the image which is going to be processes

resize = cv2.resize(img, (int(img.shape[1]/7), int(img.shape[0]/7)))

while True:
    print(img)
    print(img.shape)
    plt.imshow(resize)
    plt.show()

    key = cv2.waitKey(1)

    if key == ('e'):
        break
cv2.destroyAllWindows() 