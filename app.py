import cv2
import numpy as np

def cross(x):
    pass


# create and image and window bind
img  = np.zeros((500,700,3),np.uint8)
cv2.namedWindow(winname='mywin')
# create trackbars and switch
switch = '0: OFF \n1: ON'
cv2.createTrackbar(switch,'mywin',0,1,cross)
cv2.createTrackbar('R','mywin',0,255,cross)
cv2.createTrackbar('G','mywin',0,255,cross)
cv2.createTrackbar('B','mywin',0,255,cross)


while True:
    cv2.imshow('mywin',img)
    s = cv2.getTrackbarPos(switch,'mywin')
    r = cv2.getTrackbarPos("R",'mywin')
    g = cv2.getTrackbarPos("G",'mywin')
    b = cv2.getTrackbarPos("B",'mywin')

    if s==1:
        img[:] = [r,g,b]
    else:
        img[:] = 0

    if cv2.waitKey(1) & 0xFF== ord('q'):
        break

cv2.destroyAllWindows()