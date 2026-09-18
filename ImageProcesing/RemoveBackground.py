import cv2 as cv
import numpy as np

# Load the original image
img = cv.imread(r"C:\Python\OpenCV\Images\greenScreen.jpg")
if img is None:
    raise FileNotFoundError("Image not found at the specified path.")

# Show the original image
cv.imshow('Original Image', img)

# Crop a region that only contains green background (top-left part here)
# This region will be used as a reference for what "green background" looks like
crop = img[0:200, 0:200]  # Adjust the size if your green screen area is different

# Convert the full image and the crop to HSV color space
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV Image', hsv)

hsv1 = cv.cvtColor(crop, cv.COLOR_BGR2HSV)
cv.imshow('HSV Crop (Green Background)', hsv1)

# Calculate the color histogram of the green background crop
# Channels: 0-Hue, 1-Saturation; HistSize: 180 bins for Hue, 256 for Saturation
# Ranges: H = [0,180], S = [0,256]
hist = cv.calcHist([hsv1], [0, 1], None, [180, 256], [0, 180, 0, 256])

# Use backprojection to find all pixels in the image that match the green background
# It gives a probability map where brighter pixels are more likely to match the background
mask = cv.calcBackProject([hsv], [0, 1], hist, [0, 180, 0, 256], 1)

# Apply convolution with elliptical kernel to smooth the mask (reduce noise)
ker = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
mask = cv.filter2D(mask, -1, ker)

# Threshold the mask to get a binary image
# Only keep strong matches (background pixels) above threshold 200
_, thr = cv.threshold(mask, 200, 255, cv.THRESH_BINARY)

# Convert single-channel mask to 3-channel to match image dimensions
mask3 = cv.merge((thr, thr, thr))

# Use the mask to remove the green background from the original image
result = cv.bitwise_or(img, mask3)

# Show the intermediate and final results
cv.imshow("Thresholded Mask", thr)
cv.imshow("Final Mask (3 Channel)", mask3)
cv.imshow("Result", result)

# Wait until any key is pressed, then close all windows
cv.waitKey(0)
cv.destroyAllWindows()

