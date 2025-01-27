Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
pip install opencv-python
SyntaxError: invalid syntax
import cv2
print(cv2.__version__)
4.10.0
img=cv2.imread(r'IMG_7759.JPG',1)
print(img)
