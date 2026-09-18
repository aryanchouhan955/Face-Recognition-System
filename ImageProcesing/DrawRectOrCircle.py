import cv2 as cv
import numpy as np

color_img = np.zeros((500,800,3), dtype='uint8')

color_img[:] = 0,255,0
cv.imshow('color Image', color_img)
cv.waitKey()

#  rectangle
#                       (x0, y0) (x0+dx, y0+dy)        for -1 thickness=cv.filled
cv.rectangle(color_img, (0,100), (100,200), (0,0,255), thickness=2)
cv.imshow('color Image with ractangle', color_img)
cv.waitKey()

cv.rectangle(color_img, (0,100), (100,200), (0,0,255), thickness=-1)
cv.imshow('color Image with filled ractangle', color_img)
cv.waitKey()

#  circle
#                    (x0 ,                   y0)                     r         
cv.circle(color_img, (color_img.shape[1]//2, color_img.shape[0]//2), 20 , (0,0,255), thickness=3)
cv.imshow('color Image with filled ractangle', color_img)
cv.waitKey()

#  line
#                  (x0,y0) (x1,y1)
cv.line(color_img, (0,0), (400,250), (0,0,255), thickness=2 )
cv.imshow('color Image with line', color_img)
cv.waitKey()

# Text

cv.putText(color_img, "By AR", (0,400), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), thickness=2)
cv.imshow('color Image with txt', color_img)
cv.waitKey()

print("Code runs succesfully")