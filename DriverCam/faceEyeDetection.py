
import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml') #dataset provided by opencv to detect face 
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')#to detect eyes
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()   #reading an image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)# converting into gray code because its 2 balck and white
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  #it finds faces! 4 cordinates bnege x,y,w,h 2 parameter passs hote 1 scaleFactor — Parameter specifying how much the image size is reduced at each image scale.
                                                        #minNeighbors — Parameter specifying how many neighbors each candidate rectangle should have to retain it.
 
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
