import cv2
import numpy as np

# kernel = np.ones((5,5),np.uint8)

######Read Image from resources file######



def empty(a):
    pass
##########Detecting Color#############


#########Trackbars Creation#############
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,240)
cv2.createTrackbar("Hue min","Trackbars",0,179,empty)
cv2.createTrackbar("Hue max","Trackbars",19,179,empty)
cv2.createTrackbar("Saturation min","Trackbars",110,255,empty)
cv2.createTrackbar("Saturation max","Trackbars",240,255,empty)
cv2.createTrackbar("Value min","Trackbars",153,255,empty)
cv2.createTrackbar("Value max","Trackbars",255,255,empty)


while True:
 img=cv2.imread("Resources/lambo.png")
 imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
 h_min = cv2.getTrackbarPos("Hue min","Trackbars")
 h_max = cv2.getTrackbarPos("Hue max","Trackbars")
 s_min = cv2.getTrackbarPos("Saturation min","Trackbars")
 s_max = cv2.getTrackbarPos("Saturation max","Trackbars")
 v_min = cv2.getTrackbarPos("Value min","Trackbars")
 v_max = cv2.getTrackbarPos("Value max","Trackbars")
 print(h_max,h_min,s_max,s_min,v_max,v_min)
 lower = np.array([h_min,s_min,v_min])
 upper = np.array([h_max,s_max,v_max])
 mask = cv2.inRange(imgHSV,lower,upper)
 imgResult = cv2.bitwise_and(img,img,mask=mask)
 cv2.imshow("Image",img)
 cv2.imshow("HSV",imgHSV)
 cv2.imshow("Mask",mask)
 cv2.imshow("Result",imgResult)
 cv2.waitKey(1)


######Stacking Images######
# imgHor = np.hstack((img,img))
# imgVer = np.vstack((img,img))
# cv2.imshow("horizontal",imgHor)
# cv2.imshow("vertical", imgVer)

####### Wrap Prespective Ops.#############
# width, height = 250, 350
# pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]]) #find points from paint
# pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# matrix = cv2.getPerspectiveTransform(pts1,pts2)
# imgOutput = cv2.warpPerspective(img,matrix,(width,height))

######Various Operations on Image#####
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
# imgCanny = cv2.Canny(img,150,200)
# imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
# imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
# imgResize = cv2.resize(img,(600,300))
# imgCropped = img[0:400,400:600]

###########Creating a matrix and coloring it############
# img = np.zeros((512,512,3),np.uint8)
# print(img)
# img[:]=255,0,0

# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
# cv2.rectangle(img,(0,0),(250,350),(0,0,255),2) #use cv2.FILLED instead of 2 if u want it filled
# cv2.circle(img,(400,50),30,(255,255,0),3)
# cv2.putText(img," ozge onec ",(300,200),cv2.FONT_ITALIC,1,(0,255,255),2)

######Showing the Image#######

#cv2.imshow("Output", imgOutput)
# cv2.imshow("Image Resized",imgResize)
# cv2.imshow("Image Cropped",imgCropped)
# cv2.imshow("Gray Image",imgGray)
# cv2.imshow("Blur Image",imgBlur)
# cv2.imshow("Canny Image",imgCanny)
# cv2.imshow("Dialation Image", imgDialation)
# cv2.imshow("Eroded Image", imgEroded)

#######To see the Dimensions of the image######
# print(img.shape)
# print(imgResize.shape)


######Preventing the image vanishing#######



######Capturing and showing a video#######
#cap = cv2.VideoCapture(0)
#cap.set(3,640)
#cap.set(4,480)
#cap.set(10,300)
#while True:
    #success, img = cap.read()
    #cv2.imshow("Video",img)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #break
