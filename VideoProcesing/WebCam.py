import cv2 as cv  # Import the OpenCV library

# 0 is used for webCam
# 1 is for external cam
capture = cv.VideoCapture(0)
fps = capture.get(cv.CAP_PROP_FPS)

if fps == 0:
    fps = 25  # fallback to a default value if FPS is not available

second = 0.0
delay = 1 / fps

while True:
    # Read a frame from the video; isTrue is True if frame is read correctly

    isTrue, frame = capture.read()
    if not isTrue:
        break

    # Resize for faster display (optional)
    frame = cv.resize(frame, (1280, 720))
    frame = cv.flip(frame, 1)
    cv.putText(frame, str(second), (100,100), 0, 1, (0,255,0), thickness= 3)
    cv.imshow("Video", frame)


    second += delay

    if (cv.waitKey(1) & 0xFF == ord('q')) :
        break
    
    
print(second)



# Release the video capture object
capture.release()
# Close all OpenCV windows
cv.destroyAllWindows()
