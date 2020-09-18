def capture():
	cap=cv2.VideoCapture(4)
	
	while True:

		_,frame=cap.read()
		print(_)
		img=crop(frame)
		color2=detect(img)
		#cv2.imshow("1",frame)
		#cv2.imshow("2",img)
		#cv2.waitKey(0)
		return color2

