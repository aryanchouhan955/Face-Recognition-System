import cv2 as cv
import numpy as np


image = cv.imread(r"D:\ma.jpg")
image = cv.resize(image, (image.shape[1]//6, image.shape[0]//6))

if image is None:
    print("Error: Image not found or path is incorrect.")
else:
    cv.imshow("Window", image)
    cv.waitKey()
    grayscale_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("Window", grayscale_img)
    cv.waitKey()


    print(len(image))
    print(image.shape)

    # doubling horizontally
    h = np.hstack((image,image))
    cv.imshow('h',h)

    # doubling vertically
    v = np.vstack((image,image))
    cv.imshow('v',v)




    cv.waitKey()





print("Code Completed")