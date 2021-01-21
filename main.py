#===>How to Split RGB Color Plains on Camera

import cv2
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    B,G,R=cv2.split(frame)

    red=cv2.merge([B-B,G-G,R])
    green=cv2.merge([B-B,G,R-R])
    blue=cv2.merge([B,G-G,R-R])

    cv2.imshow("Original",frame)
    cv2.imshow('Red',red)
    cv2.imshow('Green',green)
    cv2.imshow('Blue',blue)
    if cv2.waitKey(1)==13:
        break


cap.release()
cv2.destroyWindow()
