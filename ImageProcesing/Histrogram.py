import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("C:\\Python\\OpenCV\\Images\\h1.jpg")
if img is None:
    print("img not found")
    exit()
cv.imshow('img', img)
print(img.shape)
cv.waitKey()

# histogram plot: pixel intesity distribution // no. of pixel vs intensity

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
cv.waitKey()


gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

plt.figure()
plt.title('Gray img Histogram')
plt.xlabel('Intensity')
plt.ylabel('Number of pixels')
plt.plot(gray_hist)
plt.show()


# color intensity of pixel 

B_hist = cv.calcHist([img], [0], None, [256], [0,256])
G_hist = cv.calcHist([img], [1], None, [256], [0,256])
R_hist = cv.calcHist([img], [2], None, [256], [0,256])

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.plot(B_hist, color = 'blue', label='Blue')
plt.plot(G_hist, color = 'green', label='Green')
plt.plot(R_hist, color = 'red', label='Red')
plt.legend()
plt.show()




print("cc")