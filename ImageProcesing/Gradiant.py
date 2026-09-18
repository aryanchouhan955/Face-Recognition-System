import cv2 as cv
import numpy as np

img = cv.imread("C:\\Python\\OpenCV\\Images\\h1.jpg")
if img is None:
    print("img not found")
    exit()
cv.imshow('img', img)
print(img.shape)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('lap', lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
 
cv.imshow('sobelx', sobelx)
cv.imshow('sobely', sobely)

combined = cv.bitwise_or(sobelx, sobely)
cv.imshow('combined', combined)

# canny (most adavanced edge detection)
canny = cv.Canny(gray, 80, 180)
cv.imshow('canny', canny)

cv.waitKey(0)
