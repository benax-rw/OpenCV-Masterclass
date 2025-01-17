# you need to make sure you have opencv-contrib-python==4.5.5.64
# pip uninstall opencv-python opencv-contrib-python
#pip install opencv-contrib-python==4.5.5.64
import cv2
import time
import math

# Initialize video capture
cap = cv2.VideoCapture(0)

# Initialize tracker
tracker = cv2.TrackerCSRT_create()

# Read the first frame
ret, frame = cap.read()
if not ret:
    print("Failed to read video")
    cap.release()
    exit()

# Select ROI (Region of Interest) for tracking
bbox = cv2.selectROI("Frame", frame, False)
tracker.init(frame, bbox)

# Variables for direction and speed calculation
prev_center = None
prev_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Update the tracker
    success, bbox = tracker.update(frame)

    if success:
        # Calculate the current center of the object
        x, y, w, h = map(int, bbox)
        current_center = (x + w // 2, y + h // 2)

        # Draw the bounding box and center point
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(frame, current_center, 5, (0, 0, 255), -1)

        # Calculate direction and speed if previous center exists
        if prev_center is not None:
            dx = current_center[0] - prev_center[0]
            dy = current_center[1] - prev_center[1]

            # Determine direction
            if abs(dx) > abs(dy):  # Horizontal movement
                direction = "Right" if dx > 0 else "Left"
            else:  # Vertical movement
                direction = "Down" if dy > 0 else "Up"

            # Calculate speed
            current_time = time.time()
            dt = current_time - prev_time  # Time difference
            distance = math.sqrt(dx**2 + dy**2)  # Euclidean distance
            speed = distance / dt if dt > 0 else 0

            # Update previous time
            prev_time = current_time

            # Display direction and speed
            cv2.putText(frame, f"Direction: {direction}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            cv2.putText(frame, f"Speed: {speed:.2f} px/s", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

        # Update previous center
        prev_center = current_center

    else:
        cv2.putText(frame, "Lost Tracking", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    # Display the frame
    cv2.imshow("Direction and Speed Detection", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()