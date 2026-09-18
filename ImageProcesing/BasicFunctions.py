import cv2 as cv

img = cv.imread("C:\\Python\\OpenCV\\Images\\car.png")
cv.imshow('flag',img)
cv.waitKey()

# resizing
resized = cv.resize(img, (1080,720))
cv.imshow('resized',resized)
cv.waitKey()

# grayscale
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('gray ',gray)
cv.waitKey()

# blur
blur = cv.blur(resized, (7,7))
cv.imshow('blur ',blur)
cv.waitKey()

# edge cascade
canny = cv.Canny(resized,0,100)
cv.imshow('canny ',canny)
cv.waitKey()

# dilating
dialated = cv.dilate(canny, (9,9), iterations=3)
cv.imshow('dialated ',dialated)
cv.waitKey()

# eroded
eroded = cv.erode(canny, (9,9), iterations=3)
cv.imshow('erroded ',eroded)
cv.waitKey()

# croping
croped = resized[100:500, 200:600]
cv.imshow('croped ',croped)
cv.waitKey()

print("code run succesfully")