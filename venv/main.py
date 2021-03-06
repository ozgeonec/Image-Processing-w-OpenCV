import cv2
import numpy as np


frameWidth = 440
frameHeight = 280
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

myColors=[[5,107,0,19,255,255],[133,56,0,159,156,255],[57,76,0,100,255,255]]
myColorValues = [[51,153,255],          ## BGR
                 [255,0,255],
                 [0,255,0],
                 [255,0,0]]

myPoints =  []  ## [x , y , colorId ]

# def empty(a):
#     pass

# cv2.namedWindow("HSV")
# cv2.resizeWindow("HSV", 640, 240)
# cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
# cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
# cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
# cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
# cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
# cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)
#0,179,145,255,103,255
def findColors(img,myColors,myColorValues):
    count = 0
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    newPoints=[]
    for color in myColors:
      lower = np.array(color[0:3])
      upper = np.array(color[3:6])
      mask = cv2.inRange(imgHsv, lower, upper)
      x,y=getContours(mask)
      cv2.circle(imgResult,(x,y),15,myColorValues[count],cv2.FILLED)
      cv2.imshow(str(color[0]),mask)
      if x!=0 and y!=0:
            newPoints.append([x,y,count])
      count += 1
    return newPoints

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #Check treshold
    #if area>2:
        #cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
        prmtr = cv2.arcLength(cnt,True)
        cornerPoints = cv2.approxPolyDP(cnt,0.02*prmtr,True)
        x, y, w, h = cv2.boundingRect(cornerPoints)
    return x*w//2,y

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColors(img, myColors,myColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)
    #imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    # h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    # s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    # s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    # v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    # v_max = cv2.getTrackbarPos("VALUE Max", "HSV")
    # print(h_min)


    # result = cv2.bitwise_and(img, img, mask=mask)
    #
    # mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    # hStack = np.hstack([img, mask, result])
    # cv2.imshow('Horizontal Stacking', hStack)
    findColors(img,myColors,myColorValues)
    cv2.imshow("Result",imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cap.release()
# cv2.destroyAllWindows()

################Copied Stacking Function###############
# def stackImages(scale,imgArray):
#     rows = len(imgArray)
#     cols = len(imgArray[0])
#     rowsAvailable = isinstance(imgArray[0], list)
#     width = imgArray[0][0].shape[1]
#     height = imgArray[0][0].shape[0]
#     if rowsAvailable:
#         for x in range ( 0, rows):
#             for y in range(0, cols):
#                 if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
#                 else:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
#                 if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
#         imageBlank = np.zeros((height, width, 3), np.uint8)
#         hor = [imageBlank]*rows
#         hor_con = [imageBlank]*rows
#         for x in range(0, rows):
#             hor[x] = np.hstack(imgArray[x])
#         ver = np.vstack(hor)
#     else:
#         for x in range(0, rows):
#             if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
#                 imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
#             else:
#                 imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
#             if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
#         hor= np.hstack(imgArray)
#         ver = hor
#     return ver

#############Contour Ops##############
# def getContours(img):
#     contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         #print(area)
#         #Check treshold
#     #if area>2:
#         cv2.drawContours(imgCanny,cnt,-1,(255,0,0),3)
#         prmtr = cv2.arcLength(cnt,True)
#         cornerPoints = cv2.approxPolyDP(cnt,0.02*prmtr,True)
#         print(len(cornerPoints))
#         corners = len(cornerPoints)
#         x, y, w, h = cv2.boundingRect(cornerPoints)
#
#         if corners == 3: objType = "Triangle"
#         elif corners == 4:
#              aspRatio = w/float(h)
#              if aspRatio >0.98 and aspRatio <1.03: objectType= "Square"
#              else: objType= "Rectangle"
#         elif corners > 4: objType= "Circle"
#         else: objType= "None"
#
#
#         cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),1)
#         cv2.putText(imgContour,objType,
#                     (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),1)


##############Shape Detection###################
#############Face Detection###################
# faceCascade= cv2.CascadeClassifier("Resources/haarcascades/haarcascade_frontalface_default.xml")
# img=cv2.imread("Resources/stronggirl.jpg")
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# faces = faceCascade.detectMultiScale(imgGray,1.1,4)
#
# for (x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
# imgContour = img.copy()

# def empty(a):
#      pass


#########Shape Detection Part###########
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.blur(imgGray,(5,5),1)
# imgStack = stackImages(0.5,([img,imgGray,imgBlur]))
# imgCanny = cv2.Canny(imgBlur,15,305)
# getContours(imgCanny)

# while True:
#  imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#
#  cv2.createTrackbar("Canny min","Trackbars",0,179,empty)
#  cv2.createTrackbar("Canny max","Trackbars",19,179,empty)
#
#  c_min = cv2.getTrackbarPos("Canny min","Trackbars")
#  c_max = cv2.getTrackbarPos("Canny max","Trackbars")
#
#  lower = np.array([c_min])
#  upper = np.array([c_max])
#  mask = cv2.inRange(imgHSV,lower,upper)
#  imgResult = cv2.bitwise_and(img,img,mask=mask)
#  cv2.imshow("HSV",imgHSV)



# kernel = np.ones((5,5),np.uint8)

######Read Image from resources file######



# def empty(a):
#     pass
# ##########Detecting Color/Color Picking/Masking#############
#
#
# #########Trackbars Creation#############
# cv2.namedWindow("Trackbars")
# cv2.resizeWindow("Trackbars",640,240)
# cv2.createTrackbar("Hue min","Trackbars",0,179,empty)
# cv2.createTrackbar("Hue max","Trackbars",19,179,empty)
# cv2.createTrackbar("Saturation min","Trackbars",110,255,empty)
# cv2.createTrackbar("Saturation max","Trackbars",240,255,empty)
# cv2.createTrackbar("Value min","Trackbars",153,255,empty)
# cv2.createTrackbar("Value max","Trackbars",255,255,empty)
#
#
# while True:
#  img=cv2.imread("Resources/lambo.png")
#  imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#  h_min = cv2.getTrackbarPos("Hue min","Trackbars")
#  h_max = cv2.getTrackbarPos("Hue max","Trackbars")
#  s_min = cv2.getTrackbarPos("Saturation min","Trackbars")
#  s_max = cv2.getTrackbarPos("Saturation max","Trackbars")
#  v_min = cv2.getTrackbarPos("Value min","Trackbars")
#  v_max = cv2.getTrackbarPos("Value max","Trackbars")
#  print(h_max,h_min,s_max,s_min,v_max,v_min)
#  lower = np.array([h_min,s_min,v_min])
#  upper = np.array([h_max,s_max,v_max])
#  mask = cv2.inRange(imgHSV,lower,upper)
#  imgResult = cv2.bitwise_and(img,img,mask=mask)
#  #
#  # cv2.imshow("HSV",imgHSV)
#  # cv2.imshow("Mask",mask)
#  # cv2.imshow("Result",imgResult)
#
#  imgStack = stackImages(0.6,([img,imgHSV],[mask,imgResult]))
#  cv2.imshow("Stacked Images", imgStack)

# cv2.imshow("Image Stack",imgStack)
# cv2.imshow("Image Canny",imgCanny)
# cv2.imshow("Image Contour",imgContour)

# cv2.imshow("Image",img)
# cv2.waitKey(0)


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
