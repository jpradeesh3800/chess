import cv2

img=cv2.imread("shit.jpg")
x=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
cv2.imshow("IMAGE",x)
cv2.imshow('image',img)
cv2.waitKey(0)
