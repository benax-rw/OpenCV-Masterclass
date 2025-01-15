import cv2
import numpy as np

# Step 1: Read the input image
image = cv2.imread("car1.jpg")  # Load the image containing shapes

# Step 2: Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply binary thresholding
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Step 4: Find contours in the binary image
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Step 5: Generate a random color for each detected shape instance
def generate_random_color():
    return tuple(np.random.randint(0, 256, size=3).tolist())  # Generate random RGB values

# Initialize shape counters
shape_count = {"Triangle": 0, "Square": 0, "Rectangle": 0, "Circle": 0, "Line": 0, "Polygon": 0}

# Step 6: Loop through each contour to detect and annotate the shape
for contour in contours:
    # Approximate the contour
    epsilon = 0.02 * cv2.arcLength(contour, True)  # Smaller epsilon for better approximation
    approx = cv2.approxPolyDP(contour, epsilon, True)

    # Find the center of the shape for annotation
    M = cv2.moments(contour)
    if M["m00"] != 0:  # Avoid division by zero
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
    else:
        cx, cy = 0, 0

    # Classify the shape
    if len(approx) == 2:  # Line detection
        shape_name = "Line"
    elif len(approx) == 3:
        shape_name = "Triangle"
    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h
        if 0.95 <= aspect_ratio <= 1.05:
            shape_name = "Square"
        else:
            shape_name = "Rectangle"
    else:
        # Check for circularity
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        if perimeter > 0:  # Avoid division by zero
            circularity = (4 * np.pi * area) / (perimeter ** 2)
            if 0.8 <= circularity <= 1.2:  # Circularity close to 1 indicates a circle
                shape_name = "Circle"
            else:
                shape_name = "Polygon"
        else:
            shape_name = "Polygon"

    # Update the shape count
    shape_count[shape_name] += 1

    # Generate a random unique color for this shape instance
    color = generate_random_color()

    # Draw the contour with the unique color
    cv2.drawContours(image, [contour], -1, color, 3)

    # Annotate the shape name on the image with the same color
    cv2.putText(image, f"{shape_name}", (cx - 50, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

# Step 7: Display the image with annotated shapes
cv2.imshow("Annotated Shapes with Unique Colors", image)

# Print the shape counts
print("Detected shapes:", shape_count)

# Step 8: Wait for a key press, then save the resulting image
cv2.waitKey(0)
cv2.imwrite("annotated_shapes_unique_colors.jpg", image)
cv2.destroyAllWindows()