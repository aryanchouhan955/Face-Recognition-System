import cv2 as cv
import numpy as np 

cap = cv.VideoCapture(0)

cv.namedWindow("Window")
def nothing(x):
    pass

cv.createTrackbar("Thr", "Window", 0, 255, nothing)
cv.createTrackbar("LR", "Window", 0, 255, nothing)
cv.createTrackbar("LG", "Window", 0, 255, nothing)
cv.createTrackbar("LB", "Window", 0, 255, nothing)

cv.createTrackbar("UR", "Window", 0, 255, nothing)
cv.createTrackbar("UG", "Window", 0, 255, nothing)
cv.createTrackbar("UB", "Window", 0, 255, nothing)

while cap.isOpened():

    found, frame = cap.read()
    if found is False:
        break
    
    Thr = cv.getTrackbarPos("Thr", "Window")

    LR = cv.getTrackbarPos("LR", "Window")
    LG = cv.getTrackbarPos("LG", "Window")
    LB = cv.getTrackbarPos("LB", "Window")

    UR = cv.getTrackbarPos("UR", "Window")
    UG = cv.getTrackbarPos("UG", "Window")
    UB = cv.getTrackbarPos("UB", "Window")

    lower = np.array([LB, LG, LR])
    upper = np.array([UB, UG, UR])

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Create a mask for the specified color
    m = cv.inRange(hsv, lower, upper)

    # Bitwise-AND mask and original image to extract the color region
    res = cv.bitwise_and(frame, frame, mask=m)

    # Apply threshold to the mask for contour detection
    _, threshold_img = cv.threshold(m, Thr, 255, cv.THRESH_BINARY)

    # Find contours in the thresholded mask
    cnt, hr = cv.findContours(threshold_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # Draw contours on the original frame
    cv.drawContours(frame, cnt, -1, (255, 0, 0), 2)

    # Display the result
    cv.imshow('Frame', frame)
    cv.imshow('Mask', m)
    cv.imshow('Result', res)

    # Exit on 'q' key
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cv.destroyAllWindows()

print("cc")