import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread('C:\\Users\\COMPUTER WORLD\\Desktop\\ITCppt\\Picture1.png', cv2.IMREAD_GRAYSCALE)

# Check if the pixel is black or white
# for i in range(image.shape[1]):
  # Iterate over the width of the image
i = 271
row_in_binary = ''
for j in range(image.shape[0]):  # Iterate over the height of the image
    if image[j, i] <= 225:  # Access pixels correctly using (row, column)
        row_in_binary += '1'  # Append '1' for black pixels
    else:
        row_in_binary += '0'  # Append '0' for white pixels

print(f"{i}th row:{row_in_binary}")
        