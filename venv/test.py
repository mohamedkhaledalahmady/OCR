import cv2
import pytesseract
import numpy as np

######################################
widthImg =850
HeightImg =700
######################################

pytesseract.pytesseract.tesseract_cmd= "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
img = cv2.imread("resourses/cairo.PNG")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print("String in Image: ")
print(pytesseract.image_to_string(img))

#image processing function
def preprossing(img):
    #Converte Image from BGR To GrayScale
    imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,200,200)
    kernel = np.ones((5,5))
    imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)
    imgThres = cv2.erode(imgDilation,kernel,iterations=1)

    return img

#image limitting function
def limit(img):

    pts1 = np.float32([[96,83],[542,46],[122,711],[784,603]])
    pts2 = np.float32([[0,0],[widthImg,0],[0,HeightImg],[widthImg,HeightImg]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgOutput = cv2.warpPerspective(img,matrix,(widthImg,HeightImg))

    return imgOutput

# path = "resourses/phsics.jfif"
# img2 = cv2.imread(path)
# cv2.imshow("Output",img2)
# # img2 = preprossing(img2)
# # cv2.imshow("output2", img2)
# img2 = limit(img2)
#
# img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
# cv2.imshow("output3", img2)
#
# print(img2.shape)

# #Detecting Characters
# himg,wimg,s = img2.shape
# cong = r'--oem 3 --psm 6 outputbase digits'
# print(himg,wimg)
# boxes = pytesseract.image_to_boxes(img2)
# for b in boxes.splitlines():
#     #print (b)
#     b=b.split(' ')
#     #print(b)
#     x,y,w,h =int(b[1]),int(b[2]),int(b[3]),int(b[4])
#     cv2.rectangle(img2,(x,himg-y),(w,himg-h),(0,0,255),1)
#     cv2.putText(img2,b[0],(x,himg-y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

#Detecting Characters
himg,wimg,s = img.shape
cong = r'--oem 3 --psm 6 outputbase digits'
print("size of image: ")
print("Width: ",img.shape[0])
print("Height: ",img.shape[1])
print("Channels: ",img.shape[2])
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    #print (b)
    b=b.split(' ')
    #print(b)
    x,y,w,h =int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,himg-y),(w,himg-h),(0,0,255),1)
    cv2.putText(img,b[0],(x,himg-y-25),cv2.FONT_ITALIC,0.5,(255,0,0),1)

# #Detecting words
# himg,wimg,s = img.shape
# print(himg,wimg)
# boxes = pytesseract.image_to_data(img)
# for x,b in enumerate(boxes.splitlines()):
#     if x!=0:
#         b=b.split()
#         print(b)
#         if len(b)==12:
#             x,y,w,h =int(b[6]),int(b[7]),int(b[8]),int(b[9])
#             cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),1)
#             cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)

# #Detecting digits
# himg,wimg,s = img.shape
# cong = r'--oem 3 --psm 6 outputbase digits'
#
# print(himg,wimg)
# boxes = pytesseract.image_to_data(img,config=cong)
# for x,b in enumerate(boxes.splitlines()):
#     if x!=0:
#         b=b.split()
#         print(b)
#         if len(b)==12:
#             x,y,w,h =int(b[6]),int(b[7]),int(b[8]),int(b[9])
#             cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),1)
#             cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
cv2.imshow("Output",img)

cv2.waitKey(0)

print("Mohamed")
