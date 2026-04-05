import cv2

import matplotlib.pyplot as plt

# 1. Load the image
image = cv2.imread("./Practice/01_python_first/hrattrition.png")

# Check if image loaded properly
if image is None:
    print("Error: Image not found!")
    exit()

# 2. Convert BGR to RGB (for correct display)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 3. Convert to Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 4. Apply Gaussian Blur (reduce noise)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# 5. Edge Detection (Canny)
edges = cv2.Canny(blur, 100, 200)

# 6. Thresholding (Binary Image)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# 7. Display all results
plt.figure(figsize=(12,8))

plt.subplot(2,3,1)
plt.title("Original")
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(2,3,2)
plt.title("Grayscale")
plt.imshow(gray, cmap='gray')
plt.axis('off')

plt.subplot(2,3,3)
plt.title("Blur")
plt.imshow(blur, cmap='gray')
plt.axis('off')

plt.subplot(2,3,4)
plt.title("Edges")
plt.imshow(edges, cmap='gray')
plt.axis('off')

plt.subplot(2,3,5)
plt.title("Threshold")
plt.imshow(thresh, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()