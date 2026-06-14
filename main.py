import cv2
import numpy as np

# Load image
image = cv2.imread("road.jpg")

# Check if image exists
if image is None:
    print("Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blur image
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect edges
edges = cv2.Canny(blur, 50, 150)

# Save output
cv2.imwrite("lane_edges.jpg", edges)

print("Lane detection completed!")
