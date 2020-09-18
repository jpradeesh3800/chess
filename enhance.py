import cv2
import numpy as np

img=cv2.imread("chess1.jpg")

enh=cv2.merge(list(map(cv2.equalizeHist,cv2.split(img))))

cv2.imshow("image",enh)
cv2.waitKey(0)
