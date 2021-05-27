import cv2
import copy
import numpy as np

######################################
widthImg =850
HeightImg =700
######################################

cap = cv2.VideoCapture(0)
cap.set(3,widthImg)
cap.set(4,HeightImg)
cap.set(10,150)

def preprossing(img):
    #Converte Image from BGR To GrayScale
    imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,200,200)
    kernel = np.ones((5,5))
    imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)
    imgThres = cv2.erode(imgDilation,kernel,iterations=1)

    return imgThres

def getContours(img):
    biggest = np.array([])
    maxArea = 0
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if area>5000:
            cv2.drawContours(imgContour,cnt,-1,(0,255,255),3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            if area > maxArea and len(approx) == 4:
                biggest == approx
                maxArea = area
    # cv2.drawContours(imgContour, biggest, -1, (0, 255, 255), 20)
    return biggest

def getWarp(img,biggest):

    pts1 = np.float32([[0,125],[200,54],[52,26],[21,52]])
    pts2 = np.float32([[0,0],[widthImg,0],[0,HeightImg],[widthImg,HeightImg]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgOutput = cv2.warpPerspective(img,matrix,(widthImg,HeightImg))

    return imgOutput
def limit(img):

    pts1 = np.float32([[96,83],[542,46],[122,711],[784,603]])
    pts2 = np.float32([[0,0],[widthImg,0],[0,HeightImg],[widthImg,HeightImg]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgOutput = cv2.warpPerspective(img,matrix,(widthImg,HeightImg))

    return imgOutput

path = "resourses/phsics.jfif"
img2 = cv2.imread(path)
cv2.imshow("Output",img2)
img3 = preprossing(img2)
cv2.imshow("output2", img3)
img4 = limit(img2)
cv2.imshow("output3", img4)

while True:
    success, img = cap.read()
    cv2.resize(img,(widthImg,HeightImg))
    imgContour = img.copy()

    imgThres = preprossing(img)
    biggest = getContours(imgThres)
    print(biggest)
    imgWarped = getWarp(img,biggest)
    cv2.imshow("Result1",imgContour)
    cv2.imshow("output",imgWarped)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break