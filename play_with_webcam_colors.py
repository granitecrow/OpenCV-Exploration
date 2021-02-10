import cv2 as cv
import numpy as np
import utilities

def empty(a):
    pass

cv.namedWindow("Trackbars")
cv.resizeWindow("Trackbars", 640, 240)
cv.createTrackbar("Hue Min", "Trackbars", 55, 179,empty)
cv.createTrackbar("Hue Max", "Trackbars", 155, 179,empty)
cv.createTrackbar("Sat Min", "Trackbars", 21, 255,empty)
cv.createTrackbar("Sat Max", "Trackbars", 255, 255,empty)
cv.createTrackbar("Val Min", "Trackbars", 0, 255,empty)
cv.createTrackbar("Val Max", "Trackbars", 255, 255,empty)


# Config Webcam
frameWidth = 1920
frameHeight = 1080
cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)    #brightness
while True:
    success, img = cap.read()

    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    h_min = cv.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv.getTrackbarPos("Sat Min", "Trackbars")
    s_max = cv.getTrackbarPos("Sat Max", "Trackbars")
    v_min = cv.getTrackbarPos("Val Min", "Trackbars")
    v_max = cv.getTrackbarPos("Val Max", "Trackbars")

    # print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv.inRange(imgHSV, lower, upper)

    imgResult = cv.bitwise_and(img, img, mask=mask)

    imgStack = utilities.stackImages(0.5, ([img, imgHSV], [mask, imgResult]))
    cv.imshow("stacked", imgStack)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
