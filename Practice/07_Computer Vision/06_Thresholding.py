import cv2
import matplotlib.pyplot as plt
 
# Read the image
img = cv2.imread('./Practice/01_python_first/hrattrition.png', ) # 0 
 
# Apply different thresholding techniques
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, binary_inv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, trunc = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, tozero = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, tozero_inv = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
 
# Display the results
cv2.imshow("binary",binary)
cv2.imshow("binary_inv",binary_inv)
cv2.imshow("trunc",trunc)
cv2.imshow("tozero",tozero)
cv2.imshow("tozero_inv",tozero_inv)
 
cv2.waitKey(0)
cv2.destroyAllWindows()