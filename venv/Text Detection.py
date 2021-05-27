########### Libraries ###############
import cv2
import pytesseract
import numpy as np
pytesseract.pytesseract.tesseract_cmd= "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
#####################################

########### Dimensions ##############
widthImg =850
HeightImg =700
kernel = np.ones((5,5),np.uint8)
#####################################

########### Read Image ##############
path = 'resourses/font.png'
img = cv2.imread(path)
#####################################

########### Image Processing ########
imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,500,500)
imgDulation = cv2.dilate(imgCanny,kernel,iterations=1)
imgErode = cv2.erode(imgDulation,kernel,iterations=1)
#####################################

########### Resize Image ############
scale =0.3
img= cv2.resize(img,(0,0),None,scale,scale)
imgGray= cv2.resize(imgGray,(0,0),None,scale,scale)
imgBlur= cv2.resize(imgBlur,(0,0),None,scale,scale)
imgCanny= cv2.resize(imgCanny,(0,0),None,scale,scale)
imgDulation= cv2.resize(imgDulation,(0,0),None,scale,scale)
imgErode= cv2.resize(imgErode,(0,0),None,scale,scale)
#####################################

########### Display Imags ###########
cv2.imshow("Orginal",img)
cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dulation Image",imgDulation)
#####################################

########### Print Size of Image #####
print("size of image: ")
print("Width: ",img.shape[1])
print("Height: ",img.shape[0])
print("Channels: ",img.shape[2])
#####################################

# this statement to enable us from
# which image we want to detect text
img =img
#####################################

#print text inside image using pytesseract algorithm package#
print("String in Image: ")
print(pytesseract.image_to_string(img))
#####################################

########## Detecting Characters ####
himg,wimg ,s= img.shape
cong = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    print (b)
    b=b.split(' ')
    #print(b)
    x,y,w,h =int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,himg-y),(w,himg-h),(0,0,255),1)
    cv2.putText(img,b[0],(x,himg-y-40),cv2.FONT_ITALIC,1,(255,0,0),2)
######################################

# ########## To detect words ##########
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
#             cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),1)
######################################

# ###### To detect Digits only ########
# himg,wimg,s = img.shape
# cong = r'--oem 3 --psm 6 outputbase digits'
# print(himg,wimg)
# boxes = pytesseract.image_to_data(img,config=cong)
# for x,b in enumerate(boxes.splitlines()):
#     if x!=0:
#         b=b.split()
#         #print(b)
#         if len(b)==12:
#             x,y,w,h =int(b[6]),int(b[7]),int(b[8]),int(b[9])
#             cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),1)
#             cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
######################################

####### Display Detected Image #######
cv2.imshow("Result",img)
######################################

#The function waits for specified milliseconds for any keyboard event, and 0 to infinte time
cv2.waitKey(0)