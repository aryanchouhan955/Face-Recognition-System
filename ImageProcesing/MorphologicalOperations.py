import cv2 as cv
import numpy as np


blank = np.zeros((500, 500), dtype= 'uint8')
# img = cv.putText(img, "AR", (250, 250), 0, 4, 255, 10)

# img = cv.putText(img, ".", (20, 20), 0, 1, 255, 1)
# img = cv.putText(img, ".", (40, 40), 0, 1, 255, 1)
# img = cv.putText(img, ".", (400, 400), 0, 1, 255, 1)
# img = cv.putText(img, ".", (200, 20), 0, 1, 255, 1)

img = cv.imread(r"C:\Python\OpenCV\Images\AryTxtT.png")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, img = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
img = cv.bitwise_not(img)

cv.imshow("img", img)



matrix = np.ones((7,7), np.int8)

# Erosion: reduce thickness of white lines
# Dilation: increase thickness of white lines
diluted = cv.dilate(img, matrix)
cv.imshow('diluted',diluted)

eroded = cv.erode(img, matrix)
cv.imshow('eroded',eroded)
 
# Opening operation: erosion after dilution >> It converts isolated white pixels to black

opening = cv.morphologyEx(img, cv.MORPH_OPEN, matrix)
cv.imshow('opening',opening)

# Closing operation: dilution after erosion >> It converts isolated black pixels to white

closing = cv.morphologyEx(img, cv.MORPH_CLOSE, matrix)
cv.imshow('closing',closing)

cv.waitKey()
cv.destroyAllWindows()
print("cc")