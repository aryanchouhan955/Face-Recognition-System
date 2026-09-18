import cv2 as cv

img = cv.imread("C:\\Python\\OpenCV\\Images\\h1.jpg")
if img is None:
    print("img not found")
    exit()
cv.imshow('img', img)
print(img.shape)
cv.waitKey()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
cv.waitKey()

# Simple thresholding 

threshold, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)
cv.waitKey()

# inverse thresholding 

threshold, inv = cv.threshold(gray, 125, 255, cv.THRESH_BINARY_INV)
cv.imshow('inverse', inv)
cv.waitKey()

# Adaptive thresholding
#                               max,                mean of neighbour pixels  ,  block size, bias that is added to mean
ad = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 7,  -255)
cv.imshow('adaptive', ad)
cv.waitKey()