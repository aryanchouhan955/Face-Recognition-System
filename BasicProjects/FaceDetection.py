import cv2 as cv

img = cv.imread(r"D:\OpenCVProject\FaceRecg\Aryan\IMG_20240811_151005_resized_resized.jpg")
if img is None:
    print("Img is not found")
    exit()

img = cv.resize(img, (img.shape[1], img.shape[0]))
cv.imshow('img', img)
cv.waitKey()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
cv.waitKey()

haar_cascade = cv.CascadeClassifier(r'C:\Python\OpenCV\BasicProjects\Harr_Cascade.xml')
if haar_cascade is None:
    print("Cascade is not found")
    exit()
                                                        #  optimum values for best results
face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
print(f'Number of face detected = {len(face_rect)}')

for (x,y,w,h) in face_rect:
    cv.rectangle(img, (x,y), (x+w, y+h),(0,255,0))

cv.imshow('detected faces', img)
cv.waitKey()
print("cc")
