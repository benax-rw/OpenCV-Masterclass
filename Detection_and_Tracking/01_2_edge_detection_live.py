import cv2

# Open the webcam (camera index 0)
capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("Error: Could not open webcam.")
    exit()

saved_count = 0  # Counter for saved images

while True:
    # Capture each frame from the webcam
    #when returned is true=success otherwise the capture failed
    returned, frame = capture.read()  
    if not returned:
        print("Error: Failed to capture frame.")
        break

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray_frame, threshold1=100, threshold2=200)

    # Display the edges
    cv2.imshow("Live Edge Detection", edges)

    # Capture key presses
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):  # Exit when 'q' is pressed
        break
    elif key == ord('s'):  # Save the current frame when 's' is pressed
        filename = f"edges_frame_{saved_count}.jpg"
        cv2.imwrite(filename, edges)
        print(f"Saved: {filename}")
        saved_count += 1

# Release the webcam and close all windows
capture.release()
cv2.destroyAllWindows()