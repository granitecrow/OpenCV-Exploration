# imports
import cv2 as cv
import numpy as np
import utilities

myColors = [[86, 110, 110, 245, 177, 255],
            [160,178,110,245,177,255],
            [30,94,44,111,183,255]]
myColorValues = [[223, 147, 78],
                [84,37,173],
                [0, 255, 233]]

# blue: h_min, h_max = 86, 110; s_min, s_max = 110, 245, v_min, v_max = 177, 255
# red:  h_min, h_max = 160, 178; s_min, s_max = 110, 245, v_min, v_max = 177, 255
# yellow:  h_min, h_max = 30, 94; s_min, s_max = 44, 111, v_min, v_max = 183, 255

def getContours(img):
    x, y, w, h = 0, 0, 0, 0
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv.contourArea(contour)
        if area > 500:
            # img = cv.drawContours(imgResult, contour, -1, (100,255,100), 3)
            perimeter = cv.arcLength(contour, True)
            approx = cv.approxPolyDP(contour, 0.02*perimeter, True)
            x, y, w, h = cv.boundingRect(approx)
            # cv.rectangle(imgResult, (x,y), (x+w, y+h), (255,0,0), 4)
    return x+w//2, y    #return the top-middle point of the bounding box


def findColor(img, myColors, myColorValues):
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    count = 0
    points = []
    for color in myColors:
        lower = np.array(color[0:6:2])  # take all the mins
        upper = np.array(color[1:6:2])  # take all the maxs
        mask = cv.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv.circle(imgResult, (x, y), 10, myColorValues[count], cv.FILLED)
        if x!=0 and y!=0:
            points.append([x, y, count])
        count += 1
        # cv.imshow(str(color[0]), mask)
    return points

def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv.circle(imgResult, (point[0], point[1]), 60, myColorValues[point[2]], cv.FILLED)




myPoints = [] #[x, y, colorID]
# Read Webcam
frameWidth = 1920
frameHeight = 1080
cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)    #brightness
while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints) != 0:
        for points in newPoints:
            myPoints.append(points)
    if (len(myPoints) != 0):
        drawOnCanvas(myPoints, myColorValues)
    # cv.imshow("Webcam", img)
    cv.imshow("result", imgResult)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


