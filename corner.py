import cv2
import numpy as np

img=cv2.imread("chess1.png")
l,b,h=np.shape(img)
con=np.zeros((l,b))
con=np.uint8(255*np.int32(img[:,:,2]>200)*np.int32(img[:,:,1]<50)*np.int32(img[:,:,0]<50))
contours,_=cv2.findContours(con,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

(x,y,w,h)=cv2.boundingRect(min(contours,key=cv2.contourArea))
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
print(x,y,w,h)
print(l,b,h)

cv2.imshow("image",img)
cv2.waitKey(0)
