import cv2
import pickle 

import os
os.chdir("C:\\Users\\ronak\\New folder\\codebin\\parkingsystemmm")

img=cv2.imread('carParkImg.png')

width, height = 107, 48
posList=[]

def mouseclick(events,x,y,flags,params):
    if events== cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))

while True:

    for pos in posList:
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height), (255, 0, 255), 2)

    cv2.imshow("image",img)
    cv2.setMouseCallback("image",mouseclick)
    cv2.waitKey(1)