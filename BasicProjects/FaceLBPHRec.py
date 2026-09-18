import numpy as np
import cv2 as cv

features = np.load(r'C:\Python\features.npy')
labels = np.load(r'C:\Python\labels.npy')
face_recognizer = cv.face.LBPHFaceRecognizer.create()
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')

print("cc")