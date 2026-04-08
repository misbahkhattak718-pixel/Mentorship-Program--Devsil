import cv2
 
# Load the image in color mode
image1 = cv2.imread("./Practice/01_python_first/hrattrition.png", cv2.IMREAD_COLOR)
image2 = cv2.imread("./Practice/01_python_first/Resizing.PNG", cv2.IMREAD_GRAYSCALE)

 
# Check if the image was loaded successfully
if image1 is None:
    print("Error: Image not found or unable to read.")
else:
    print("Image loaded successfully!")
if image2 is None:
    print("Error: Image not found or unable to read.")
else:
    print("Image loaded successfully!")

# Save the images in a different format
cv2.imwrite("image1.jpg", image1)
cv2.imwrite("image2.png", image2)

print("Images saved successfully!")
print("Press any key to exit.")
# Display the images.
cv2.imshow("Image 1", image1)
cv2.imshow("Image 2", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

