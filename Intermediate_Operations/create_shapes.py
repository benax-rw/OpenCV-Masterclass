import cv2
import numpy as np

# Create a blank white image
image = np.ones((500, 500, 3), dtype="uint8") * 255

# Draw shapes on the image
cv2.rectangle(image, (50, 50), (200, 200), (0, 0, 0), -1)  # Black rectangle
cv2.circle(image, (300, 300), 50, (0, 0, 0), -1)            # Black circle
cv2.line(image, (400, 50), (400, 200), (0, 0, 0), 5)        # Black line
cv2.polylines(image, [np.array([[250, 400], [300, 450], [200, 450]], dtype=np.int32)], 
              True, (0, 0, 0), 3)                           # Black triangle

# Save the image as "shapes.png"
cv2.imwrite("shapes.png", image)

# Display the created image
cv2.imshow("Shapes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()