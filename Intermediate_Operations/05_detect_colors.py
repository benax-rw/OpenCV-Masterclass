import cv2
import numpy as np

# Step 1: Define color ranges and their corresponding names
colors = {
    "Red": ([0, 120, 70], [10, 255, 255]),
    "Green": ([36, 100, 100], [86, 255, 255]),
    "Blue": ([94, 80, 2], [126, 255, 255]),
    "Yellow": ([22, 93, 200], [45, 255, 255]),
    "Orange": ([10, 100, 20], [25, 255, 255]),
    "Purple": ([129, 50, 70], [158, 255, 255]),
    "White": ([0, 0, 200], [180, 30, 255]),
}

# Step 2: Start the webcam feed
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Resize the frame for consistent processing
    frame = cv2.resize(frame, (640, 480))

    # Convert the frame to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Initialize variables to annotate the color
    detected_color = None
    max_area = 0

    for color_name, (lower, upper) in colors.items():
        # Convert the lower and upper bounds to NumPy arrays
        lower_bound = np.array(lower, dtype="uint8")
        upper_bound = np.array(upper, dtype="uint8")

        # Create a mask for the color
        mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            # Filter out small contours
            area = cv2.contourArea(contour)
            if area > max_area:  # Keep the largest contour
                max_area = area
                detected_color = color_name

                # Get the bounding box of the largest contour
                x, y, w, h = cv2.boundingRect(contour)

                # Draw the bounding box and annotate the color
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
                cv2.putText(frame, color_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # Display the frame with the detected color annotation
    cv2.imshow("Color Detection", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()