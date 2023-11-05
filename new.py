import cv2
import pickle 

import os
os.chdir("C:\\Users\\ronak\\New folder\\codebin\\parkingsystemmm")

img=cv2.imread('carParkImg.png')

while True:
    cv2.imsho("image",img)
    cv2.waitKey(1)
