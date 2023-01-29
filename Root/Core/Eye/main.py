import cv2
import pathlib

moin = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"
Data = cv2.CascadeClassifier(str(moin))

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = Data.detectMultiScale(gray, 1.5, 2)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
cap.release()