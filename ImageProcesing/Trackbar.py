import cv2 as cv
import numpy as np 

cv.namedWindow("Window")
def nothing(x):
    pass
cv.createTrackbar("R", "Window", 0, 255, nothing)
cv.createTrackbar("G", "Window", 0, 255, nothing)
cv.createTrackbar("B", "Window", 0, 255, nothing)
while True:
    R = cv.getTrackbarPos("R", "Window")
    G = cv.getTrackbarPos("G", "Window")
    B = cv.getTrackbarPos("B", "Window")

    color = np.zeros((500, 500, 3), dtype='uint8')
    color[:] = B, G, R
    cv.imshow('color', color)

    if cv.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cv.destroyAllWindows()
cv.destroyAllWindows()

print("cc")