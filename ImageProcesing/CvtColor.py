import cv2 as cv

temp = cv.imread("C:\\Python\\OpenCV\\Images\\h1.jpg")
if temp is None:
    print("Image is not found")
    import sys

img = cv.resize(temp, (1080,721), interpolation=cv.INTER_CUBIC)


# In opencv color vector sequence B G R
cv.imshow('horse', img)
cv.waitKey()

# In all other lib seq: R G B

from matplotlib import pyplot as plt
plt.imshow(img)
plt.title('horse')
plt.axis('off')
plt.waitforbuttonpress()

# converting BGR to RGB
im = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(im)
plt.title('horse')
plt.axis('off')
plt.waitforbuttonpress()

# converting BGR to LAB
im = cv.cvtColor(img, cv.COLOR_BGR2LAB)
plt.imshow(im)
plt.title('horse')
plt.axis('off')
plt.waitforbuttonpress()

# converting BGR to HSV
im = cv.cvtColor(img, cv.COLOR_BGR2HSV)
plt.imshow(im)
plt.title('horse')
plt.axis('off')
plt.waitforbuttonpress()

# converting BGR to LAB
im = cv.cvtColor(img, cv.COLOR_BGR2LAB)
plt.imshow(im)
plt.title('horse')
plt.axis('off')
plt.waitforbuttonpress()


# converting gray to BGR
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
cv.waitKey()

# converting gray to BGR
image = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow('gray to color img',image)
cv.waitKey()

cv.destroyAllWindows()
print("CC")