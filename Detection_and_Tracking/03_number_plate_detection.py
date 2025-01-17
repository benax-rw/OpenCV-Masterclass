import cv2

# Step 1: Read the image
image = cv2.imread("car1.jpg")
if image is None:
    print("Error: Image not found!")
    exit()

# Resize for consistent processing
image = cv2.resize(image, (600, 400))  # Resize for faster processing

# Step 2: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Step 4: Apply Canny edge detection
edges = cv2.Canny(blurred, 50, 150)

# Step 5: Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Initialize variables
license_plate = None

# Step 6: Loop through contours to find the license plate
for contour in contours:
    # Approximate the contour
    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    # Check if the approximated contour has 4 points (rectangle)
    if len(approx) == 4:
        # Get the bounding box
        x, y, w, h = cv2.boundingRect(approx)

        # Calculate aspect ratio
        aspect_ratio = float(w) / h

        # Define criteria for license plate
        if 2.0 < aspect_ratio < 5.0 and 1000 < cv2.contourArea(contour) < 20000:
            license_plate = (x, y, w, h)
            break  # Stop after finding the first valid license plate

# Step 7: Highlight the detected license plate
if license_plate:
    x, y, w, h = license_plate
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)  # Green rectangle
    cv2.putText(image, "License Plate", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
else:
    print("No license plate detected!")

# Step 8: Display the results
cv2.imshow("License Plate Detection", image)

# Save the result
cv2.imwrite("detected_license_plate.jpg", image)

cv2.waitKey(0)
cv2.destroyAllWindows()