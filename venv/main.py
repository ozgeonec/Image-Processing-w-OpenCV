import cv2
import numpy

print("import")
img=cv2.imread("Resources/stronggirl.jpg")
cv2.imshow("Output",img)
cv2.waitKey(0)

cap = cv2.VideoCapture("Resources/chewievideo.mp4")

while True:
    success, imag = cap.read()
    cv2.imshow("Video",imag)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
