import cv2
import numpy as np
from detection import detect
def crop(img):
	# finding shape
	l,b,h=img.shape

	# finding red pixels
	con=np.uint8(255*np.uint8(img[:,:,2]>100)*np.uint8(img[:,:,1]<100)*np.uint8(img[:,:,0]<100))

	# draw contours
	contours,_=cv2.findContours(con,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	# sorting wrt area
	c=sorted(contours,key=cv2.contourArea)

	# drawing a polygon
	epsilon = 0.1*cv2.arcLength(c[-2],True)
	a = cv2.approxPolyDP(c[-2],epsilon,True)

	# finding the corners of polygon in order
	box=[a[0][0],a[1][0],a[2][0],a[3][0]]
	box=sorted(box,key=lambda x:x[1])
	if box[0][0]>box[1][0]:
		box[0],box[1]=box[1],box[0]
	if box[2][0]>box[3][0]:
		box[2],box[3]=box[3],box[2]
	i=1
	box=np.array(box)
	box+=np.array([[i,i],[-i,i],[i,-i],[-i,-i]])

	# Cropping
	pts1 = np.float32(box)
	pts2 = np.float32([[0,0],[480,0],[0,480],[480,480]])
	M = cv2.getPerspectiveTransform(pts1,pts2)
	dst = cv2.warpPerspective(img,M,(480,480))

	return dst

if __name__=="__main__":
	c=cv2.imread("shot1.jpg")
	z=crop(c)
	color,intensity=detect(z)
	print(color)
	print(intensity)
	cv2.imshow("image",z)
	cv2.imshow("img",c)
	cv2.waitKey(0)

