import cv2 as cv
import numpy as np

img = cv.imread(r"D:\OpenCVProject\FaceRecg\Aryan\IMG_20240728_173810_resized_resized.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


print(img.shape)
print(len(img[0][0]))
print(len(gray[0]))
print(gray)

vec = [[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]]
vec = np.array(vec)
print(vec.shape)

resized = cv.resize(img, (500, 500))
cv.imshow('resized', resized)
cv.imshow('img', img)

rotation = cv.rotate(resized )
cv.imshow('rotation', rotation)

cv.waitKey()

print("cc")