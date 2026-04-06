import cv2
import numpy as np

# 1. Load the color image
image = cv2.imread('./Practice/01_python_first/hrattrition.png')

if image is None:
    print("Error: Image not found!")
    exit()

# Get image dimensions
height, width, channels = image.shape

# ================================
# Method 1: Manual Pixel Iteration (Weighted)
# ================================
gray_manual = np.zeros((height, width), dtype=np.uint8)

for i in range(height):
    for j in range(width):
        # OpenCV uses BGR format
        B = image[i, j][0]
        G = image[i, j][1]
        R = image[i, j][2]

        # 3. Weighted grayscale formula
        gray_value = int(0.114 * B + 0.587 * G + 0.299 * R)

        # 4. Assign value
        gray_manual[i, j] = gray_value

# ================================
# Method 2: Average Method (Manual Loop)
# ================================
gray_average = np.zeros((height, width), dtype=np.uint8)

for i in range(height):
    for j in range(width):
        B, G, R = image[i, j]
        gray_value = int((B + G + R) / 3)
        gray_average[i, j] = gray_value

# ================================
# Method 3: OpenCV Built-in
# ================================
gray_opencv = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ================================
# Method 4: NumPy Vectorized (Fast)
# ================================
gray_numpy = (0.114 * image[:,:,0] + 
              0.587 * image[:,:,1] + 
              0.299 * image[:,:,2]).astype(np.uint8)

# ================================
# Method 5: Max Channel
# ================================
gray_max = np.max(image, axis=2)

# ================================
# Method 6: Min Channel
# ================================
gray_min = np.min(image, axis=2)

# ================================
# 5. Display Images using cv2.imshow()
# ================================
cv2.imshow("Original Image", image)
cv2.imshow("Gray Manual (Weighted)", gray_manual)
cv2.imshow("Gray Average", gray_average)
cv2.imshow("Gray OpenCV", gray_opencv)
cv2.imshow("Gray NumPy", gray_numpy)
cv2.imshow("Gray Max", gray_max)
cv2.imshow("Gray Min", gray_min)

# Wait and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()