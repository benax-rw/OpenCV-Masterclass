import cv2
import pytesseract
import numpy as np
import re

# Ensure pytesseract knows the location of Tesseract (if using Windows)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Step 1: Read the input image
image = cv2.imread("car1.jpg")
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
plate_coords = None

# Step 6: Detect the license plate
for contour in contours:
    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    if len(approx) == 4:  # Check for rectangle
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h
        if 2.0 < aspect_ratio < 5.0 and 1000 < cv2.contourArea(contour) < 20000:
            license_plate = gray[y:y + h, x:x + w]  # Crop the license plate region
            plate_coords = (x, y, w, h)  # Save coordinates for annotation
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)  # Highlight plate
            break

# Step 7: Preprocess the license plate for OCR
if license_plate is not None:
    # Enhance the license plate
    _, license_plate_bin = cv2.threshold(license_plate, 127, 255, cv2.THRESH_BINARY)  # Binarize

    # Apply dilation to emphasize characters
    kernel = np.ones((3, 3), np.uint8)
    license_plate_dilated = cv2.dilate(license_plate_bin, kernel, iterations=1)

    # Detect contours within the license plate region
    contours_text, _ = cv2.findContours(license_plate_dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter out small or irrelevant contours
    mask = np.zeros_like(license_plate_dilated)
    for cnt in contours_text:
        if cv2.contourArea(cnt) > 50:  # Keep only significant contours
            cv2.drawContours(mask, [cnt], -1, 255, -1)

    # Perform OCR on the filtered image
    filtered_license_plate = cv2.bitwise_and(license_plate_dilated, mask)
    custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    raw_text = pytesseract.image_to_string(filtered_license_plate, config=custom_config).strip()
    print("Raw OCR Text:", raw_text)

    # Step 8: Post-OCR correction
    # Use regex to match the expected license plate format
    match = re.match(r'^[A-Z0-9]{6,7}$', raw_text)
    corrected_text = match.group() if match else raw_text[:7]  # Trim to 7 characters if needed
    print("Corrected License Plate Text:", corrected_text)

    # Annotate the text on the original image
    if plate_coords:
        x, y, w, h = plate_coords
        cv2.putText(image, corrected_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Display the processed license plate
    cv2.imshow("Processed License Plate", filtered_license_plate)
else:
    print("License plate not detected!")

# Step 9: Display the annotated image
cv2.imshow("License Plate Detection with Annotation", image)

# Save the result
cv2.imwrite("annotated_license_plate.jpg", image)

cv2.waitKey(0)
cv2.destroyAllWindows()