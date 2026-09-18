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

capture = cv.VideoCapture(0)
fps = capture.get(cv.CAP_PROP_FPS)

if fps == 0:
    fps = 25  # fallback to a default value if FPS is not available

second = 0.0
delay = 1 / fps

while True:
    # Read a frame from the video; isTrue is True if frame is read correctly

    isTrue, img = capture.read()
    if not isTrue:
        break
    
    img = cv.flip(img, 1)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in face_rect:
        roi = gray[y:y+h, x:x+w]

        label, confidence = face_recognizer.predict(roi)

        cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        cv.putText(img, people_name[label] + f" with confidance = {int(confidence)} %", (x,y), cv.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 1)
    

    cv.putText(img, str(second), (100,100), 0, 1, (0,255,0), thickness= 3)
    cv.imshow("Video", img)
    second += delay
    if (cv.waitKey(1) & 0xFF == ord('q')) :
        break
    
    
print(second)



# Release the video capture object
capture.release()
# Close all OpenCV windows
cv.destroyAllWindows()


