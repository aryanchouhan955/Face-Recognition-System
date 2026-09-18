import cv2 as cv

img = cv.imread(r"C:\Python\OpenCV\Images\h1.jpg")

# method 1
def reScale(img, scale: float):
    return cv.resize(img, (int(img.shape[1]*scale), int(img.shape[0]*scale)) )

scaled = reScale(img, 2)

cv.imshow('img', img)
cv.imshow('scaled', scaled)

# method 2

scaled = cv.pyrDown(img )

cv.imshow('scaled down', scaled)

scaled = cv.pyrUp(img, scaled )

cv.imshow('scaled up', scaled)

cv.waitKey()



print("cc")