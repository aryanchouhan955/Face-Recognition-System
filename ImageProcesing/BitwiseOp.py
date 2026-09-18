import cv2 as cv
import numpy as np

#  taking 3 channel blank img
blank = np.zeros((400,400,3), dtype='uint8')

rect = cv.rectangle(blank.copy(), (20,20), (380,380), (255,0,0), thickness=-1)
cir = cv.circle(blank.copy(), (200, 200), 200, (100,255,0), thickness=-1)
cv.imshow('rect', rect)
cv.imshow('cir', cir)
cv.waitKey()

# AND --> taking common color
bitwise_and = cv.bitwise_and(rect, cir)
cv.imshow('bitwise_and', bitwise_and)
cv.waitKey()

# OR --> adding color
bitwise_or = cv.bitwise_or(rect, cir)
cv.imshow('bitwise_or', bitwise_or)
cv.waitKey()

# xor --> non intersecting region
bitwise_xor = cv.bitwise_xor(rect, cir)
cv.imshow('bitwise_xor', bitwise_xor)
cv.waitKey()
 
# not --> flipping : (b,g,r)--->(255-b,255-g,255-r)
bitwise_not = cv.bitwise_not(rect)
cv.imshow('bitwise_not', bitwise_not)
cv.waitKey()

temp = cv.rectangle(blank.copy(), (20,20), (380,380), (0,255,255), thickness=-1)
cv.imshow('temp', temp)
cv.waitKey()


print("cc")