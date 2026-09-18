# Face Recognition System

This project is a beginner-friendly OpenCV face recognition workflow built in Python. It demonstrates how to:

- detect human faces in images using Haar Cascade
- collect face samples from labeled folders
- train an LBPH face recognizer
- recognize faces in new images

The project is organized around a simple learning pipeline and uses OpenCV's built-in computer vision tools.

---

## Project Structure

```text
OpenCV/
│
├── BasicProjects/
│   ├── FaceDetection.py
│   ├── FaceLBPHRec.py
│   ├── RecognizeFace.py
│   ├── TrainingRecognizer.py
│   ├── Harr_Cascade.xml
│   └── face_trained.yml
│
├── Basics/
├── ImageProcesing/
├── Images/
├── MyIdea/
├── VideoProcesing/
├── temp.ipynb
└── README.md
```

---

## Workflow Overview

The complete system works in four major stages:

### 1) Face Detection
The first step is to detect a face from an image or webcam frame.

- `BasicProjects/FaceDetection.py` loads an image
- converts it to grayscale
- uses `cv.CascadeClassifier()` with Haar cascade XML
- finds face regions using `detectMultiScale()`
- draws rectangles around detected faces

This step confirms that the face detection model is working before training or recognition begins.

### 2) Data Collection / Training Preparation
The system then prepares labeled face data for training.

- the project expects folders containing different people
- each folder represents one person/class name
- the script reads all images inside those folders
- each image is converted to grayscale
- the face is cropped using the detected coordinates
- every face is resized to a fixed size
- image features and labels are saved into NumPy arrays

Relevant script:

- `BasicProjects/TrainingRecognizer.py`

It creates arrays like:

- `features.npy`
- `labels.npy`

These arrays become the training data used by the recognizer.

### 3) Model Training
Once face samples are collected, the LBPH recognizer is trained.

- `FaceLBPHRec.py` loads the feature and label arrays
- creates an LBPH face recognizer using `cv.face.LBPHFaceRecognizer.create()`
- calls `train(features, labels)`
- saves the trained model as `face_trained.yml`

This file is the final trained model used for recognition.

### 4) Face Recognition
After training, the model can predict the identity of a face in a new image.

- `BasicProjects/RecognizeFace.py` loads a test image
- detects faces in the image
- crops each detected face
- passes the face ROI into the trained LBPH recognizer
- returns a label and confidence score
- draws a bounding box and labels the person on the image

This is the final recognition stage of the project.

---

## How the Project Works in Simple Terms

The project follows this flow:

1. Load a face image
2. Detect the face area
3. Crop the face
4. Save it as a training sample
5. Repeat for multiple people
6. Train the model with all face samples
7. Test the model on a new image
8. Predict who the face belongs to

This is a classic supervised face recognition pipeline using OpenCV + machine learning.

---

## Main Files and Their Purpose

### `BasicProjects/FaceDetection.py`
Tests face detection on a single image.

### `BasicProjects/TrainingRecognizer.py`
Collects all detected faces from labeled folders and prepares the training dataset.

### `BasicProjects/FaceLBPHRec.py`
Trains the LBPH face recognizer and stores the trained model in `face_trained.yml`.

### `BasicProjects/RecognizeFace.py`
Recognizes faces in a new test image and displays the predicted identity.

### `BasicProjects/Harr_Cascade.xml`
The Haar cascade file used for detecting faces.

### `BasicProjects/face_trained.yml`
Stored trained recognizer model.

---

## Required Libraries

Install the required Python packages:

```bash
pip install opencv-python numpy
```

If you want the full OpenCV package with contrib modules (sometimes needed for face recognition features), use:

```bash
pip install opencv-contrib-python
```

---

## Important Notes

This project uses hardcoded absolute paths such as:

- `D:\OpenCVProject\FaceRecg`
- `C:\Python\OpenCV\BasicProjects\Harr_Cascade.xml`

So before running the scripts, you should update those file paths to match your own local folder structure.

Example:

```python
DIR = r"C:\Python\OpenCV\YourDatasetFolder"
haar_cascade = cv.CascadeClassifier(r"C:\Python\OpenCV\BasicProjects\Harr_Cascade.xml")
```

---

## Recommended Folder Structure for Training Data

```text
FaceRecg/
├── Person1/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── image3.jpg
├── Person2/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── image3.jpg
└── Person3/
    ├── image1.jpg
    └── image2.jpg
```

Each folder should contain sample images of only one person. The folder name is used as the label.

---

## Typical Execution Order

1. Place face images in labeled folders
2. Run `TrainingRecognizer.py` to collect training samples
3. Run `FaceLBPHRec.py` to train the model
4. Run `RecognizeFace.py` to test recognition on a new image

---

## Example Outcome

When recognition succeeds, the program may print output like:

```text
label = Aryan with confidence = 20
```

and draw a green rectangle around the detected face with the person name.

---

## Summary

This project is a practical OpenCV face recognition example using:

- Haar Cascade for detection
- LBPH for recognition
- labeled image folders for training
- Python + NumPy + OpenCV

It is a perfect beginner-level project for understanding how face recognition systems work in real applications.

---

## Future Improvements

You can expand this project by adding:

- webcam-based live face recognition
- better dataset organization
- confidence threshold filtering
- multiple face detection in a live video stream
- GUI interface with Tkinter or Flask

---

## Author

This project was built as a hands-on OpenCV face recognition learning project.
