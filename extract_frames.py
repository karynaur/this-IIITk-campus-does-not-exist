import cv2

vid=cv2.VideoCapture('Pranjal IIIT.mp4')
i=0
while(vid.isOpened()):
   ret,frame=vid.read()
   if ret==False:break
   cv2.imwrite('iiitk'+str(i)+'.jpg',frame)
   i+=1
vid.release()
cv2.destroyAllWindows()
