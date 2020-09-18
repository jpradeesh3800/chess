import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

fig=plt.figure(figsize=(8, 8))
img=cv2.resize(img,(480,480))

red=np.uint8(255*np.int32(img[:,:,2]>200)*np.int32(img[:,:,1]<50)*np.int32(img[:,:,0]<50))
orange=np.uint8(np.int32(img[:,:,2]>150)*np.int32(img[:,:,1]<120)*np.int32(img[:,:,0]<120))
yellow=np.uint8(np.int32(img[:,:,2]>150)*np.int32(img[:,:,1]>150)*np.int32(img[:,:,0]<120))

columns = 8
rows = 8
color=[]
for i in range(rows):
	for j in range(columns):
		#x=img[60*(i):60*(i+1),60*(j):60*(j+1),:]

		y=np.sum(yellow[60*(i):60*(i+1),60*(j):60*(j+1)])
		o=np.sum(orange[60*(i):60*(i+1),60*(j):60*(j+1)])	

		if y>o and y>80:
			r="y"
		elif o>y and o>80:
			r="o"
		else:
			r="e"

		color.append(r)
		fig.add_subplot(rows, columns, 8*(i)+j+1)
		plt.imshow(img[60*(i):60*(i+1),60*(j):60*(j+1),:])
print(color)
#plt.show()
cv2.imshow("image",img)
cv2.waitKey(0)
plt.show()
