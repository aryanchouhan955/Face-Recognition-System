import numpy as np
import cv2 as cv
import os

DIR = r"D:\OpenCVProject\FaceRecg"
people_name = os.listdir(DIR)

haar_cascade = cv.CascadeClassifier(r'C:\Python\OpenCV\BasicProjects\Harr_Cascade.xml')
if haar_cascade is None:
    print("Cascade is not found")
    exit()

face_recognizer = cv.face.LBPHFaceRecognizer.create()
face_recognizer.read(r'C:\Python\OpenCV\BasicProjects\face_trained.yml')


img = cv.imread(r"D:\OpenCVProject\testing img\SA1.jpg")
cv.imshow('img',img)
cv.waitKey()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in face_rect:
    roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(roi)
    print(f'label = {people_name[label]} with confidance = {confidence}')

    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
    cv.putText(img, people_name[label] + f" with confidance = {int(confidence)} %", (x,y), cv.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
    
cv.imshow('img',img)
cv.waitKey()
