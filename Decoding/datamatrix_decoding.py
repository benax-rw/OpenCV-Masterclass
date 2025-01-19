from pyzbar.pyzbar import decode
import cv2

# Read the image
image = cv2.imread("datamatrix.png")

# Decode Data Matrix
codes = decode(image)
for code in codes:
    data = code.data.decode("utf-8")
    print(f"Data Matrix Data: {data}")
    points = code.polygon
    points = [(point.x, point.y) for point in points]
    cv2.polylines(image, [np.array(points, dtype=np.int32)], True, (0, 255, 0), 2)

cv2.imshow("Data Matrix", image)
cv2.waitKey(0)
cv2.destroyAllWindows()