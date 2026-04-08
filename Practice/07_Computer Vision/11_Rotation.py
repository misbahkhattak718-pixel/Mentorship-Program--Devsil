

import cv2

# Correct image path
image_path = "./Practice/01_python_first/hrattrition.png"

# Read image
img = cv2.imread(image_path)

# Function to display image
def new_func(img):
    cv2.imshow("Image with Line", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Check if image loaded successfully
if img is not None:
    # Draw a line on the image
    cv2.line(
        img,
        (20, 160),     # Start point
        (200, 160),    # End point
        (0, 255, 255), # Color (BGR)
        5              # Thickness
    )
    
    # Show image
    new_func(img)

else:
    print("Error: Image not found or unable to load.")