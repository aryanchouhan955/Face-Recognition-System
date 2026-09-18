import cv2 as cv

capture = cv.VideoCapture("D:\\OpenCVProject\\Videos\\ElephantV25fps.mp4")

def resize(frame,scale):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width, height)
    resizedFrame = cv.resize(frame, dimension, interpolation=cv.INTER_AREA)
    return resizedFrame

while True:
    isTrue, frame = capture.read()
    resized_frame = resize(frame, 0.5)
    if not isTrue:
        break
    cv.imshow("Video", resized_frame)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
