import cv2 as cv
import numpy as np

#                    (H,   W)         data type of image 
blank_img = np.zeros((500,800), dtype='uint8')

height = blank_img.shape[0]
width = blank_img.shape[1]
print(f"H = {height}, W = {width}")

cv.imshow('Blank Image', blank_img)
cv.waitKey()

#                    (H  ,W  , no. of color in rgb)
color_img = np.zeros((500,800,3), dtype='uint8')

color_img[:] = 255,0,0
cv.imshow('color Image', color_img)
cv.waitKey()

#        x0 to x0+dx y0 to y0+dy
color_img[0 : 200, 0:400] = 0,0,255
cv.imshow('color Image', color_img)
cv.waitKey()

print("Code runs succesfully")
