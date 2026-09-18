import cv2 as cv
import numpy as np
import os

# Use OpenCV's built-in cascade path
harr_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
if harr_cascade.empty():
    print("Haar Cascade not loaded")
    exit()
DIR = r"D:\OpenCVProject\FaceRecg"
people_name = os.listdir(DIR)

labels = []
features = []

def Train():
    for person in people_name:
        folder_path = os.path.join(DIR, person)
        label = people_name.index(person)

        for img_name in os.listdir(folder_path):
            img_path = os.path.join(folder_path, img_name)

            img = cv.imread(img_path)
            if img is None:
                continue
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            face_rect = harr_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
            for (x, y, w, h) in face_rect:
                cropped = gray[y:y+h, x:x+w]
                resized = cv.resize(cropped, (200, 200))  # Resize to 200x200
                features.append(resized)
                labels.append(label)

Train()
print(len(labels))
print(len(features))

features = np.array(features)
labels = np.array(labels)
np.save('features.npy', features)
np.save('labels.npy', labels)


print("cc")
