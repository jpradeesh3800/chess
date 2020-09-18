import cv2
import numpy as np
import matplotlib.pyplot as plt 
import time

start=time.time()
img = cv2.imread('shot7.jpg')
l,b,h=img.shape

# Finding corners
con=np.zeros((l,b))

con=np.uint8(255*np.uint8(img[:,:,2]>100)*np.uint8(img[:,:,1]<100)*np.uint8(img[:,:,0]<100))

contours,_=cv2.findContours(con,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(img,contours,-1,(255,0,0),3)
c=sorted(contours,key=cv2.contourArea)

#(x,y,w,h)=cv2.boundingRect(c[-2])
'''
[[590 427]
 [261 410]
 [278  82]
 [607 100]]
'''
'''
rect = cv2.minAreaRect(c[-2])
box = cv2.boxPoints(rect)
box = np.int0(box)
print(box)'''
epsilon = 0.1*cv2.arcLength(c[-2],True)
a = cv2.approxPolyDP(c[-2],epsilon,True)
box=[a[0][0],a[1][0],a[2][0],a[3][0]]


#cv2.drawContours(img,[box],0,(0,0,255),2)

box=sorted(box,key=lambda x:x[1])
if box[0][0]>box[1][0]:
	box[0],box[1]=box[1],box[0]
if box[2][0]>box[3][0]:
	box[2],box[3]=box[3],box[2]


i=1
box=np.array(box)
box+=np.array([[i,i],[-i,i],[i,-i],[-i,-i]])
pts1 = np.float32(box)
pts2 = np.float32([[0,0],[480,0],[0,480],[480,480]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(480,480))

con2=np.uint8(255*np.uint8(dst[:,:,2]>100)*np.uint8(dst[:,:,1]<100)*np.uint8(dst[:,:,0]<100))


print(time.time()-start)
cv2.imwrite("shit.jpg",dst)
cv2.imshow("image1",img)
cv2.imshow("image2",dst)
cv2.waitKey(0)

