import cv2
import pytesseract
import numpy as np

kernel = np.ones((5,5),np.uint8)
print(kernel)
#dunction to joinning image together
# def stackeImage(scale,imgArray):
#     rows = len(imgArray)
#     cols = len(imgArray[0])
#     rowsAvilable = isinstance(imgArray[0],list)
#     width = imgArray[0][0].shape[1]
#     height = imgArray[0][0].shape[0]
#     if rowsAvilable:
#         for x in range(0,rows):
#             for y in range(0,cols):
#                 if imgArray[x][y].shape[:2]==imgArray[0][0].shape[:2]:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y],(0,0),None,scale,scale)
#                 else:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y],(imgArray[0][0].shape[1],imgArray[0][0].shape[0]),None,scale,scale)
#                 if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor(imgArray[x][y],cv2.COLOR_GRAY2BGR)
#         imageBlank = np.zeros((height,width,3),np.uint8)
#         hor = [imageBlank]*rows
#         hor_con = [imageBlank]*rows
#         for x in range(0,rows):
#             hor[x] = np.hstack(imgArray[x])
#         ver = np.vstack(hor)
#     else:
#         for x in range(0,rows):
#             if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
#                 imgArray[x]= cv2.resize(imgArray[x],(0,0),None,scale,scale)
#             else:
#                 imgArray[x]= cv2.resize(imgArray[x],(imgArray[0].shape[1],imgArray[0].shape[1]),None,scale,scale)
#             if len(imgArray[x].shape) ==2:
#                 imgArray[x]=cv2.cvtColor(imgArray[x],cv2.COLOR_GRAY2BGR)
#         hor = np.hstack(imgArray)
#         ver=hor
#     return ver

img = cv2.imread("resourses/hOIuY.jpg")
# img= cv2.resize(img,(0,0),None,0.25,0.25)

imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(imgBlur,100,200)
imgDulation = cv2.dilate(imgCanny,kernel,iterations=2)
imgErode = cv2.erode(imgDulation,kernel,iterations=2)

# stackImage = stackeImage(0.2,([img,imgGray]))
# cv2.imshow("Result",stackImage)
scale =0.2
img= cv2.resize(img,(0,0),None,scale,scale)
imgGray= cv2.resize(imgGray,(0,0),None,scale,scale)
imgBlur= cv2.resize(imgBlur,(0,0),None,scale,scale)
imgCanny= cv2.resize(imgCanny,(0,0),None,scale,scale)
imgDulation= cv2.resize(imgDulation,(0,0),None,scale,scale)
imgErode= cv2.resize(imgErode,(0,0),None,scale,scale)

print(img.shape)

imgGray = cv2.cvtColor(imgGray,cv2.COLOR_GRAY2BGR)
imgBlur = cv2.cvtColor(imgBlur,cv2.COLOR_GRAY2BGR)
imgCanny = cv2.cvtColor(imgCanny,cv2.COLOR_GRAY2BGR)
imgDulation = cv2.cvtColor(imgDulation,cv2.COLOR_GRAY2BGR)
imgErode = cv2.cvtColor(imgErode,cv2.COLOR_GRAY2BGR)

hor = np.hstack((img,imgGray,imgBlur))
hor2 = np.hstack((imgCanny,imgDulation,imgErode))
ver = np.vstack((hor,hor2))

cv2.imshow("Vertical",ver)

# cv2.imshow("Original",img)
# cv2.imshow("Gray",imgGray)
# cv2.imshow("Blur",imgBlur)
# cv2.imshow("Canny",imgCanny)
# cv2.imshow("Dulation",imgDulation)
# cv2.imshow("Erode",imgErode)

# img2 = cv2.imread("resourses/zMoo4.jpg")
# print(img2.shape)
#
# img2= cv2.resize(img2,(0,0),None,0.5,0.5)
#
# imgGray = cv2.cvtColor(imgGray,cv2.COLOR_GRAY2BGR)
# hor = np.hstack((img,imgGray))
# ver = np.vstack((img1,img2))
#
# cv2.imshow("Horizontal",hor)

cv2.waitKey(0)