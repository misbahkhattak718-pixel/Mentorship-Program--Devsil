import cv2

# 1. Load Image
image = cv2.imread('./Practice/01_python_first/hrattrition.png')

if image is None:
    print("Error: Image not found!")
    exit()

# ================================
# 2. Access a Single Pixel
# ================================
row, col = 100, 50
pixel = image[row, col]

print("Pixel at (100,50) [BGR]:", pixel)

# Access individual channels
B = pixel[0]
G = pixel[1]
R = pixel[2]

print("Blue:", B, "Green:", G, "Red:", R)

# ================================
# 3. Modify Pixel Values
# ================================
image[row, col] = [255, 255, 255]   # White pixel
image[row, col+10] = [0, 0, 255]    # Red pixel

# ================================
# 4. Convert to Grayscale
# ================================
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Access grayscale pixel
gray_value = gray[row, col]
print("Grayscale value at (100,50):", gray_value)

# ================================
# 5. Loop Through Pixels (Partial Demo)
# ================================
height, width, channels = image.shape

print("\nFirst few pixel values:")

for i in range(3):        # only first 3 rows (for demo)
    for j in range(3):    # only first 3 columns
        print(f"Pixel ({i},{j}) =", image[i, j])

# ================================
# 6. Access Entire Channels
# ================================
blue_channel = image[:, :, 0]
green_channel = image[:, :, 1]
red_channel = image[:, :, 2]

# ================================
# 7. Show Images
# ================================
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()