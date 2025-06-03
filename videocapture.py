import cv2
cap = cv2.VideoCapture(0)
while True:
  key,imgc = cap.read()
  cv2.imshow('test video',imgc)
  cv2.waitKey(1)
