import cv2 as cv
import numpy as np

faceCascade = cv.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")


def detectFace(img):
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x,y,w,h) in faces:
        cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
    cv.imshow("image", img)


# Read Webcam
frameWidth = 1920
frameHeight = 1080
cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)    #brightness
while True:
    success, img = cap.read()
    detectFace(img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
