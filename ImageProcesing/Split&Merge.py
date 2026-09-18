import cv2 as cv

img = cv.imread("C:\\Python\\OpenCV\\Images\\h1.jpg")
cv.imshow('Image', img)
cv.waitKey()

# spliting into b,g,r
b, g, r = cv.split(img)

cv.imshow('blue intensity', b)
cv.waitKey()

cv.imshow('green intensity', g)
cv.waitKey()

cv.imshow('red intensity', r)
cv.waitKey()

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merging
merged = cv.merge([b,g,r])
cv.imshow('merged', merged)
cv.waitKey()

# spliting into blue, green, red images
import numpy as np
blank = np.zeros(img.shape[:2], dtype="uint8")
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('blue', blue)
cv.waitKey()
cv.imshow('green', green)
cv.waitKey()
cv.imshow('red', red)
cv.waitKey()

cv.destroyAllWindows()
print("CC")