import cv2 as cv
import numpy as np

img = cv.imread("C:\\Python\\OpenCV\\Images\\h1.jpg")
cv.imshow('img', img)
cv.waitKey()

blank = np.zeros(img.shape[:2], dtype='uint8')
circle = cv.circle(blank, (540,360), 250, 255, thickness=-1)
cv.imshow('circle', circle)
cv.waitKey()



# masking
masked_img = cv.bitwise_and(img, img, mask=circle)
cv.imshow('masked_img', masked_img)
cv.waitKey()
 
print("cc")
