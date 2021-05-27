import cv2
import pytesseract
import numpy as np


path = 'resourses/font.png'
img = cv2.imread(path)
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(img,500,500)

print(img.shape)
print(imgGray.shape)
cv2.imshow("Orginal",img)
cv2.imshow("Gray",imgGray)
cv2.imshow("Blur",imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.waitKey(0)
