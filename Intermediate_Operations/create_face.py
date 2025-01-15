import cv2
import numpy as np

# Create a blank white image
image = np.ones((400, 400, 3), dtype="uint8") * 255

# Draw the face (circle)
cv2.circle(image, (200, 200), 100, (0, 0, 0), 3)

# Draw the eyes (two small circles)
cv2.circle(image, (170, 180), 10, (0, 0, 0), -1)  # Left eye
cv2.circle(image, (230, 180), 10, (0, 0, 0), -1)  # Right eye

# Draw the mouth (ellipse)
cv2.ellipse(image, (200, 240), (50, 20), 0, 0, 180, (0, 0, 0), 3)

# Save the image as "face_image.jpg"
cv2.imwrite("face_image.jpg", image)

# Display the generated image
cv2.imshow("Generated Face", image)
cv2.waitKey(0)
cv2.destroyAllWindows()