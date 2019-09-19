import cv2
video = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
	ret, frame = video.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	rects= detector.detectMultiScale(gray,scaleFactor=1.3,minSize=(30, 30))
	for(i,(x,y,w,h))in enumerate (rects):
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)	
	cv2.imshow("Faces Of Humans",frame)
	k=cv2.waitKey(1)
	if k==27:
		break



