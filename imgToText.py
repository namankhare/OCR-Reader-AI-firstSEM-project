"""Program for reading Text from images"""

# PIL is a library in python that adds support for opening, manipulating, and saving many different image file formats.
from PIL import Image
# pytsseract is an OCR tool for python. It will read and recognize the text in images, license plates etc.
import pytesseract
# OpenCV-Python is a library of Python bindings designed to solve computer vision problems.
import cv2

# Defining the path of tesseract.exe in our device.
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
# Reading image
img = cv2.imread('glt.jpg')
# Converting image to string and printing it.
text = pytesseract.image_to_string(Image.open('glt.jpg'), lang="eng")
print(text)
# Creates a window
cv2.namedWindow("Input image")
# Displays an image in the specified window
cv2.imshow("Input image", img)
# Waits for a pressed key.
cv2.waitKey(0)


