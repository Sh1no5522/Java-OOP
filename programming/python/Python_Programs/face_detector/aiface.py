#import numpy as np
import cv2

cam = cv2.VideoCapture(0)
faces = cv2.CascadeClassifier(r'C:\Users\FSOS\Downloads\Programming-20250917T165746Z-1-001\Programming\python\Python_Programs\haarcascade_frontalcatface_extended.xml')

while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    results = faces.detectMultiScale(gray, scaleFactor= 1.05 , minNeighbors= 3)
    for (x,y,w,h) in results:
        cv2.rectangle(frame, (x,y-50), (x + w , y + h + 50), (0, 0, 255), thickness= 2)
    cv2.imshow("CamDet", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()