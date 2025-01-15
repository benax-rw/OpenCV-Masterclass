import cv2
import numpy as np

# Step 1: Initialize video capture
cap = cv2.VideoCapture(0)  # Use 0 for webcam, or replace with a video file path

# Step 2: Initialize background subtractor
background_subtractor = cv2.createBackgroundSubtractorMOG2()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Resize for consistent processing
    frame = cv2.resize(frame, (640, 480))

    # Apply the background subtractor to get the foreground mask
    mask = background_subtractor.apply(frame)

    # Optional: Apply thresholding to clean up the mask
    _, mask = cv2.threshold(mask, 50, 255, cv2.THRESH_BINARY)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize motion state
    motion_detected = False

    # Draw bounding boxes around detected motion
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Ignore small movements
            motion_detected = True
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green bounding box

    # Create the annotation window
    annotation = np.zeros((200, 640, 3), dtype=np.uint8)  # Black window for text

    # Annotate motion state in the annotation window
    if motion_detected:
        cv2.putText(annotation, "Motion Detected", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)  # Green text
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