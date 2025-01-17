import cv2
import numpy as np
import time
import os

# Ensure the "motion_images" directory exists
output_folder = "motion_images"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Initialize video capture
cap = cv2.VideoCapture(0)

# Initialize background subtractor
background_subtractor = cv2.createBackgroundSubtractorMOG2()

# Track motion state, previous centroids, and cumulative displacement
motion_detected = False
prev_centroids = []
cumulative_dx = 0
cumulative_dy = 0

# Threshold for significant movement
movement_threshold = 10  # Minimum displacement to consider

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Resize for consistent processing
    frame = cv2.resize(frame, (640, 480))

    # Apply the background subtractor to get the foreground mask
    mask = background_subtractor.apply(frame)

    # Apply thresholding to clean up the mask
    _, mask = cv2.threshold(mask, 50, 255, cv2.THRESH_BINARY)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize motion state and motion rate
    new_motion_detected = False
    motion_rate = 0  # Represents the total area of motion
    current_centroids = []

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:  # Ignore small movements
            motion_rate += area  # Add the area of the contour to motion rate
            x, y, w, h = cv2.boundingRect(contour)
            cx, cy = x + w // 2, y + h // 2  # Calculate the centroid
            current_centroids.append((cx, cy))
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green bounding box

    # Calculate the motion rate as a percentage of the frame area
    motion_rate_percentage = (motion_rate / (frame.shape[0] * frame.shape[1])) * 100

    # Only count motion if rate exceeds 3%
    if motion_rate_percentage > 3:
        new_motion_detected = True

    # Calculate cumulative displacement for dominant direction
    if prev_centroids and current_centroids:
        for prev, curr in zip(prev_centroids, current_centroids):
            dx = curr[0] - prev[0]
            dy = curr[1] - prev[1]

            # Only add significant displacement to cumulative values
            if abs(dx) > movement_threshold:
                cumulative_dx += dx
            if abs(dy) > movement_threshold:
                cumulative_dy += dy

    # Determine dominant direction based on net cumulative displacement
    if abs(cumulative_dx) > abs(cumulative_dy):
        dominant_direction = "Right" if cumulative_dx > 0 else "Left"
    else:
        dominant_direction = "Down" if cumulative_dy > 0 else "Up"

    # Save the frame if motion is detected
    if new_motion_detected and not motion_detected:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(output_folder, f"motion_{timestamp}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Motion detected! Image saved as {filename}")

    # Update previous centroids and motion state
    prev_centroids = current_centroids
    motion_detected = new_motion_detected

    # Create the annotation window
    annotation = np.zeros((200, 640, 3), dtype=np.uint8)  # Black window for text

    # Annotate motion state in the annotation window
    if motion_detected:
        motion_rate_text = f"Moving at the rate: {motion_rate_percentage:.2f}%"
        cv2.putText(annotation, "Motion Detected", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)  # Green text
        cv2.putText(annotation, motion_rate_text, (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(annotation, f"Dominant Direction: {dominant_direction}", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
    else:
        cv2.putText(annotation, "No Motion", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)  # Red text

    # Display the frame, mask, and annotation window
    cv2.imshow("Motion Detection", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Annotation", annotation)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()