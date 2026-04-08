import cv2
 
# Load the image
image = cv2.imread("./Practice/01_python_first/hrattrition.png")
 
# Scaling factors for resizing
scale_down = 0.077  
scale_up = 0.088    
 
# Resize the image (scaling down)
resized_down = cv2.resize(image, None, fx=scale_down, fy=scale_down, interpolation=cv2.INTER_LINEAR)
 
# Resize the image (scaling up)
resized_up = cv2.resize(image, None, fx=scale_up, fy=scale_up, interpolation=cv2.INTER_LINEAR)
 
# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Scaled Down Image", resized_down)
cv2.imshow("Scaled Up Image", resized_up)
cv2.waitKey(0)
cv2.destroyAllWindows()