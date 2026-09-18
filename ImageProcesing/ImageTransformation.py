import cv2 as cv

car = cv.imread("C:\\Python\\OpenCV\\Images\\car.png")


# resizing 
img = cv.resize(car, (1280, 720), interpolation= cv.INTER_CUBIC )

cv.imshow('car', img)
cv.waitKey()

# rotation

def rotate(image, angle, pivot=None, scale=1.0):
    (h, w) = image.shape[:2]
    if pivot is None:
        pivot = (w // 2, h // 2)
    # Get the rotation matrix
    M = cv.getRotationMatrix2D(pivot, angle, scale)
    # Perform the rotation
    rotated = cv.warpAffine(image, M, (w, h))
    return rotated


rotated_img = rotate(img, -45)

cv.imshow('rotated car', rotated_img)
cv.waitKey()

# flipping
# 1 horizontal flip
# 0 vertical flip
# -1 both simultaniously
flip = cv.flip(img, -1)
cv.imshow('flip car', flip)
cv.waitKey()

print("code successfully run")

