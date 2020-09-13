import cv2
import numpy


#img=cv2.imread("Resources/stronggirl.jpg")
#cv2.imshow("Output",img)
#cv2.waitKey(0)

cap = cv2.VideoCapture("Resources/chewievideo.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
