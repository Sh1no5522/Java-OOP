import cv2

img = cv2.imread(r'C:\Users\Sh1nO\Documents\Programming\python\Python_Programs\plate_detector\i-_2_.jpg')
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
plates = cv2.CascadeClassifier(r'C:\Users\Sh1nO\Documents\Programming\python\Python_Programs\plate_detector\ai.xml')
results = plates.detectMultiScale(gray, scaleFactor= 1.05 , minNeighbors= 1)
for (x,y,w,h) in results:
    cv2.rectangle(img, (x,y), (x + w , y + h), (0, 0, 255), thickness= 3)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()