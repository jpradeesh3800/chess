import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def detect(img):
	img=cv2.merge(list(map(cv2.equalizeHist,cv2.split(img))))
	orange=np.uint8(np.int32(img[:,:,2]>130)*np.int32(img[:,:,1]<150)*np.int32(img[:,:,0]<150))
	yellow=np.uint8(np.int32(img[:,:,2]>130)*np.int32(img[:,:,1]>130)*np.int32(img[:,:,0]<150))
	color=[]
	intensity=[]
	factor=20
	for i in range(8):
		k=[]
		for j in range(8):
			y=np.sum(yellow[60*(i):60*(i+1),60*(j):60*(j+1)])
			o=np.sum(orange[60*(i):60*(i+1),60*(j):60*(j+1)])	

			if y>o and y>factor:
				r="y"
			elif o>y and o>factor:
				r="o"
			else:
				r="e"
			
			intensity.append((o,y))
			k.append(r)
		color.append(k)

	color=pd.DataFrame(color,index=list("87654321"),columns=list("abcdefgh"))
	return color,intensity		

def display(img):
	b,g,r=cv2.split(img)
	img=cv2.merge((r,g,b))
	fig=plt.figure(figsize=(8, 8))
	for i in range(8):
		for j in range(8):
			fig.add_subplot(8, 8, 8*(i)+j+1)
			plt.imshow(img[60*(i):60*(i+1),60*(j):60*(j+1),:])
	plt.show()

if __name__=="__main__":
	frame=cv2.imread("shit.jpg")
	color,intensity=detect(frame)
	print(color)
	display(frame)
