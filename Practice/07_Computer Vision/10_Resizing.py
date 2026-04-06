import cv2
 
# Load the image
image = cv2.imread("./Practice/01_python_first/Resizing.PNG")
 
# Display the original image
cv2.imshow("Original Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()