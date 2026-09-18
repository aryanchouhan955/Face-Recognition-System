import cv2 as cv

img = cv.imread("C:\\Python\\OpenCV\\Images\\h1.jpg")
if img is None:
    print("Image is not found")
    exit()
cv.imshow('image', img)
cv.waitKey()
print(img.shape)

# Intensity of central pixel =  Average of intensity of pixels of block sorounding the cetral pixel
#                 Kernal size = (length, width) of block of pixels 
average = cv.blur(img, (5,5))
cv.imshow('average', average)
cv.waitKey()
print(average.shape)

# by taking weighted avg of intensity of pixels of block sorounding the cetral pixel
#                 Kernal size = (length, width) of block of pixels 
gauss = cv.GaussianBlur(img, (5,5), 0)
cv.imshow('gauss', gauss)
cv.waitKey()


# by taking median of intensity of pixels of block sorounding the cetral pixel
#                 Kernal size = (length, width) of block of pixels 
median = cv.medianBlur(img, 5)
cv.imshow('median', median)
cv.waitKey()

# bilateral: less effecting edge of img
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bilateral', bilateral)
cv.waitKey()

print("Mubarakho")