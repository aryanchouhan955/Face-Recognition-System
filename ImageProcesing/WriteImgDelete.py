import cv2 as cv
import os

FolderPath = r"D:\OpenCVProject\FaceRecg\Yash"

for item_name in os.listdir(FolderPath):
    path = os.path.join(FolderPath, item_name)
    img = cv.imread(path)

    if img is not None and img.shape[0] > 1080:
        scale = 1080.0 / float(img.shape[0])
        new_width = int(img.shape[1] * scale)
        img_resized = cv.resize(img, (new_width, 1080))

        resized_path = os.path.join(FolderPath, f"{os.path.splitext(item_name)[0]}_resized{os.path.splitext(item_name)[1]}")
        cv.imwrite(resized_path, img_resized)

       

print("cc")