import cv2
image = cv2.imread('C:\\Users\\COMPUTER WORLD\\Desktop\\ITCppt\\flawer1.png', cv2.IMREAD_GRAYSCALE)
print(image.shape[1])
print(image.shape[0])