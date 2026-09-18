import cv2 as cv
import numpy as np

car = cv.imread("C:\\Python\\OpenCV\\Images\\h1.jpg")
img = cv.resize(car, (1080, 721), interpolation= cv.INTER_CUBIC )

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny = cv.Canny(img, 125, 175)

# Thresholding
ret, thres = cv.threshold(gray, 125, 225, cv.THRESH_BINARY) 
cv.imshow('thres', thres)
cv.waitKey()

#                                      (img    , mode       , method             )
counturs, hierarchies = cv.findContours(thres, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# counturs: list of all the coordinates of counturs, hierarchies: h of c

blank= np.zeros(img.shape, dtype='uint8')
cv.drawContours(blank, counturs, -1, (0, 255, 0   ), 1)
cv.imshow('countor', blank)
cv.waitKey()

print(f'no. of countur points: {len(counturs)}')
print("code successfully run")