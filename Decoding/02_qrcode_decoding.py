import cv2

# Initialize QR code detector
detector = cv2.QRCodeDetector()

# Read the image
image = cv2.imread("qrcode.png")

# Detect and decode the QR code
data, points, _ = detector.detectAndDecode(image)

if data:
    print(f"QR Code Data: {data}")
    cv2.polylines(image, [points.astype(int)], True, (0, 255, 0), 2)
else:
    print("No QR code detected.")

cv2.imshow("QR Code", image)
cv2.waitKey(0)
cv2.destroyAllWindows()