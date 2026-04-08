# Python program to explain cv2.flip() method

# importing cv2
import cv2

# path
path = r'./Practice/01_python_first/hrattrition.png'

# Reading an image in default mode
src = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Image'

# Using cv2.flip() method
# Use Flip code 0 to flip vertically
image = cv2.flip(src, 0)

# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)