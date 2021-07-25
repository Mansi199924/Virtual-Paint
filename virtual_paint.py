import cv2 
import numpy as np
frameWidth = 640
frameHeight = 480
brightness = 150
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, brightness)

myColors = [[53 , 179 , 73 , 255 , 1 , 255],
            [48 , 79 , 35, 255 , 0 , 255]]

myColorValues = [[0,0,255],[0,255,0]]

myPoints = []  #[x,y,colorid]

def findColor(img,myColors,myColorValues):
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    newPoints = []
    for i in range(2):
        h_min = myColors[i][0]
        h_max = myColors[i][1]
        s_min = myColors[i][2]
        s_max = myColors[i][3]
        v_min = myColors[i][4]
        v_max = myColors[i][5]
        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])
        mask = cv2.inRange(imgHsv, lower, upper)
        x,y = getContours(mask)
        cv2.circle(imgResult,(x,y),8,myColorValues[i],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,i])
        #cv2.imshow(str(i),mask)
    return newPoints

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            #cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y


def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult,(point[0],point[1]),8,myColorValues[point[2]], cv2.FILLED)
        

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img,myColors,myColorValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
            
    if len(newPoints) != 0:
        drawOnCanvas(myPoints,myColorValues)

    cv2.imshow('Result', imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()