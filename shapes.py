import cv2 as cv
import numpy as np
import utilities

def getContours(img):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv.contourArea(contour)
        print(area)
        if area > 500:
            img = cv.drawContours(imgContours, contour, -1, (100,255,100), 3)
            perimeter = cv.arcLength(contour, True)
            print(perimeter)
            approx = cv.approxPolyDP(contour, 0.02*perimeter, True)
            print(len(approx))
            obj_sides = len(approx)
            x, y, w, h = cv.boundingRect(approx)
            cv.rectangle(imgContours, (x,y), (x+w, y+h), (255,0,0), 4)
            if obj_sides == 3:
                objectType = "Triangle"
                cv.putText(imgContours, objectType, (x+(w//2)-20, y+(h//2)), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 2)
            if obj_sides == 4:
                if (w/h > 0.95) and (w/h <1.05):
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
                cv.putText(imgContours, objectType, (x+(w//2)-20, y+(h//2)), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 2)
            if obj_sides == 5:
                objectType = "Pentagon"
                cv.putText(imgContours, objectType, (x+(w//2)-20, y+(h//2)), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 2)
            if obj_sides == 6:
                objectType = "Hexagon"
                cv.putText(imgContours, objectType, (x+(w//2)-20, y+(h//2)), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 2)
            if obj_sides >= 7:
                objectType = "Circle"
                cv.putText(imgContours, objectType, (x+(w//2)-20, y+(h//2)), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 2)
            else:
                objectType = "None"
           
    return img




path = 'Resources\shapes.png'
img = cv.imread(path)

imgContours = img.copy()
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv.Canny(imgBlur, 50, 50)

imgCnt = getContours(imgCanny)

imgStack = utilities.stackImages(0.6, ([img, imgGray], [imgBlur, imgCanny]))

cv.imshow("Contours", imgCnt)
cv.imshow("image", imgStack)

cv.waitKey(0)