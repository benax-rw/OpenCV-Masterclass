import cv2
import numpy as np
import time
import os

# Ensure the "motion_images" directory exists
output_folder = "motion_images"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Initialize video capture
cap = cv2.VideoCapture(0)  # Use 0 for webcam, or replace with a video file path

# Initialize background subtractor
background_subtractor = cv2.createBackgroundSubtractorMOG2()

# Track motion state
motion_detected = False

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

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:  # Ignore small movements
            motion_rate += area  # Add the area of the contour to motion rate
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green bounding box

    # Calculate the motion rate as a percentage of the frame area
    motion_rate_percentage = (motion_rate / (frame.shape[0] * frame.shape[1])) * 100

    # Only count motion if rate exceeds 10%
    if motion_rate_percentage > 30:
        new_motion_detected = True

    # If motion is newly detected, save the frame
    if new_motion_detected and not motion_detected:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(output_folder, f"motion_{timestamp}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Motion detected! Image saved as {filename}")

    # Update motion state
    motion_detected = new_motion_detected

    # Create the annotation window
    annotation = np.zeros((200, 640, 3), dtype=np.uint8)  # Black window for text

    # Annotate motion state in the annotation window
    if motion_detected:
        motion_rate_text = f"Moving at the rate: {motion_rate_percentage:.2f}%"
        cv2.putText(annotation, "Motion Detected", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)  # Green text
        cv2.putText(annotation, motion_rate_text, (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
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