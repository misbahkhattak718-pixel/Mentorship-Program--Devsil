import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
image = cv2.imread('./Practice/01_python_first/hrattrition.png')

if image is None:
    print("Error: Image not found!")
    exit()

# Convert BGR to RGB (for display)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# ================================
# Method 1: OpenCV Built-in
# ================================
gray_opencv = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ================================
# Method 2: Average Method
# Gray = (R + G + B) / 3
# ================================
avg_gray = np.mean(image, axis=2).astype(np.uint8)

# ================================
# Method 3: Weighted Method (Luminosity)
# Gray = 0.299R + 0.587G + 0.114B
# ================================
B, G, R = cv2.split(image)
weighted_gray = (0.114 * B + 0.587 * G + 0.299 * R).astype(np.uint8)

# ================================
# Method 4: Max Channel Method
# ================================
max_gray = np.max(image, axis=2)

# ================================
# Method 5: Min Channel Method
# ================================
min_gray = np.min(image, axis=2)

# ================================
# Method 6: Red Channel Only
# ================================
red_gray = R

# ================================
# Method 7: Green Channel Only
# ================================
green_gray = G

# ================================
# Method 8: Blue Channel Only
# ================================
blue_gray = B

# ================================
# Display Results
# ================================
plt.figure(figsize=(15,10))

plt.subplot(3,3,1)
plt.title("Original")
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(3,3,2)
plt.title("OpenCV Gray")
plt.imshow(gray_opencv, cmap='gray')
plt.axis('off')

plt.subplot(3,3,3)
plt.title("Average Method")
plt.imshow(avg_gray, cmap='gray')
plt.axis('off')

plt.subplot(3,3,4)
plt.title("Weighted (Luminosity)")
plt.imshow(weighted_gray, cmap='gray')
plt.axis('off')

plt.subplot(3,3,5)
plt.title("Max Channel")
plt.imshow(max_gray, cmap='gray')
plt.axis('off')

plt.subplot(3,3,6)
plt.title("Min Channel")
plt.imshow(min_gray, cmap='gray')
plt.axis('off')

plt.subplot(3,3,7)
plt.title("Red Channel")
plt.imshow(red_gray, cmap='gray')
plt.axis('off')

plt.subplot(3,3,8)
plt.title("Green Channel")
plt.imshow(green_gray, cmap='gray')
plt.axis('off')

plt.subplot(3,3,9)
plt.title("Blue Channel")
plt.imshow(blue_gray, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()