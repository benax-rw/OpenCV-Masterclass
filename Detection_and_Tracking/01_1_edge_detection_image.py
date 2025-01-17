import cv2

# Read the image
image = cv2.imread("car2.jpg", cv2.IMREAD_GRAYSCALE)  # Convert to grayscale for edge detection

    # Apply Canny edge detection
    # In this case, we have two ranges:
    # 1. Range A (100–200):
    # - Changes (gradients) in this range are considered potential edges.
    # - These are weaker changes that will only be marked as edges if they are connected to edges in Range B.
    # 2. Range B (200–255):
    # - Changes (gradients) in this range are considered strong edges.
    # - These are significant changes in brightness and are always marked as edges, regardless of connections.

    # The Canny method processes the input image and produces a binary image where:
    # 1. White pixels (255) represent the detected edges. These are the pixels that meet the threshold criteria for being considered edges.
    # 2. Black pixels (0) represent the non-edges. These are areas where the pixel intensity does not change significantly.   
edges = cv2.Canny(image, threshold1=100, threshold2=200)

# Display the edges
cv2.imshow("Edges", edges)

# Wait for a key press, then save the result
cv2.waitKey(0)
cv2.imwrite("canny_edges.jpg", edges)
cv2.destroyAllWindows()