import cv2 as cv
import numpy as np
import sys

img = cv.imread(r"D:\OpenCVProject\FaceRecg\Aryan\IMG_20240728_173810_resized_resized.jpg")
if img is None:
    print("img not found")
    sys.exit()

cv.imshow('img', img)
cv.waitKey()

img = img[0: 500, 0:500]
cv.imshow('img', img)
cv.waitKey()

# adding border to img
bordered_img = cv.copyMakeBorder(img, 20, 20, 20, 20, cv.BORDER_CONSTANT, value=[0, 200, 0])
cv.imshow('bordered_img', bordered_img)
cv.waitKey()

bordered_img = cv.copyMakeBorder(img, 40, 40, 40, 40, cv.BORDER_REFLECT)
cv.imshow('bordered_img', bordered_img)
cv.waitKey()

bordered_img = cv.copyMakeBorder(img, 40, 40, 40, 40, cv.BORDER_REPLICATE)
cv.imshow('bordered_img', bordered_img)
cv.waitKey()

print("cc")